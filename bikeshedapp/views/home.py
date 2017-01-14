from django.shortcuts     import redirect
from django.views.generic import ListView
from bikeshedapp.models   import Bike

class BikeList(ListView):

    model = Bike;

    def dispatch(self, request, *args, **kwargs):
        self.request = request     #So get_context_data can access it.
        return super(BikeList, self).dispatch(request, *args, **kwargs)

    def get_queryset(self):
        """
        Returns the all colors, for display in the main table. The search
        result query set, if any, is passed as context.
        """
        return  super(BikeList, self).get_queryset()

    def get_context_data(self, **kwargs):
        #The current context.
        context = super(BikeList, self).get_context_data(**kwargs)
