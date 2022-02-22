import imp
from django.apps import apps as django_apps
from django.views.generic import TemplateView
from edc_base.view_mixins import EdcBaseViewMixin
from edc_navbar import NavbarViewMixin
from flourish_caregiver.models import *
from flourish_caregiver.models import *
from flourish_prn.models import *
from django.db.models import Q


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
        Caregivers from previous BHP studies Currently on-Study
        """
        metadataset_screening_identifier = MaternalDataset.objects.values_list('screening_identifier',
                                                                               flat=True).distinct()
        caregiver_offstudy_subject_identifier = CaregiverOffStudy.objects.values_list('subject_identifier', flat=True)

        subject_consents = SubjectConsent.objects.filter(
            Q(screening_identifier__in=metadataset_screening_identifier) & ~Q(
                subject_identifier__in=caregiver_offstudy_subject_identifier)).values_list(
            'subject_identifier').distinct().count()
        return subject_consents

    @property
    def total_child_prev(self):
        """
        Children from previous BHP studies Currently on-Study
        """

        child_offstudy_subject_identifiers = ChildOffStudy.objects.values_list('subject_identifier', flat=True)

        # children from previous study

        total_children = CaregiverChildConsent.objects.filter(Q(study_child_identifier__isnull=False) & ~Q(
            subject_identifier__in=child_offstudy_subject_identifiers)).count()
        return total_children

    @property
    def total_all_preg_women(self):
        """
        All women who consented when pregnant (on and off study)
        """
        return AntenatalEnrollment.objects.count()

    @property
    def total_consented_pregnant_women(self):
        """
        All women who consented when pregnant – Currently ON- study
        """

        maternal_offstudy_subject_identifiers = CaregiverOffStudy.objects.values_list('subject_identifier',
                                                                                      flat=True).distinct()
        all_consented_women = AntenatalEnrollment.objects.exclude(
            subject_identifier__in=maternal_offstudy_subject_identifiers).count()
        return all_consented_women

    @property
    def total_currently_pregnant_women(self):
        """
        Currently Pregnant Women On-Study
        """

        maternal_offstudy_subject_identifiers = CaregiverOffStudy.objects.values_list('subject_identifier',
                                                                                      flat=True).distinct()

        maternal_delivery_subject_identifiers = MaternalDelivery.objects.values_list('subject_identifier',
                                                                                     flat=True).distinct()

        currently_preg = AntenatalEnrollment.objects.exclude(
            Q(subject_identifier__in=maternal_offstudy_subject_identifiers) |
            Q(subject_identifier__in=maternal_delivery_subject_identifiers)).count()

        return currently_preg

    @property
    def total_maternal_delivery(self):
        """
        Newly recruited (not from previous BHP studies) women enrolled in pregnancy who gave birth who are currently On-Study
        """

        return MaternalDelivery.objects.count()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context.update(
            flourish_consents=self.total_flourish_consents,
            flourish_assents=self.total_child_assents,
            child_consents=self.total_child_consents,
            continued_consents=self.total_continued_consents,
            total_caregiver_prev_study=self.total_caregiver_prev_study,
            total_child_prev=self.total_child_prev,
            total_all_preg_women=self.total_all_preg_women,
            total_consented_pregnant_women=self.total_consented_pregnant_women,
            total_currently_pregnant_women=self.total_currently_pregnant_women,
            total_maternal_delivery=self.total_maternal_delivery
        )
        return context
