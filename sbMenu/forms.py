from django import forms
from .models import *


class hamburguesaForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            if isinstance(field, forms.DecimalField):
                field.widget.attrs['class'] += ' decimal-field'
            elif isinstance(field, forms.ImageField):
                field.widget.attrs['class'] += ' image-field'

    class Meta:
        model =  hamburguesa
        fields = '__all__'





