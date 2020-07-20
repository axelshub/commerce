from django.forms import ModelForm
from django import forms
from django.contrib.auth.models import User
from .models import *

class new_listing(ModelForm):
    class Meta:
        model = Listing
        exclude = ["listed_by"]
        
        
class new_bid(ModelForm):
    class Meta:
        model = Bid
        fields = ["bid"]

