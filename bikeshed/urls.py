from django.conf.urls import include, url
from django.contrib   import admin
from bikeshedapp.views import BikeList, post_form_upload

urlpatterns = [
    url(r"^$", BikeList.as_view(), name="bike_list"),
    url(r"add_bike$", post_form_upload, name="add_bike"),
]
