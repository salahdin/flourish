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
from edc_appointment.admin_site import edc_appointment_admin
from flourish_maternal.admin_site import flourish_maternal_admin
from flourish_infant.admin_site import flourish_infant_admin


from .views import HomeView, AdministrationView

urlpatterns = [
    path('accounts/', include('edc_base.auth.urls')),
    path('admin/', include('edc_base.auth.urls')),

    path('admin/', admin.site.urls),
    path('admin/', edc_appointment_admin.urls),
    path('admin/', flourish_maternal_admin.urls),
    path('admin/', flourish_infant_admin.urls),
    path('administration/', AdministrationView.as_view(),
         name='administration_url'),
    path('admin/flourish_maternal/', RedirectView.as_view(url='admin/flourish_maternal/'),
         name='maternal_subject_models_url'),
    path('flourish_maternal/', include('flourish_maternal.urls')),
     path('flourish_infant/', include('flourish_infant.urls')),
    path('maternal_subject/', include('flourish_dashboard.urls')),
    path('edc_base/', include('edc_base.urls')),
    path('edc_data_manager/', include('edc_data_manager.urls')),
    path('edc_device/', include('edc_device.urls')),
    path('edc_protocol/', include('edc_protocol.urls')),
    path('edc_subject_dashboard/', include('edc_subject_dashboard.urls')),

    path('home/', HomeView.as_view(), name='home_url'),
    path('', HomeView.as_view(), name='home_url'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
