from django.urls import path
from . views import(
    index,
    aboutus,
    contactus,
    media,
    chefs,
)

urlpatterns = [
    path('', index, name='index'),
    path('aboutus/', aboutus, name='aboutus'),
    path('contactus/', contactus, name='contactus'),
    path('media/', media, name='media'),
    path('chefs/', chefs, name='chefs'),
]
