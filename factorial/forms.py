from django import forms

class NumberForm(forms.Form):
    number = forms.IntegerField(min_value=0)
