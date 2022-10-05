
from django import forms
from .models import candidate
from django.core.validators import RegexValidator


# Functions to convert every letter to Lowercase
class LowerCase(forms.CharField):
    def to_python(self, value):
        return value.lower()


# Functions to convert every letter to UpperCase
class UpperCase(forms.CharField):
    def to_python(self, value):
        return value.upper()


class CandidateForm(forms.ModelForm):

    # VALIDATIONS
    first_name = forms.CharField(
        min_length=3, max_length=30,
        validators=[RegexValidator(r'^[a-zA-ZÀ-ÿ\s]*$', 
        message='Only letters is allowed!')], 
        widget=forms.TextInput(attrs={'placeholder': 'First Name'}))

    last_name = forms.CharField(
        min_length=3, max_length=30,
        validators=[RegexValidator(r'^[a-zA-ZÀ-ÿ\s]*$', 
        message='Only letters is allowed!')], 
        widget=forms.TextInput(attrs={'placeholder': 'Last Name'}))
    

    # Job always in UPPERCASE
    job = UpperCase(
        label='Job code',
        min_length=5, max_length=5, 
        widget=forms.TextInput(attrs={'placeholder': 'Example: FR-22'}))

    # Job always in LOWERCASE
    email = LowerCase(
        min_length=8, max_length=50,
        validators=[RegexValidator(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$', 
        message='Put a valid email address!')], 
        widget=forms.TextInput(attrs={'placeholder': 'Email'}))

    
    age = forms.CharField(
        min_length=2, max_length=3,
        validators=[RegexValidator(r'^[0-9]*$', 
        message='Only number is allowed!')], 
        widget=forms.TextInput(attrs={'placeholder': 'Age'}))


    message = forms.CharField(
        required=False,
        min_length=10, max_length=1000,
        widget=forms.Textarea(attrs={'placeholder': 'Message', 'rows':5}
        ),
    )


    class Meta:
        model = candidate
        exclude = ['Situation', 'created_at']
        
        
        #OUTSIDE Widget
        Widgets = {
            'phone': forms.TextInput(
                attrs={
                    'style':'font-size: 18px',
                    'placeholder':'Phone',
                    'data-mask': '(000) 000-0000'
                }
            )
        }