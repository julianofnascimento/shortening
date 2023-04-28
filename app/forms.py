from django import forms

class UrlForm(forms.Form):
    url = forms.CharField(label="Enter a URL to short: ", max_length=150)