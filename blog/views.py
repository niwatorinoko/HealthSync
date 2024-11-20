from django.views.generic import TemplateView


class ExpertsView(TemplateView):
    template_name = 'blog/experts.html'

class MentalView(TemplateView):
    template_name = 'blog/mental.html'

class SleepRecoveryView(TemplateView):
    template_name = 'blog/sleeprecovery.html'