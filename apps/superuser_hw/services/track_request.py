from logging import Logger

from django.http import HttpRequest

from apps.superuser_hw.models import Request


def normalize_session_key(session):
    if not session.session_key:
        session.save()
    return session.session_key


class RequestTracker:
    def __init__(self, request_obj: HttpRequest, logger: Logger):
        self.request_obj = request_obj
        self.logger = logger

    def manage_request_object(self):
        request_info = self._collect_request_info()
        self.logger.info(
            f"[INFO] "
            f"{request_info['user'] or 'Anonymous User'} - {request_info['path']} - {request_info['session_key']}"
            f" [INFO]",
        )
        if request_record := Request.objects.filter(**request_info).first():
            self.logger.info("[ACTION-START] Request record exists. Start updating [ACTION-START]")
            self._update_request_record(request_record)
        else:
            self.logger.info("[ACTION-START] Request record doesn't exist. Start creating [ACTION-START]")
            self._create_request_record(request_info)

    def _collect_request_info(self):
        user = self.request_obj.user if self.request_obj.user.is_authenticated else None

        return {
            "session_key": normalize_session_key(self.request_obj.session),
            "user": user,
            "path": self.request_obj.path,
        }

    def _update_request_record(self, request_record: Request):
        request_record.visits_count += 1
        self.logger.info(f"[INSTANCE] {request_record} [INSTANCE]")
        request_record.save()
        self.logger.info("[ACTION-END] Request record updated successfully [ACTION-END]")

    def _create_request_record(self, request_info: dict):
        request_record = Request(**request_info)
        self.logger.info(f"[INSTANCE] {request_record} [INSTANCE]")
        request_record.save()
        self.logger.info("[ACTION-END] Request record created successfully [ACTION-END]")
