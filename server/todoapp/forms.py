from django import forms
from .models import TodoItem
 
class TodoInputForm(forms.Form):
    text = forms.CharField()

# class NavigationButtons(forms.Form):
#     show_all = forms.

class TodoEditForm(forms.ModelForm):
    class Meta:
        model = TodoItem
        fields = ['text', 'status']