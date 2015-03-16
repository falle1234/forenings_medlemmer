from django import forms
from members.models import Person

class PersonForm(forms.ModelForm):
    class Meta:
        model=Person
        fields= ['name','street','placename','zipcity','email','phone']