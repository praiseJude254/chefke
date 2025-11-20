from django.urls import path
from . views import(
    index,
    aboutus,
    contactus,
    media,
    chefs,
    login,
    signup,
    booking,
    services,
    gallery
)

urlpatterns = [
    path('', index, name='index'),
    path('aboutus/', aboutus, name='aboutus'),
    path('contactus/', contactus, name='contactus'),
    path('media/', media, name='media'),
    path('chefs/', chefs, name='chefs'),
    path('login/', login, name='login'),
    path('signup/', signup, name='signup'),
    path('booking/', booking, name='booking'),
    path('services', services, name='services'),
    path('gallery', gallery, name='gallery')
    
]
