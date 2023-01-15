from django.core.serializers.json import DjangoJSONEncoder
from django.shortcuts import render
from django.views.decorators.http import require_http_methods
from django.template import loader
from django.http import HttpResponse
from .service.dex import DEXModel
from django.conf import settings
from .forms import DexForm, DexFormWithDescription
import logging

logger = logging.getLogger("ocena")


def main(request): # Skripta za main stran
    dex = DEXModel(settings.DEX_MODEL)
    template = loader.get_template('ocena/main.html') # Template za main stran
    context = {'form': DexFormWithDescription(dex.get_input_attributes_with_descriptions())}
    return HttpResponse(template.render(context, request))


@require_http_methods(["POST"])
def final(request): # Skripta za stran z rezultati
    dex = DEXModel(settings.DEX_MODEL)
    form = DexForm(dex.get_input_attributes(), request.POST)
    if form.is_valid(): # Izvede se le, če je forma veljavna
        template = loader.get_template('ocena/final.html') # Template za stran z rezultati
        quantitative_response, qualitative_response = dex.evaluate_model(form.cleaned_data)
        context = {'quantitative_response': quantitative_response, 'qualitative_response': qualitative_response} # Prva spremenljivka za kvantitativni odziv, druga za kvalitatitvni
        return HttpResponse(template.render(context, request))
    return render(request, "main.html", {"form": form})