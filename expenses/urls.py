from django.urls import path
from .views import ExpenseCreateAPI, ExpenseListAPI, ExpenseDeleteAPI, ExpenseAiOverviewAPI, home_ui


urlpatterns = [
    path("", home_ui),
    path("api/expense/create/", ExpenseCreateAPI.as_view()),
    path("api/expense/list/", ExpenseListAPI.as_view()),
    path("api/expense/delete/", ExpenseDeleteAPI.as_view()),
    path("api/expense/ai-overview/", ExpenseAiOverviewAPI.as_view()),
]