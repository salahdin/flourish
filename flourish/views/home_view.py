from django.views.generic import TemplateView
from edc_base.view_mixins import EdcBaseViewMixin
from edc_navbar import NavbarViewMixin

from flourish_caregiver.models import SubjectConsent


class HomeView(EdcBaseViewMixin, NavbarViewMixin, TemplateView):

    template_name = 'flourish/home.html'
    navbar_name = 'flourish'
    navbar_selected_item = 'home'

    @property
    def total_flourish_consents(self):
        """Returns flourish consents.
        """
        return SubjectConsent.objects.all().count()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context.update(
            flourish_consents=self.total_flourish_consents)
        return context
