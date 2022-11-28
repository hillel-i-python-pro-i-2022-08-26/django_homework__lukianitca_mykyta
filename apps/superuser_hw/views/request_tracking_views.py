from django.views.generic import ListView

from apps.superuser_hw.models import Request


class AllRequestsView(ListView):
    model = Request
    context_object_name = "requests"
    template_name = "request_tracking/show_requests.html"
