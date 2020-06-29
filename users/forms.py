from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms import TextInput, EmailInput

from users.models import Profile


class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={'class': 'form-control'}))
    username = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2',)

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if User.objects.filter(username=username).exists():
            self.fields['username'].widget.attrs['class'] += ' is-invalid'
            raise forms.ValidationError("This username is already in use.")
        return username

    def clean_email(self):
        email = self.cleaned_data.get('email')
        username = self.cleaned_data.get('username')

        if email and User.objects.filter(email=email).exclude(username=username).exists():
            self.fields['email'].widget.attrs['class'] += ' is-invalid'
            raise forms.ValidationError(f'Account with {email} email already exists.')
        return email


class UserForm(forms.ModelForm):
    username = forms.CharField(required=True, widget=TextInput(attrs={'class': 'form-control username'}))
    first_name = forms.CharField(required=False, widget=TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(required=False, widget=TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(required=True, widget=EmailInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email',)


class ProfileForm(forms.ModelForm):
    image = forms.FileField(required=False, widget=forms.FileInput(attrs={'class': 'form-control upload_img'}))
    location = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    birth_date = forms.DateField(required=False, widget=forms.DateInput(attrs={'class': 'form-control'}))
    bio = forms.CharField(required=False, widget=forms.Textarea(attrs={'class': 'form-control'}))

    class Meta:
        model = Profile
        fields = ('image', 'location', 'bio', 'birth_date',)


