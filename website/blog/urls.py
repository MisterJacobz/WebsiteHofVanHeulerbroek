from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('vergaderruimte/info', views.vergaderruimte_info, name='vergaderruimte-info'),
    path('vergaderruimte/fotos', views.vergaderruimte_fotos, name='vergaderruimte-fotos'),
    path('vergaderruimte/prijzen', views.vergaderruimte_prijzen, name='vergaderruimte-prijzen'),
    path('contact', views.contact, name='contact'),
    path('over-ons', views.over_ons, name='over-ons'),
    path('route', views.route, name='route'),
]
