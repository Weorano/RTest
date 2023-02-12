from django.shortcuts import render

from quarry.forms import ModelFilterForm
from quarry.models import DumpTrucks


def index_view(request):
    parameters = DumpTrucks.objects.all()

    if request.method == 'GET':
        form = ModelFilterForm(request.GET)
        if not form.is_valid():
            form.fields['model'].initial = 'Все'
    else:
        form = ModelFilterForm(request.GET)

    if form.is_valid():
        parameters = DumpTrucks.objects.filter(model__name=form.cleaned_data['model'])

    return render(request, 'index.html', {
        'form': form,
        'parameters': parameters
    })
