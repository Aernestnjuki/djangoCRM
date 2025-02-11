from django.shortcuts import render
from django.http import HttpResponse
from .models import *


def home_page(request):
    lead = Lead.objects.all()
    context = {
        "name": "Njuki",
        "programming_language": "Django",
        "lead": lead
    }
    return render(request, "home_page.html", context=context)

def lead_detail(request, pk):
    lead_pk = Lead.objects.get(id=pk)
    return HttpResponse(lead_pk.lead_name)
