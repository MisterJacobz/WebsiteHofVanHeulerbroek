from django import forms
from . models import ConferenceRoomReservation

class ConferenceRoomReservationForm(forms.ModelForm):
    class Meta:
        model = ConferenceRoomReservation
        fields = ['group_name']