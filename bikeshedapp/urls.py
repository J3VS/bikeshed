from django.conf.urls  import url

from django.conf.urls import include, url
from django.contrib   import admin

urlpatterns = [
    (r'^/', include('bikeshed.urls')),
    url(r'^admin/', include(admin.site.urls)),
]
