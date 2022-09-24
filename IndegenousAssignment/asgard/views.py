from django.shortcuts import render
from django.http import HttpResponse
from asgard.models import Item
from django.views.generic import View
from django.core import serializers

def index(request):
    # it = Item.objects.all()
    # l = serializers.serialize('json',it)
    l = Item.objects.all().values()
    return render(request, "asgard/index.html",{'Type' : l})