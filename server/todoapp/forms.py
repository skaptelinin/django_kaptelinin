from django import forms
from .models import TodoItem
 
class TodoInputForm(forms.Form):
    text = forms.CharField(widget=forms.TextInput(
        attrs={'class' : 'form-control col-md-11', 'autofocus': True,
        'autocomplete': 'off'}))

class TodoEditForm(forms.ModelForm):
    class Meta:
        model = TodoItem
        fields = ['text', 'status']