from django.shortcuts import render
from django.views.generic import TemplateView

from quarry.forms import ModelFilterForm
from quarry.models import DumpTrucks


class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        parameters = DumpTrucks.objects.all()
        form = ModelFilterForm(self.request.GET)

        if self.request.method == 'GET':
            if not form.is_valid():
                form.fields['model'].initial = 'Все'

        if form.is_valid():
            parameters = DumpTrucks.objects.filter(model__name=form.cleaned_data['model'])

        context['form'] = form
        context['parameters'] = parameters

        return context
