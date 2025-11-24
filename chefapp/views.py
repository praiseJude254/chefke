from django.shortcuts import render, redirect
from .models import Chef, Testimonial, ChefCategory
import random
from .models import ContactMessage
from django.urls import reverse
# Create your views here.
def index(request):
    # Get 6 random elite chefs
    elite_chefs = Chef.objects.filter(is_elite=True).order_by('?')[:6]
    
    # Get all other non-elite chefs
    all_other_chefs = Chef.objects.filter(is_elite=False)

    testimonials_qs = list(Testimonial.objects.all())
    random.shuffle(testimonials_qs)  
    testimonials = testimonials_qs[:6] 

    # Pre-generate star strings
    for t in testimonials:
        t.stars = '★' * t.rating + '☆' * (5 - t.rating)

    context = {
        'elite_chefs': elite_chefs,
        'all_other_chefs': all_other_chefs,
        'testimonials': testimonials,
    }
    return render(request, 'chefapp/index.html', context)

def contact_success(request):
    name = request.GET.get('name', 'Guest') 
    return render(request, 'chefapp/contact_success.html', {'name': name})


def aboutus(request):
    return render(request, 'chefapp/aboutus.html')



def contactus(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        attachment = request.FILES.get('attachment')

        saved_message = ContactMessage.objects.create(
            name=name,
            email=email,
            subject=subject,
            message=message,
            attachment=attachment
        )

        # Redirect to success page
        return redirect(reverse('contact_success') + f'?name={name}')

    return render(request, 'chefapp/contactus.html')


def events(request):
    return render(request, 'chefapp/events.html')

def chefs(request):
    # Get 6 random elite chefs
    elite_chefs = Chef.objects.filter(is_elite=True).order_by('?')[:6]
    
    # Get all other non-elite chefs
    all_other_chefs = Chef.objects.filter(is_elite=False)

    # Get all chef categories
    categories = ChefCategory.objects.all()

    context = {
        'elite_chefs': elite_chefs,
        'all_other_chefs': all_other_chefs,
        'categories': categories, 
    }
    return render(request, 'chefapp/chefs.html', context)


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

def chef_registration(request):
    return render(request, 'chefapp/chef_registration.html')

