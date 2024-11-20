from django.urls import path
from .views import EventsView, ClinicView, FactsView, GlobalIssueView, QuotesView, TipsView

app_name = 'news'

urlpatterns = [
    path('event/', EventsView.as_view(), name='event'),
    path('clinic/', ClinicView.as_view(), name='clinic'),
    path('facts/', FactsView.as_view(), name='facts'),
    path('global_issue/', GlobalIssueView.as_view(), name='global_issue'),
    path('quotes/', QuotesView.as_view(), name='quotes'),
    path('tips/', TipsView.as_view(), name='tips'),
]
#http://0.0.0.0:8000/accounts/nutrition_plan/