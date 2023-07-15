from django import forms
from django.forms import ModelForm
from .models import Profile
from django.contrib.auth.models import User

class UpdateProfileForm(forms.ModelForm):
    profile_pic = forms.ImageField(widget=forms.FileInput(attrs={'class': 'input'}))
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    phone_number = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(widget=forms.EmailInput({'class': 'form-control'}))

    class Meta:
        model = Profile
        fields = ['profile_pic', 'email','first_name','last_name','phone_number'] 

class UpdateUserForm(forms.ModelForm): 
    username = forms.CharField(max_length=100,required=True,widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ['username', 'email']