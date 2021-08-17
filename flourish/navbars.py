from django.conf import settings
from edc_navbar import NavbarItem, site_navbars, Navbar


flourish = Navbar(name='flourish')

flourish.append_item(
    NavbarItem(
        name='maternal_dataset',
        label='Maternal Dataset',
        fa_icon='far fa-user-circle',
        url_name=settings.DASHBOARD_URL_NAMES.get('maternal_dataset_listboard_url')))

flourish.append_item(
    NavbarItem(
        name='maternal_screening',
        label='Maternal Screening',
        fa_icon='far fa-user-circle',
        url_name=settings.DASHBOARD_URL_NAMES.get('maternal_screening_listboard_url')))

flourish.append_item(
    NavbarItem(
        name='maternal_subject',
        label='Maternal Subjects',
        fa_icon='far fa-user-circle',
        url_name=settings.DASHBOARD_URL_NAMES.get('subject_listboard_url')))

flourish.append_item(
    NavbarItem(
        name='Follow Ups',
        title='Follow Ups',
        label='Follow Ups',
        fa_icon='fa-user-plus',
        url_name='flourish_follow:home_url'))

flourish.append_item(
    NavbarItem(
        name='reports',
        title='Reports',
        label='Reports',
        fa_icon='fa-user-plus',
        url_name='flourish_reports:recruitment_report_url'))

flourish.append_item(
    NavbarItem(
        name='export_data',
        label='Export Data',
        fa_icon='fa fa-database',
        url_name='flourish_export:home_url'))

site_navbars.register(flourish)
