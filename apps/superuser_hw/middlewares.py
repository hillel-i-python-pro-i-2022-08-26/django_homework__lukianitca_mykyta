import logging
from collections.abc import Callable

from django.http import HttpRequest


class LogTrackRequestsMiddleware:
    _NAME = "Tracking Requests Middleware"

    def __init__(self, get_response: Callable):
        self.get_response = get_response
        self.logger = logging.getLogger("django")
        self.logger.info(f"Init {self._NAME}")

    def __call__(self, request: HttpRequest):

        self.logger.info(f"Current User: {request.user}")
        return self.get_response(request)
