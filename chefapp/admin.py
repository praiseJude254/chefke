from django.contrib import admin
from .models import Chef, Testimonial, ChefCategory
from .models import ContactMessage

# Register your models here.
@admin.register(Chef)
class ChefAdmin(admin.ModelAdmin):
    list_display = ('name', 'specialty', 'is_elite', 'price', 'rating', 'reviews_count')
    list_filter = ('is_elite', 'specialty')
    search_fields = ('name', 'specialty')

@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ('client_name', 'rating', 'created_at')
    list_filter = ('rating', 'created_at')
    search_fields = ('client_name', 'testimonial_text')    


@admin.register(ChefCategory)
class ChefCategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'slug')
    prepopulated_fields = {'slug': ('title',)}     



@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'created_at')
    list_filter = ('subject', 'created_at')
    search_fields = ('name', 'email', 'subject', 'message')
    readonly_fields = ('created_at',)
