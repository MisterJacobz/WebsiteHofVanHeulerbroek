from django.shortcuts import render
from django.http import HttpResponse

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

def training_home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/training_home.html', context)