from django import forms
 
class TodoInputForm(forms.Form):
    text = forms.CharField()
    status = forms.BooleanField()