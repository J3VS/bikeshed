from django.conf.urls import include, url
from django.contrib   import admin
from bikeshedapp.views import ColorList, BikeList, toggle_color_like, post_form_upload

urlpatterns = [
    url(r"color_list$", ColorList.as_view(), name="color_list"),
    url(r"^$", BikeList.as_view(), name="bike_list"),
    url(r"add_bike$", post_form_upload, name="add_bike"),

    url(r"^like_color_(?P<color_id>\d+)/$", toggle_color_like, name="toggle_color_like"),
]
