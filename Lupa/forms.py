from django import forms

class BusquedaForm(forms.Form):
    query = forms.CharField(label='Buscar en MonClothes', max_length=100, required=False)