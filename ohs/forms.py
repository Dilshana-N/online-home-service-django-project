from django import forms
from django.contrib.auth.forms import UserCreationForm

from ohs.models import Register, Login


class login_form(UserCreationForm):
    class Meta:
        model = Login
        fields =('username','password1','password2')


class Register(forms.ModelForm):
    class Meta:
        model = Register
        fields = '__all__'
        exclude = ('user',)
