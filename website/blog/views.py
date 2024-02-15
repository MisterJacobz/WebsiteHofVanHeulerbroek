from django.shortcuts import render
from django.http import HttpResponse
from .models import ConferenceRoom, MenuItems, MenuItemsExtraInfo, Reservation

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
    context = {
        'conference_room': ConferenceRoom.objects.all(),
        'menu_items': MenuItems.objects.all(),
        'menu_items_extra_info': MenuItemsExtraInfo.objects.all(),
        'reservations': Reservation.objects.filter(reservation_type='c')
    }
    return render(request, 'blog/vergaderruimte.html', context)

def bed_and_breakfast(request):
    context = {
        'reservations': Reservation.objects.filter(reservation_type='b')
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