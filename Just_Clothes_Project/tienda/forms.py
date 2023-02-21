from django import forms


class EditProfile(forms.Form):
    username = forms.CharField(max_length=1000, widget=forms.TextInput(attrs={'class': "form-control"}))
    first_name = forms.CharField(max_length=1000, widget=forms.TextInput(attrs={'class': "form-control"}))
    last_name = forms.CharField(max_length=1000, widget=forms.TextInput(attrs={'class': "form-control"}))
    email = forms.EmailField(max_length=200, widget=forms.EmailInput(attrs={'class': "form-control"}))
    address = forms.CharField(max_length=1000, widget=forms.TextInput(attrs={'class': "form-control"}))

class CreateProfile(forms.Form):
    username = forms.CharField(max_length=1000, widget=forms.TextInput(attrs={'class': "form-control"}))
    password = forms.CharField(max_length=1000, widget=forms.TextInput(attrs={'class': "form-control"}))
    first_name = forms.CharField(max_length=1000, widget=forms.TextInput(attrs={'class': "form-control"}))
    last_name = forms.CharField(max_length=1000, widget=forms.TextInput(attrs={'class': "form-control"}))
    email = forms.EmailField(max_length=200, widget=forms.EmailInput(attrs={'class': "form-control"}))
    address = forms.CharField(max_length=1000, widget=forms.TextInput(attrs={'class': "form-control"}))
