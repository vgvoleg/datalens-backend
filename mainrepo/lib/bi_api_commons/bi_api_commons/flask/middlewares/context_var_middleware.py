"""
Middleware to reset context on each request.
"""
from __future__ import annotations

import contextvars
from typing import TYPE_CHECKING

from bi_api_commons.flask.middlewares.wsgi_middleware import FlaskWSGIMiddleware

if TYPE_CHECKING:
    from bi_api_commons.flask.types import WSGIEnviron, WSGIStartResponse, WSGIReturn


class ContextVarMiddleware(FlaskWSGIMiddleware):
    _APP_FLAG_ATTR_NAME = "_bi_middleware_flag_context_var"

    def wsgi_app(self, environ: WSGIEnviron, start_response: WSGIStartResponse) -> WSGIReturn:
        ctx = contextvars.Context()
        return ctx.run(self.original_wsgi_app, environ, start_response)