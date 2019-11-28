from django import forms
 
class TodoInputForm(forms.Form):
    text = forms.CharField(widget=forms.TextInput(
        attrs={'class' : 'form-control col-md-11', 'autofocus': True,
        'autocomplete': 'off'}))

class TodoEditForm(forms.Form):
    text = forms.CharField(widget=forms.TextInput(
        attrs={'class' : 'form-control col-md-11',
        'id': 'id_edit_text',
        'autocomplete': 'off'}))