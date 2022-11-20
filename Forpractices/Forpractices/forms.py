# Creation of forms by Django.
from django import forms

class usersform(forms.Form):
    Username=forms.CharField()#required=False
    # Widget=forms.TextInput(attrs={'class':"form-control"})
    # print('\n')
    password = forms.CharField(widget=forms.PasswordInput )#label="Value 2"
    Email=forms.EmailField()

