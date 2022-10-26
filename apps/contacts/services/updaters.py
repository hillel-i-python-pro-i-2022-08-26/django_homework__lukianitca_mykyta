from django.http import HttpRequest
from django.utils import timezone


def update_request_obj(request: HttpRequest) -> HttpRequest:
    visited_contacts = request.session.get("visited", 0)
    request.session.update({
        "visited": visited_contacts + 1,
        "last_visit": timezone.now().strftime("%Y-%m-%d %H:%M:%S"),
    })
    return request

