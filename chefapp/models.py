from django.db import models

# Create your models here.

class Chef(models.Model):
    name = models.CharField(max_length=255)
    specialty = models.CharField(max_length=255)
    profile_image = models.ImageField(upload_to='chefs/')
    verified = models.BooleanField(default=True)
    rating = models.FloatField(default=4.0)
    reviews_count = models.PositiveIntegerField(default=0)
    price = models.CharField(max_length=50)  # e.g., "KES 5,500/hr"
    is_elite = models.BooleanField(default=False)  # top picks

    def star_rating(self):
        """Return ★ characters based on rating"""
        full_stars = int(self.rating)
        half_star = self.rating - full_stars >= 0.5
        stars = '★' * full_stars
        if half_star:
            stars += '☆'
        return stars

    def __str__(self):
        return self.name

class ChefCategory(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    icon = models.ImageField(upload_to='icons/')  
    slug = models.SlugField(unique=True, blank=True, null=True)  

    def __str__(self):
        return self.title



class Testimonial(models.Model):
    client_name = models.CharField(max_length=100)
    client_photo = models.ImageField(upload_to='testimonials/')
    testimonial_text = models.TextField()
    rating = models.PositiveSmallIntegerField(default=5)  # 1-5 stars
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']  

    def __str__(self):
        return f"{self.client_name} ({self.rating}★)"

class ContactMessage(models.Model):
    SUBJECT_CHOICES = [
        ('General', 'General'),
        ('Booking', 'Booking'),
        ('Partnership', 'Partnership'),
        ('Support', 'Support'),
    ]

    name = models.CharField(max_length=255)
    email = models.EmailField()
    subject = models.CharField(max_length=50, choices=SUBJECT_CHOICES)
    message = models.TextField()
    attachment = models.FileField(upload_to='contact_attachments/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} ({self.subject})"
