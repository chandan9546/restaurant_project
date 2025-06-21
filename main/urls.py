from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('menu/', views.menu, name='menu'),
    path('reservation/', views.reservation_view, name='reservation'),
    path('thank-you/', views.thank_you, name='thank_you'),
    path('review/', views.customer_reviews, name='review'),
    path('contact/', views.contact, name='contact'),
    path('services/', views.services, name='services'),

]
