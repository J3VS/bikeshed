from django.shortcuts import render
from bikeshedapp.forms import AddBikeForm
from bikeshedapp.models import Bike
import datetime

def post_form_upload(request):
    if request.method == 'GET':
        form = AddBikeForm()
    else:
        # A POST request: Handle Form Upload
        # Bind data from request.POST into a PostForm
        form = AddBikeForm(request.POST)
        # If data is valid, proceeds to create a new post and redirect the user
        if form.is_valid():
            print "It is valid"
            bike = form.save(commit=False)

            bike.created_by = request.user;
            bike.created_date = datetime.datetime.now()
            bike.save()
            return HttpResponseRedirect(reverse('/', kwargs={'bike_id': bike.id}))
        else:
            print "It is not valid"
            print form.errors
            print request.user

    return render(request, 'bikeshedapp/add_bike.html', {
        'form': form,
    })
