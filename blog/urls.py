from django.urls import path
from .views import ExpertsView, MentalView, SleepRecoveryView

app_name = 'news'

urlpatterns = [
    path('experts/', ExpertsView.as_view(), name='experts'),
    path('mental/', MentalView.as_view(), name='mental'),
    path('sleeprecovery/', SleepRecoveryView.as_view(), name='sleeprecovery'),
]