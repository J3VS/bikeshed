from django.shortcuts import render
from bikeshedapp.forms import AddBikeForm
from bikeshedapp.models import Bike
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.core.exceptions import ObjectDoesNotExist
import datetime

def post_form_upload(request):
    if request.method == 'GET':
        form = AddBikeForm()
    else:
        form = AddBikeForm(request.POST, request.FILES)
        if form.is_valid():
            bike = form.save(commit=False)

            try:
                user = User.objects.get(username="test_user")
            except ObjectDoesNotExist:
                user = User.objects.create_user('test_user')
                user.save()

            bike.created_by = user
            bike.created_date = datetime.datetime.now()
            bike.save()
            return HttpResponseRedirect("/")
        else:
            print form.errors
            print request.user

    return render(request, 'bikeshedapp/add_bike.html', {
        'form': form,
    })
