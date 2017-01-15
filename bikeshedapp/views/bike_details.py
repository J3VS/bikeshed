from django.views.generic.detail import DetailView, SingleObjectMixin
from bikeshedapp.models import Bike

class BikeDetails(DetailView, SingleObjectMixin):
    template_name = "bikeshedapp/bike_detail.html"
    model = Bike
