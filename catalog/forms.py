from django import forms
from .models import Product, Version

class StyleFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field_name, field in self.fields.items():
            if not isinstance(field.widget, forms.CheckboxInput):
                field.widget.attrs['class'] = 'form-control'
class ProductForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'

    def clean_name(self):
        cleaned_data = self.cleaned_data['name']
        prohibited_products = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция',
                               'радар']
        for obj in prohibited_products:
            if obj in cleaned_data:
                raise forms.ValidationError("Такой продукт нельзя создать")

        return cleaned_data

    def clean_description(self):
        cleaned_data = self.cleaned_data['description']
        prohibited_products = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция',
                               'радар']
        for obj in prohibited_products:
            if obj in cleaned_data:
                raise forms.ValidationError("Такой продукт нельзя создать")

        return cleaned_data
class VersionForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Version
        fields = '__all__'
