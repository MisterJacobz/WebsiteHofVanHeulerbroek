from django.urls import path
from django.views.generic import RedirectView
from . import views

urlpatterns = [
    path('', views.home, name='root'),
    # path('vergaderruimte/info', views.vergaderruimte_info, name='vergaderruimte-info'),
    # path('vergaderruimte/fotos', views.vergaderruimte_fotos, name='vergaderruimte-fotos'),
    # path('vergaderruimte/tariven', views.vergaderruimte_tariven, name='vergaderruimte-tariven'),
    path('vergaderruimte', views.vergaderruimte, name='vergaderruimte'),
    path('bed_and_breakfast', views.bed_and_breakfast, name='bed_and_breakfast'),
    path('contact', views.contact, name='contact'),
    path('over-ons', views.over_ons, name='over-ons'),
    path('omgeving', views.omgeving, name='omgeving'),
]
