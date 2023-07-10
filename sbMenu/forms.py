from django import forms
from .models import *


class hamburguesaForm(forms.ModelForm):

    class Meta:
        model =  hamburguesa
        fields = '__all__'





