from django.shortcuts import render
from .models import Configuration


def post_list(request):
    return render(request, 'spiderapp/post_list.html', {})

def configuration_view(request):
    configuration=Configuration.objects.get()
    return render(request,'spiderapp/configuration.html', {'configuration': configuration})
