"""flourish URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import RedirectView
from edc_action_item.admin_site import edc_action_item_admin
from edc_appointment.admin_site import edc_appointment_admin
from edc_locator.admin_site import edc_locator_admin
from flourish_caregiver.admin_site import flourish_caregiver_admin
from edc_visit_schedule.admin_site import edc_visit_schedule_admin
from edc_call_manager.admin_site import edc_call_manager_admin
from edc_data_manager.admin_site import edc_data_manager_admin

from flourish_child.admin_site import flourish_child_admin
from pre_flourish.admin_site import pre_flourish_admin
from flourish_follow.admin_site import flourish_follow_admin


from .views import HomeView, AdministrationView

urlpatterns = [
    path('accounts/', include('edc_base.auth.urls')),
    path('admin/', include('edc_base.auth.urls')),

    path('admin/', admin.site.urls),
    path('admin/', edc_appointment_admin.urls),
    path('admin/', edc_data_manager_admin.urls),
    path('admin/', edc_locator_admin.urls),
    path('admin/', edc_action_item_admin.urls),
    path('admin/', flourish_caregiver_admin.urls),
    path('admin/', flourish_follow_admin.urls),
    path('admin/', pre_flourish_admin.urls),
    path('admin/edc_visit_schedule/', edc_visit_schedule_admin.urls),
    path('admin/edc_call_manager/', edc_call_manager_admin.urls),
    path('admin/', flourish_child_admin.urls),
    path('administration/', AdministrationView.as_view(),
         name='administration_url'),
    path('admin/flourish_caregiver/', RedirectView.as_view(url='admin/flourish_caregiver/'),
         name='maternal_subject_models_url'),
    path('flourish_caregiver/', include('flourish_caregiver.urls')),
    path('flourish_child/', include('flourish_child.urls')),
    path('pre_flourish/', include('pre_flourish.urls')),
    path('pre_flourish/subject/', include('pre_flourish.dashboard_urls')),
    path('flourish_follow/', include('flourish_follow.urls')),
    path('edc_action_item/', include('edc_action_item.urls')),
    path('edc_base/', include('edc_base.urls')),
    path('edc_consent/', include('edc_consent.urls')),
    path('edc_data_manager/', include('edc_data_manager.urls')),
    path('edc_call_manager/', include('edc_call_manager.urls')),
    path('edc_device/', include('edc_device.urls')),
    path('edc_protocol/', include('edc_protocol.urls')),
    path('edc_subject_dashboard/', include('edc_subject_dashboard.urls')),
    path('edc_visit_schedule/', include('edc_visit_schedule.urls')),

    path('subject/', include('flourish_dashboard.urls')),

    path('home/', HomeView.as_view(), name='home_url'),
    path('', HomeView.as_view(), name='home_url'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
