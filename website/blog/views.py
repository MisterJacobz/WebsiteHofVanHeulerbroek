from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import ConferenceRoom, MenuItems, MenuItemsExtraInfo, ConferenceRoomReservation
from .forms import ConferenceRoomReservationForm
from django.core.mail import send_mail
from decouple import config

posts = [
    {'author': 'Henk 1',
    'title': 'Post 1',
    'content': 'Some random text',
    'date_posted': '11 Oktober'
    },
    {'author': 'Henk 2',
    'title': 'Post 2',
    'content': 'Some random text',
    'date_posted': '11 Oktober'
    }
]

# Create your views here.
def home(request):
    return render(request, 'blog/home.html')

def vergaderruimte(request):
    if request.method == "POST":
        form = ConferenceRoomReservationForm(request.POST)
        if form.is_valid():
            print("form = ", form)
            print("Thing = ", config('EMAIL_HOST_USER'))
            message = "Test"
            send_mail(
                "Aanvraag voor reservering vergaderruimte",
                message,
                config('EMAIL_HOST_USER'),
                ["harjacobz@gmail.com"]
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