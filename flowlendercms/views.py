from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from flowlendercms.models import Feedback,Service,New,Contect,Apply,About
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

    contacts    = Contect.objects.filter(pk=1)
    applylist   = Apply.objects.all()
    sevicelist  = Service.objects.all()
    newslist    = New.objects.all()
    aboutlist   = About.objects.filter(pk=1)

    template = loader.get_template('flowlendercms/index.html')

    context = {
        'contacts': contacts,
        'applylist': applylist,
        'sevicelist': sevicelist,
        'newslist': newslist,
        'aboutlist': aboutlist,
    }

    return HttpResponse(template.render(context, request))
