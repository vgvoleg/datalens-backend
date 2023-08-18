from __future__ import annotations

import json
import logging

import flask
import requests
from werkzeug.exceptions import Forbidden

from bi_constants.api_constants import DLHeadersCommon, DLCookiesCommon
from bi_api_commons.access_control_common import match_path_prefix, get_token_from_authorization_header, AuthTokenType
from bi_api_commons.base_models import TenantCommon, YaTeamAuthData
from bi_api_commons.flask.middlewares.commit_rci_middleware import ReqCtxInfoMiddleware

from bi_blackbox_client.authenticate import authenticate

LOGGER = logging.getLogger(__name__)


def _check_auth(skip_auth_path_list: tuple[str, ...]) -> None:
    """
    Check current request is authorized using blackbox api.
    """
    should_skip_auth = match_path_prefix(
        skip_auth_path_list,
        flask.request.path,
    )
    if should_skip_auth:
        return

    host = flask.request.environ.get('HTTP_HOST')
    if not host:
        host = flask.current_app.config['SERVER_NAME']
        host = host.split(':')[0]

    rci = ReqCtxInfoMiddleware.get_last_resort_rci()
    assert rci, "Can not get any RCI for current request"
    req_id = rci.request_id

    secret_session_id_cookie = flask.request.cookies.get(DLCookiesCommon.YA_TEAM_SESSION_ID.value, None)
    secret_sessionid2_cookie = flask.request.cookies.get(DLCookiesCommon.YA_TEAM_SESSION_ID_2.value, None)
    secret_authorization_header_value = flask.request.headers.get(DLHeadersCommon.AUTHORIZATION_TOKEN.value)

    user_ip = (
        flask.request.access_route[-2] if len(flask.request.access_route) > 1
        else flask.request.access_route[0]
    )
    auth_res = authenticate(
        session_id_cookie=secret_session_id_cookie,
        sessionid2_cookie=secret_sessionid2_cookie,
        authorization_header=secret_authorization_header_value,
        host=host,
        userip=user_ip,
        requests_session=flask.current_app.blackbox_requests_session,
        timeout=flask.current_app.config['BLACKBOX_TIMEOUT'],
        statbox_id=req_id,
    )

    if auth_res['username'] is None:
        LOGGER.info("Blackbox auth was not passed. Blackbox resp: %s", json.dumps(
            auth_res.get('blackbox_response')
        ))
        raise Forbidden()

    auth_data = YaTeamAuthData(
        oauth_token=get_token_from_authorization_header(secret_authorization_header_value, AuthTokenType.oauth),
        cookie_session_id=secret_session_id_cookie,
        cookie_sessionid2=secret_sessionid2_cookie,
    )
    temp_rci = ReqCtxInfoMiddleware.get_temp_rci()
    enriched_temp_rci = temp_rci.clone(
        user_name=auth_res['username'],
        user_id=auth_res['user_id'],
        auth_data=auth_data,
        tenant=TenantCommon(),
    )
    ReqCtxInfoMiddleware.replace_temp_rci(enriched_temp_rci)


def set_up(app: flask.Flask, skip_auth_path_list: tuple[str, ...] = ()) -> None:
    session = requests.Session()
    adapter = requests.adapters.HTTPAdapter(
        max_retries=requests.packages.urllib3.Retry(
            **dict(
                app.config['BLACKBOX_RETRY_PARAMS'],
                method_whitelist=('GET', 'POST'),
            ),
        ),
    )
    session.mount('http://', adapter)
    session.mount('https://', adapter)
    app.blackbox_requests_session = session
    app.before_request(lambda: _check_auth(skip_auth_path_list=skip_auth_path_list))
