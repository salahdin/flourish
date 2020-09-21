from django.conf import settings
from edc_navbar import NavbarItem, site_navbars, Navbar


flourish = Navbar(name='flourish')

flourish.append_item(
    NavbarItem(
        name='maternal_screening',
        label='Maternal Screening',
        fa_icon='far fa-user-circle',
        url_name=settings.DASHBOARD_URL_NAMES.get('maternal_screening_listboard_url')))

flourish.append_item(
    NavbarItem(
        name='maternal_locator',
        label='Maternal Locator',
        fa_icon='far fa-user-circle',
        url_name=settings.DASHBOARD_URL_NAMES.get('maternal_locator_listboard_url')))

flourish.append_item(
    NavbarItem(
        name='maternal_subject',
        label='Maternal Subjects',
        fa_icon='far fa-user-circle',
        url_name=settings.DASHBOARD_URL_NAMES.get('subject_listboard_url')))


site_navbars.register(flourish)
