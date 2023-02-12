from django import forms

from .models import DumpTruckModels


class ModelFilterForm(forms.Form):
    model = forms.ModelChoiceField(
        label='Модель',
        queryset=DumpTruckModels.objects.all(),
        widget=forms.Select(
            attrs={
                'id': 'filter1'
            }
        ),
        initial='Все',
    )

    def __init__(self, *args, **kwargs):
        super(ModelFilterForm, self).__init__(*args, **kwargs)
        self.fields['model'].choices = [('все', 'Все')] + list(self.fields['model'].choices)
