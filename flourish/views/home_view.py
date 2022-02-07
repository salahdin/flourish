import imp
from django.apps import apps as django_apps
from django.views.generic import TemplateView
from edc_base.view_mixins import EdcBaseViewMixin
from edc_navbar import NavbarViewMixin
from flourish_caregiver.models import *
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

    @property
    def total_child_assents(self):
        child_assent_cls = django_apps.get_model('flourish_child.childassent')
        return child_assent_cls.objects.count()

    @property
    def total_child_consents(self):
        child_consent_cls = django_apps.get_model(
            'flourish_caregiver.caregiverchildconsent')
        return child_consent_cls.objects.count()

    @property
    def total_continued_consents(self):
        continued_consent_cls = django_apps.get_model(
            'flourish_child.childcontinuedconsent')
        return continued_consent_cls.objects.count()

    @property
    def total_caregiver_prev_study(self):
        """
        Caregiver From Metadataset
        """

        metadataset_pids = MaternalDataset.objects.values_list(
            'screening_identifier', flat=True).distinct()
        subject_consents = SubjectConsent.objects.filter(
            screening_identifier__in=metadataset_pids).values_list('subject_identifier').distinct().count()

        return subject_consents



    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context.update(
            flourish_consents=self.total_flourish_consents,
            flourish_assents=self.total_child_assents,
            child_consents=self.total_child_consents,
            continued_consents=self.total_continued_consents)
        return context
