from django import forms
from .models import Reservation, Contact,Review

class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ['name',  'phone', 'date', 'time', 'guests']

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'message']


# forms.py
class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['name', 'review', 'rating']  
        widgets = {
            'rating': forms.NumberInput(attrs={
                'min': 1,
                'max': 5,
                'placeholder': 'Enter rating (1-5)'
            })
        }

    def clean_rating(self):
        rating = self.cleaned_data['rating']
        if rating < 1 or rating > 5:
            raise forms.ValidationError("Rating must be between 1 and 5.")
        return rating 
