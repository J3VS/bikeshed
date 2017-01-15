from django.conf.urls import include, url
from django.contrib   import admin
from bikeshedapp.views import BikeList, post_form_upload, BikeDetails

urlpatterns = [
    url(r'^$', BikeList.as_view(), name="bike_list"),
    url(r'^add_bike$', post_form_upload, name="add_bike"),
    url(r'^bike_details/(?P<pk>\d+)$', BikeDetails.as_view(), name="bike_details"),
]
