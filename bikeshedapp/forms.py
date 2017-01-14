from django.forms import ModelForm, CharField, Textarea
from bikeshedapp.models import Bike

class AddBikeForm(ModelForm):
    description = CharField(widget=Textarea)

    class Meta:
        model = Bike
        exclude = ['created_by', 'created_date', 'image']

    def __init__(self, *args, **kwargs):
        super(AddBikeForm, self).__init__(*args, **kwargs)
        self.fields['brand'].empty_label = "Select Brand"
        self.fields['brand'].widget.choices = self.fields['brand'].choices
        self.fields['type'].empty_label = "Select Type"
        self.fields['type'].widget.choices = self.fields['type'].choices
