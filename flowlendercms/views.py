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
    template = loader.get_template("flowlendercms/index.html")
    return HttpResponse(template.render())

def getjson(request):
    #leads_as_json = serializers.serialize('json', EventDetail.objects.all())
    #return HttpResponse(leads_as_json, content_type='json')
    dataX={}
    DataM = []
    QS=EventDetail.objects.all()

    for obj in QS:
        data={}
        data['id'] = obj.id
        data['category'] = "real_estate"
        data['title'] = obj.event_name
        data['location'] = obj.location
        strX=str(obj.event_geocode)
        listX=strX.split(",")
        data['latitude'] = float(listX[0])
        data['longitude'] = float(listX[1])
        data['url'] = obj.event_web

        #XXXXXXXXXXXXXXXXX
        data['type'] = "760.24 Miles"
        data['type_icon'] =  "/static/assets/icons/store/apparel/umbrella-2.png"
        data['rating'] = 4
        data['cattye'] = "Double Elimination"
        data['result'] = "Time Only"
        data['xyz'] = "KIDS"
        #XXXXXXXXXXXXXXXXX
        objP=Promoter.objects.get(pk=1)
        data['promotor'] = objP.promoter_name

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
        data['gi'] = obj.gi
        data['nogi'] = obj.nogi
        data['kids'] = obj.kids
        data['pro'] = obj.pro
        data['purse'] = obj.purse
        data['absolute'] = obj.absolute
        data['adults'] = obj.adults
        data['kids_special_format'] = obj.kids_special_format

        data['cost'] = obj.cost
        data['predate'] = obj.predate
        data['cost_late'] = obj.cost_late
        data['cutoff_date'] = obj.cutoff_date
        data['event_description'] = obj.event_description
        data['event_web'] = obj.event_web

        data['small_image'] = obj.small_image.url
        data['large_image'] = obj.large_image.url


        DataM.append(data)

    dataX['data']=DataM
    json_data = json.dumps(dataX)
    return HttpResponse(json_data, content_type='json')

def submit(request):
    template = loader.get_template("flowlendercms/submit.html")
    return HttpResponse(template.render())
