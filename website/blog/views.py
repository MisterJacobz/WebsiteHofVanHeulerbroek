from django.shortcuts import render
from django.http import HttpResponse
from .models import ConferenceRoom, MenuItems, Reservation

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
        'reservations': Reservation.objects.all()
    }
    return render(request, 'blog/vergaderruimte.html', context)

def over_ons(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/over_ons.html', context)

def route(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/route.html', context)

def contact(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/contact.html', context)