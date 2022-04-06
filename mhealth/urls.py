from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='mhealth-home'),
    path('contact/', views.contact, name="mhealth-contact"),
    path('appointment/', views.appointment, name='mhealth-appointment'),
    path('pharmacy/', views.pharmacy, name='mhealth-pharmacy'),
    path('testkit/', views.testkit, name='mhealth-testkit'),
]