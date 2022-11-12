from django.views.generic import TemplateView

from apps.base.services import FakeEngine, UsersDataGenerator


# def index(request):
#     return render(request, "base/index.html", {"title": "Main page"})


class IndexPage(TemplateView):
    template_name = "base/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Main page"
        return context


# def greetings(request, username: str | None = None):
#     if not username:
#         username = FakeEngine().generate_fake_name()
#     context = {
#         "username": username,
#         "title": "Greetings",
#         "current_offers": [f"Offer {i}" for i in range(1, 6)],
#     }
#     return render(request, "base/greet_user.html", context)


class GreetingsPage(TemplateView):
    template_name = "base/greet_user.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        username = self.kwargs.get("username")
        if not username:
            username = FakeEngine().generate_fake_name()
        context.update(
            {
                "username": username,
                "title": "Greetings",
                "current_offers": [f"Offer {i}" for i in range(1, 6)],
            }
        )
        return context


# def users_info(request, amount_users: int | None = 10):
#     users_list = UsersDataGenerator(amount_users).unique_users
#     return render(request, "base/unique_users.html", {"title": "Unique Users", "unique_users": users_list})


class UsersInfoView(TemplateView):
    template_name = "base/unique_users.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        amount_users = self.kwargs.get("amount_users", 10)
        context.update(
            {
                "title": "Unique Users",
                "unique_users": UsersDataGenerator(amount_users).unique_users,
            }
        )
        return context
