from django import forms
from store.models import Order
from django_countries.fields import CountryField
from django_countries.widgets import CountrySelectWidget
from django.contrib.auth.models import User

class CheckoutUserForm(forms.Form):
    STATE = (('state',('State')),('telangana', 'Telangana'), ('andhra pradesh', 'Andhra Pradesh'))
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control mb-2','placeholder':'First name'}),label="")
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control mb-2','placeholder':'Last name'}),label="")
    email = forms.CharField(widget=forms.EmailInput(attrs={'class':'form-control mb-2','placeholder':'Email'}),label="")
    mobile = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control mb-2','placeholder':'Mobile'}),label="")
    address = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control mb-2','placeholder':'Address'}),label="")
    city = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control mb-2', 'placeholder': 'City'}), label="")
    state = forms.ChoiceField(choices=STATE, widget=forms.Select(attrs={'class': 'form-control mb-2', 'placeholder': 'Address'},),label="",)
    zip_code = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control mb-2','placeholder':'Zipcode'}),label="")
    
    
class ProfileForm(forms.ModelForm):
    image = forms.ImageField(widget=forms.FileInput(attrs={'class':'form-control mb-2'}),label="")

    class Meta:
        model = Order
        fields = ['image',]


class LoginPageForm(forms.ModelForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control mb-2','placeholder':'Username'}),label="")
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control mb-2','placeholder':'Password'}),label="")
    class Meta:
        model = User
        fields = ["username","password"]
    
class RegsiterForm(forms.ModelForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control mb-2','placeholder':'Username'}),label="")
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control mb-2','placeholder':'First name'}),label="")
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control mb-2','placeholder':'Last name'}),label="")
    email = forms.CharField(widget=forms.EmailInput(attrs={'class':'form-control mb-2','placeholder':'Email'}),label="")
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control mb-2','placeholder':'Enter Password'}),label="")
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control mb-2','placeholder':'Re-Enter Password'}),label="")


    class Meta:
        model = User
        fields = ["username","first_name","last_name","email","password1","password2"]