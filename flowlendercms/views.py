from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from flowlendercms.models import Feedback
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse

# Create your views here.
@csrf_exempt
def index(request):

    if request.method == 'POST':
    #POST goes here . is_ajax is must to capture ajax requests. Beginner's pit.
        if request.is_ajax():
            #Always use get on request.POST. Correct way of querying a QueryDict.
            fd=Feedback(name=request.POST.get('name'),phone=request.POST.get('phone'),email=request.POST.get('email'),message=request.POST.get('message'))
            fd.save()
            #Returning same data back to browser.It is not possible with Normal submit
            data = {"status":"sucess"}

            return JsonResponse(data)

    template = loader.get_template('flowlendercms/index.html')
    return HttpResponse(template.render(request))
