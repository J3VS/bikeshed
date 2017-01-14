from django.conf.urls  import url
from bikeshedapp.views import ColorList

from django.conf.urls import patterns, include, url
from django.contrib   import admin

urlpatterns = [
    (r'^bikeshed/', include('bikeshed.urls')),
    url(r'^admin/', include(admin.site.urls)),
]
