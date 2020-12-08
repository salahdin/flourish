from datetime import datetime
from dateutil.tz import gettz
from django.apps import AppConfig as DjangoAppConfig

from edc_appointment.apps import AppConfig as BaseEdcAppointmentAppConfig
from edc_appointment.appointment_config import AppointmentConfig
from edc_appointment.constants import COMPLETE_APPT
from edc_base.apps import AppConfig as BaseEdcBaseAppConfig
from edc_data_manager.apps import AppConfig as BaseEdcDataManagerAppConfig
from edc_locator.apps import AppConfig as BaseEdcLocatorAppConfig
from edc_protocol.apps import AppConfig as BaseEdcProtocolAppConfig
from edc_timepoint.apps import AppConfig as BaseEdcTimepointAppConfig
from edc_timepoint.timepoint import Timepoint
from edc_timepoint.timepoint_collection import TimepointCollection
from edc_visit_tracking.apps import AppConfig as BaseEdcVisitTrackingAppConfig
from flourish_dashboard.patterns import subject_identifier


class AppConfig(DjangoAppConfig):
    name = 'flourish'


class EdcAppointmentAppConfig(BaseEdcAppointmentAppConfig):
    configurations = [
        AppointmentConfig(
            model='edc_appointment.appointment',
            related_visit_model='flourish_caregiver.maternalvisit',
            appt_type='clinic')]


class EdcBaseAppConfig(BaseEdcBaseAppConfig):
    project_name = 'Flourish'
    institution = 'Botswana-Harvard AIDS Institute'


class EdcDataManagerAppConfig(BaseEdcDataManagerAppConfig):
    identifier_pattern = subject_identifier
    extra_assignee_choices = {}


class EdcProtocolAppConfig(BaseEdcProtocolAppConfig):
    protocol = 'BHP035'
    protocol_name = 'Flourish'
    protocol_number = '035'
    protocol_title = ''
    study_open_datetime = datetime(
        2020, 9, 16, 0, 0, 0, tzinfo=gettz('UTC'))
    study_close_datetime = datetime(
        2023, 12, 31, 23, 59, 59, tzinfo=gettz('UTC'))


class EdcTimepointAppConfig(BaseEdcTimepointAppConfig):
    timepoints = TimepointCollection(
        timepoints=[
            Timepoint(
                model='edc_appointment.appointment',
                datetime_field='appt_datetime',
                status_field='appt_status',
                closed_status=COMPLETE_APPT),
            Timepoint(
                model='edc_appointment.historicalappointment',
                datetime_field='appt_datetime',
                status_field='appt_status',
                closed_status=COMPLETE_APPT),
        ])


class EdcLocatorAppConfig(BaseEdcLocatorAppConfig):
    name = 'edc_locator'
    reference_model = 'flourish_caregiver.maternallocator'


class EdcVisitTrackingAppConfig(BaseEdcVisitTrackingAppConfig):
    visit_models = {
        'flourish_caregiver': (
            'maternal_visit', 'flourish_caregiver.maternalvisit'),
        'flourish_child': (
            'child_visit', 'flourish_child.childvisit'),
        'pre_flourish': (
            'maternal_visit', 'pre_flourish.preflourishcaregivervisit'), }
