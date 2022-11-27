from django.http import HttpRequest

from apps.superuser_hw.models import Request


def collect_request_info(request_obj: HttpRequest):
    session = request_obj.session
    if not session.session_key:
        session.save()

    user = request_obj.user if request_obj.user.is_authenticated else None

    return {
        "session_key": session.session_key,
        "user": user,
        "path": request_obj.path,
    }


def update_request_record(request_record: Request):
    request_record.visits_count += 1
    request_record.save()
    return


def create_request_record(request_info: dict):
    Request(**request_info).save()
    return


def manage_request_object(request_obj):
    request_info = collect_request_info(request_obj)
    if request_record := Request.objects.filter(**request_info).first():
        update_request_record(request_record)
    else:
        create_request_record(request_info)
