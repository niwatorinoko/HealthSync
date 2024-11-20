from django.views.generic import TemplateView


class EventsView(TemplateView):
    template_name = 'news/events.html'

class ClinicView(TemplateView):
    template_name = 'news/clinic.html'

class FactsView(TemplateView):
    template_name = 'news/facts.html'

class GlobalIssueView(TemplateView):
    template_name = 'news/globalissue.html'

class QuotesView(TemplateView):
    template_name = 'news/quotes.html'

class TipsView(TemplateView):
    template_name = 'news/tips.html'