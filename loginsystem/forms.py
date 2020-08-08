from django import forms
from .models import *

class register(forms.ModelForm):

    def __init__(self, *args, **kwargs):

        super(register, self).__init__(*args, **kwargs)
        self.fields['username'].label = "User Name"
        self.fields['emailID'].label = "Email Address"
        self.fields['password'].label = "Password"
        self.fields['password_again'].label = "Confirm Your Password"
        self.fields['password'].min_length = 8

    class Meta:
        model = newuser
        fields = '__all__'
    
    username = forms.CharField(widget = forms.TextInput(attrs = {'placeholder': 'Please Enter your username', 'class': 'col-md-4'}))
    emailID = forms.EmailField(widget = forms.TextInput(attrs = {'placeholder': 'Please Enter Your Email Address', 'class': 'col-md-4'}))
    password = forms.CharField(widget = forms.PasswordInput(attrs = {'placeholder': 'Please Enter Your Password', 'class': 'col-md-4'}))
    password_again = forms.CharField(widget = forms.PasswordInput(attrs = {'placeholder': 'Please Enter Your Password', 'class': 'col-md-4'}))


class login(forms.Form):

    def __init__(self, *args, **kwargs):

        super(login, self).__init__(*args, **kwargs)
        self.fields['username'].label = "User Name"
        self.fields['password'].label = "Password"

    username = forms.CharField(widget = forms.TextInput(attrs = {'placeholder': 'Please Enter Your Username', 'class': 'col-md-4'}))
    password = forms.CharField(widget = forms.PasswordInput(attrs = {'placeholder': 'Please Enter Your Password', 'class': 'col-md-4'}))

class passwordemailform(forms.Form):

    def __init__(self, *args, **kwargs):

        super(passwordemailform, self).__init__(*args, **kwargs)
        self.fields['emailID'].label = "Enter your registered email id"

    emailID = forms.EmailField(
        widget=forms.TextInput(
            attrs={'placeholder': 'Enter your registered email id', 'class': 'col-md-4'}
        )
    )

class password_reset(forms.Form):

    def __init__(self, *args, **kwargs):

        super(password_reset, self).__init__(*args, **kwargs)
        self.fields['username'].label = "User Name"
        self.fields['password'].label = "New Password"
        self.fields['password_again'].label = "Confirm New Password"

    username = forms.CharField(
        widget=forms.TextInput(
            attrs={'placeholder': 'Please Enter a valid username', 'class': 'col-md-4'}
        )
    )

    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={'placeholder': 'Please Enter A Password', 'class': 'col-md-4'}
        )
    )

    password_again = forms.CharField(
        widget=forms.PasswordInput(
            attrs={'placeholder': 'Please Confirm Your Password', 'class': 'col-md-4'}
        )
    )
