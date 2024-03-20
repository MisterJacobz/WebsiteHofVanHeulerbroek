from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import ConferenceRoom, MenuItems, MenuItemsExtraInfo, ConferenceRoomReservation
from .forms import ConferenceRoomReservationForm
from django.core.mail import send_mail
from decouple import config
from django.template.loader import render_to_string

conference_room_reservation_request1 = """
Beste __name,

Uw aanvraag voor het reserveren van de vergaderruimte is in goede orde ontvangen. U zult binnenkort iets van ons te horen krijgen voor verder overleg.
Hieronder de opgegeven gegevens:
Groepsnaam: __group_name
Aantal personen: __group_size
Telefoonnummer: __phone_number
Adres: __address
Postcode: __zipcode
Plaats: __city
Aanvang: __reservation_datetime_start
Einde: __reservation_datetime_finish
"""

conference_room_reservation_request2 = """
Aanvraag binnen van __name:
Groepsnaam: __group_name
email: __email
Aantal personen: __group_size
Telefoonnummer: __phone_number
Adres: __address
Postcode: __zipcode
Plaats: __city
Aanvang: __reservation_datetime_start
Einde: __reservation_datetime_finish
"""

# Create your views here.
def home(request):
    return render(request, 'blog/home.html')

def vergaderruimte(request):
    if request.method == "POST":
        form = ConferenceRoomReservationForm(request.POST)
        values = request.POST.dict()
        if form.is_valid():
            email_html1 = conference_room_reservation_request1
            email_html2 = conference_room_reservation_request2
            for key, val in values.items():
                email_html1 = email_html1.replace('__'+key, val)
                email_html2 = email_html2.replace('__'+key, val)
            send_mail(
                "Aanvraag voor reservering vergaderruimte",
                email_html1,
                config('EMAIL_HOST_USER'),
                [values.get('email')]
            )
            send_mail(
                "Aanvraag voor reservering vergaderruimte",
                email_html2,
                config('EMAIL_HOST_USER'),
                [config('EMAIL_HOST_USER')]
            )
            form.save()
            return redirect("home")

    else:
        form = ConferenceRoomReservationForm()
    context = {
        'conference_room': ConferenceRoom.objects.all(),
        'menu_items': MenuItems.objects.all(),
        'menu_items_extra_info': MenuItemsExtraInfo.objects.all(),
        'reservations': ConferenceRoomReservation.objects.all(), #filter(reservation_type='c'),
        'form': form,
    }
    return render(request, 'blog/vergaderruimte.html', context)

def bed_and_breakfast(request):
    context = {
        'reservations': ConferenceRoomReservation.objects.all(), #filter(reservation_type='b')
    }
    return render(request, 'blog/bed_and_breakfast.html', context)

def over_ons(request):
    return render(request, 'blog/over_ons.html')

def omgeving(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/omgeving.html', context)

def contact(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/contact.html', context)