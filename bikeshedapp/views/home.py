from django.views.generic      import ListView
from django.views.generic.list import MultipleObjectMixin
from bikeshedapp.models        import Bike

class BikeList(ListView, MultipleObjectMixin):
    template_name = "bikeshedapp/bike_list.html"
    model = Bike
    paginate_by = 50
