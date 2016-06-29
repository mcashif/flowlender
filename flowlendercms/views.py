from django.shortcuts import render
from django.template import loader
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import get_object_or_404, render
import json




def index(request):
    template = loader.get_template("flowlendercms/index.html")
    return HttpResponse(template.render())

def getjson(request):
    if request.method == 'GET':
            with open('/Users/Apple/pythoneprojects/items.txt') as data_file:
                 jdata = json.load(data_file)
            return HttpResponse(jdata, content_type = 'application/json')

def submit(request):
    template = loader.get_template("flowlendercms/submit.html")
    return HttpResponse(template.render())
