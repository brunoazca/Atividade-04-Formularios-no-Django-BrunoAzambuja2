from django import forms
from .models import Sports, Activities

class SportsForm(forms.ModelForm):
    class Meta:
        model = Sports
        fields = ["title","num_of_players","creation_date","like_rank"]
      
class ActivitiesForm(forms.ModelForm):
    class Meta:
        model = Activities
        fields = ["title","effort","frequency","like_rank"]
