from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'chefapp/index.html')

def aboutus(request):
    return render(request, 'chefapp/aboutus.html')

def contactus(request):
    return render(request, 'chefapp/contactus.html')

def media(request):
    return render(request, 'chefapp/media.html')

def chefs(request):
    return render (request, 'chefapp/chefs.html')

def login(request):
    return render (request, 'chefapp/login.html')

def signup(request):
    return render (request, 'chefapp/signup.html')

def booking(request):
    return render(request, 'chefapp/booking.html')

def services(request):
    return render(request, 'chefapp/services.html')

def gallery(request):
    return render(request, 'chefapp/gallery.html')

