from faulthandler import disable
from django import forms
from .models import SMOKER, candidate
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

    # First Name
    first_name = forms.CharField(
        min_length=3, max_length=30,
        validators=[RegexValidator(r'^[a-zA-ZÀ-ÿ\s]*$', 
        message='Only letters is allowed!')], 
        widget=forms.TextInput(attrs={
            'placeholder': 'First Name',
            'style': 'font-size: 13px; text-transform: capitalize'
            }))

    # Last Name
    last_name = forms.CharField(
        min_length=3, max_length=30,
        validators=[RegexValidator(r'^[a-zA-ZÀ-ÿ\s]*$', 
        message='Only letters is allowed!')], 
        widget=forms.TextInput(attrs={
            'placeholder': 'Last Name',
            'style': 'font-size: 13px; text-transform: capitalize'
            }))
    

    # Job (Uppercase function)
    job = UpperCase(
        label='Job code',
        min_length=5, max_length=5, 
        widget=forms.TextInput(attrs={
            'placeholder': 'Example: FR-22',
            'style': 'font-size: 13px; text-transform: uppercase'
            }))


    # Email (LOWERCASE Function)
    email = LowerCase(
        min_length=8, max_length=50,
        validators=[RegexValidator(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$', 
        message='Put a valid email address!')], 
        widget=forms.TextInput(attrs={
            'placeholder': 'Email',
            'style': 'font-size: 13px; text-transform: lowercase'
            }))

    # Age
    age = forms.CharField(
        min_length=2, max_length=3,
        validators=[RegexValidator(r'^[0-9]*$', 
        message='Only number is allowed!')], 
        widget=forms.TextInput(attrs={
            'placeholder': 'Age',
            'style': 'font-size: 13px',
            }))

    # Experience 
    experience = forms.BooleanField(label='I have exprience', required=False)

    # Message
    message = forms.CharField(
        required=False,
        min_length=10, max_length=1000,
        widget=forms.Textarea(attrs={
            'placeholder': 'Message', 'rows':3,
            'style': 'font-size: 13px',
            }
        ),
    )

    # FIle (upload)
    file = forms.FileField(
        required=False,
        widget=forms.ClearableFileInput(
            attrs={
                'style':'font-size: 13px'
            }
        )

    )
    
    
    # #GENDER
    # GENDER =[('M', 'Male'), ('F', 'Female')]
    # gender = forms.CharField(label='Gender', widget=forms.RadioSelect(choices=GENDER))


    class Meta:
        model = candidate
        exclude = ['Situation', 'created_at']
        
        
        SALARY = (
            ('','Salary expectation (month)'),
            ('Between ($3000 and $4000)','Between ($3000 and $4000)'),
            ('Between ($4000 and $5000)','Between ($3000 and $4000)'),
            ('Between ($5000 and $7000)','Between ($5000 and $7000)'),
            ('Between ($7000 and $10000)','Between ($7000 and $10000)'),
        )
        

        GENDER =[('M', 'Male'), ('F', 'Female')]
       
        #OUTSIDE Widget
        widgets = {
            'phone': forms.TextInput(
                attrs={
                    'style':'font-size: 18px',
                    'placeholder':'Phone',
                    'data-mask': '(000) 000-0000'
                }
            ),

            #SALARY
            'salary': forms.Select(
                choices=SALARY,
                attrs={
                    'class':'form-control',
                    'style': 'font-size: 13px',
                }
            ),

            'gender': forms.RadioSelect(choices=GENDER, attrs={'class': 'btn-check'}),
            'smoker': forms.RadioSelect(choices=SMOKER, attrs={'class': 'btn-check'}),
            'personality': forms.Select(attrs={'style': 'font-size: 13px'}),
        }

    #SUPER FUNCTION
    def __init__(self, *args, **kwargs):
        super(CandidateForm, self).__init__(*args, **kwargs)

        # CONTROL PANEL (Optional method to control)
        # self.fields['experience'].disabled = False
        # self.fields['email'].widget.attrs.update({'readonly': 'readonly'})

        # SELECT OPTIONS
       # self.fields['personality'].choices = [('', 'Select a personality'),] + list(self.fields["personality"].choices)[1:]
        
        # WIDGET CONTROL
        #Readonly
        # readonly = ['first_name', 'last_name', 'job']
        # for field in readonly:
        #     self.fields[field].widget.attrs['readonly'] = False
            
        # # Disable
        # disabled = ['first_name', 'last_name', 'job']
        # for field in disabled:
        #     self.fields[field].widget.attrs['disabled'] = False