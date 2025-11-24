from django import forms
from .models import ContactMessage

class ContactMessageForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'subject', 'message', 'attachment']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Your Name', 'required': True}),
            'email': forms.EmailInput(attrs={'placeholder': 'Your Email', 'required': True}),
            'subject': forms.Select(attrs={'required': True}),
            'message': forms.Textarea(attrs={'placeholder': 'Your Message', 'rows': 5, 'required': True}),
            'attachment': forms.ClearableFileInput(),
        }
