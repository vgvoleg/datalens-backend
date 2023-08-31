from __future__ import annotations

import os
from typing import ClassVar

from aiohttp import web

from statcommons.unistat.common import dump_for_prometheus
from statcommons.unistat.uwsgi import uwsgi_prometheus

from bi_api_commons.aiohttp.aiohttp_wrappers import DLRequestView, RequiredResourceCommon, RequiredResource


class MetricsView(DLRequestView):
    REQUIRED_RESOURCES: ClassVar[frozenset[RequiredResource]] = frozenset({RequiredResourceCommon.SKIP_AUTH})

    async def get(self):  # type: ignore  # TODO: fix
        result = []
        if os.environ.get('UWSGI_STATS'):
            uwsgi_metrics = uwsgi_prometheus(label_prefix='uwsgi_')
            result.extend(uwsgi_metrics)

        body = ''.join(dump_for_prometheus(result))
        return web.Response(text=body)