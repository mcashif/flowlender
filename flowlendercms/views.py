from django.shortcuts import render
from django.template import loader
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import get_object_or_404, render
from django.core import serializers
from .models import EventDetail,Promoter
import json



def index(request):

    latitude=0
    latitude=0

    if "latitude" in request.session:
        latitude = request.session["latitude"]

    if "longitude" in request.session:
        longitude = request.session["longitude"]

    return render(request, 'flowlendercms/index.html', {'lat': latitude, 'lng': longitude})

def detail(request,event_id):
    event = get_object_or_404(EventDetail, pk=event_id)
    return render(request, 'flowlendercms/event_detail.html', {'event': event})

def setSessionData(request):

    if "latitude" in request.GET:
        del request.session['latitude']
        request.session['latitude'] = request.GET["latitude"]

    if "longitude" in request.GET:
        del request.session['longitude']
        request.session['longitude'] = request.GET["longitude"]

    return HttpResponse(request.session['latitude'])

def getjson(request):
    dataX={}
    DataM = []
    QS=EventDetail.objects.all()
    count=1
    for obj in QS:
        data={}
        data['id'] = count
        count+=1
        data['category'] = "real_estate"
        data['title'] = obj.event_name
        data['location'] = obj.location
        strX=str(obj.event_geocode)
        listX=strX.split(",")
        data['latitude'] = float(listX[0])
        data['longitude'] = float(listX[1])
        data['url'] = obj.event_web


        data['promotor'] = str(obj.event_promoter)

        data['event_date'] = str(obj.event_date)
        data['event_tentitive'] = obj.event_tentitive
        data['end_date'] = str(obj.end_date)
        data['address'] = obj.address
        data['city'] = obj.city
        data['state'] = obj.state
        data['zip_code'] = obj.zip_code

        data['rule'] = obj.rule
        data['bracket'] = obj.bracket
        data['kids_special_formats'] = obj.kids_special_formats
        data['kids_special_rules'] = obj.kids_special_rules

        data['GI'] = obj.gi
        data['NOGI'] = obj.nogi
        data['KIDS'] = obj.kids
        data['PRO'] = obj.pro
        data['PURSE'] = obj.purse
        data['ABSOLUTE'] = obj.absolute
        data['ADULTS'] = obj.adults
        data['KSF'] = obj.kids_special_format

        data['cost'] = obj.cost
        data['predate'] = str(obj.predate)
        data['cost_late'] = obj.cost_late
        data['cutoff_date'] = str(obj.cutoff_date)
        data['event_description'] = obj.event_description
        data['event_web'] = obj.event_web

        objP=Promoter.objects.get(promoter_name=obj.event_promoter)
        data['small_image'] = objP.promoter_logo.url
        data['large_image'] = obj.large_image.url


        DataM.append(data)

    dataX['data']=DataM
    json_data = json.dumps(dataX)
    return HttpResponse(json_data, content_type='json')

def submit(request):
    template = loader.get_template("flowlendercms/submit.html")
    return HttpResponse(template.render())
