import imp
from django.apps import apps as django_apps
from django.views.generic import TemplateView
from edc_base.view_mixins import EdcBaseViewMixin
from edc_navbar import NavbarViewMixin
from flourish_caregiver.models import *
from flourish_caregiver.models import *
from flourish_prn.models import *

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

    @property
    def total_preg_onstudy(self):
        """
        Pregnant Women Onstudy
        """
        caregiver_offstudy_pids = CaregiverOffStudy.objects.values_list(
            'subject_identifier')
        pregnent_women_onstudy = AntenatalEnrollment.objects.exclude(
            subject_identifier__in=caregiver_offstudy_pids).values_list('subject_identifier').count()

        return pregnent_women_onstudy

    @property
    def total_preg_offstudy(self):
        """
        Pregnant Women Offstudy
        """

        pregnant_women_pids = AntenatalEnrollment.objects.values_list(
            'subject_identifier').distinct()

        pregnent_women_offstudy = CaregiverOffStudy.objects.filter(
            subject_identifier__in=pregnant_women_pids).values_list('subject_identifier').distinct().count()

        return pregnent_women_offstudy

    @property    
    def total_maternal_delivery(self):
        """
        Women who gave birth while on study 
        """


        pregnant_women_pids = AntenatalEnrollment.objects.values_list(
            'subject_identifier').distinct()

        maternal_deliveries = MaternalDelivery.objects.filter(subject_identifier__in=pregnant_women_pids).values_list(
            'subject_identifier').values_list('subject_identifier').distinct().count()

        return maternal_deliveries






    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context.update(
            flourish_consents=self.total_flourish_consents,
            flourish_assents=self.total_child_assents,
            child_consents=self.total_child_consents,
            continued_consents=self.total_continued_consents)
        return context
