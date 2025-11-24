from django.urls import path
from . views import(
    index,
    aboutus,
    contactus,
    events,
    chefs,
    login,
    signup,
    booking,
    services,
    gallery,
    chef_registration,
    contact_success
)

urlpatterns = [
    path('', index, name='index'),
    path('aboutus/', aboutus, name='aboutus'),
    path('contactus/', contactus, name='contactus'),
    path('events/', events, name='events'),
    path('chefs/', chefs, name='chefs'),
    path('login/', login, name='login'),
    path('signup/', signup, name='signup'),
    path('booking/', booking, name='booking'),
    path('services', services, name='services'),
    path('gallery', gallery, name='gallery'),
    path('chef_registration', chef_registration, name='chef_registration'),
    path('contact/success/', contact_success, name='contact_success'),
    
]
