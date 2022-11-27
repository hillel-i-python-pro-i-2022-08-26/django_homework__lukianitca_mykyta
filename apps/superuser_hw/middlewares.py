import logging
from collections.abc import Callable

from django.http import HttpRequest

from apps.superuser_hw.services import manage_request_object


class LogTrackRequestsMiddleware:
    _NAME = "Tracking Requests Middleware"

    def __init__(self, get_response: Callable):
        self.get_response = get_response
        self.logger = logging.getLogger("django")
        self.logger.info(f"Init {self._NAME}")

    def __call__(self, request: HttpRequest):

        self.logger.info("[START] request tracking [START]")

        manage_request_object(request)

        self.logger.info("[END] request tracking [END]")
        return self.get_response(request)
