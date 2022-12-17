from django.db.models import Sum

from apps.superuser_hw.services.extra_structures import RequestInfo


class Aggregator:
    def __init__(self, queryset):
        self.queryset = queryset

    def aggregate_requests(self):
        request_info = RequestInfo(
            self.queryset.aggregate(Sum("visits_count")).get("visits_count__sum"),
            self.queryset.count(),
        )
        return {"request_info": request_info}
