"""youngun URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include, re_path

from rest_framework import permissions
#from drf_yasg.views import get_schema_view
#from drf_yasg import openapi

from django.conf.urls.static import static
from django.conf import settings

from django_otp.admin import OTPAdminSite


admin.site.__class__ = OTPAdminSite

#schema_view = get_schema_view(
#    openapi.Info(
#        title="Snippets API",
#        default_version='v1',
#        description="Test description",
#        terms_of_service="https://www.google.com/policies/terms/",
#        contact=openapi.Contact(email="contact@snippets.local"),
#        license=openapi.License(name="BSD License"),
#    ),
#    public=True,
#    permission_classes=(permissions.AllowAny,),
#)

urlpatterns = [
#   re_path(r'^swagger(?P<format>\.json|\.yaml)$',
#           schema_view.without_ui(cache_timeout=0), name='schema-json'),
#    re_path(r'^swagger/$', schema_view.with_ui('swagger',
#                                               cache_timeout=0), name='schema-swagger-ui'),
#    re_path(r'^redoc/$', schema_view.with_ui('redoc',
#                                             cache_timeout=0), name='schema-redoc'),

    path('campmanager/', admin.site.urls),
    path("api/", include('youngun.apps.campaigns.urls', namespace="campaigns")),
    path("api/", include('youngun.apps.authentication.urls', namespace="users")),
    path("api/", include('youngun.apps.content.urls', namespace="content")),
    path("api/", include('youngun.apps.usermanager.urls', namespace="profile")),
    path('', include('drfpasswordless.urls')),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

admin.site.site_header = "Youngun Campaign Tracker Admin"
admin.site.site_url = "https://youngun.in"
admin.site.site_title = "Youngun Campaign Tracker Admin"
