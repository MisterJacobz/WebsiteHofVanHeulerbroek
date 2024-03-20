from django import forms
from . models import ConferenceRoomReservation

class ConferenceRoomReservationForm(forms.ModelForm):
    class Meta:
        model = ConferenceRoomReservation
        fields = [
            'group_name',
            'group_size',
            'name',
            'email',
            'phone_number',
            'address',
            'zipcode',
            'city',
            'reservation_datetime_start',
            'reservation_datetime_finish',
        ]