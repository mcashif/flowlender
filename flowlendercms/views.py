from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from flowlendercms.models import ClientDetail
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from .forms import ClientDetailForm


def data(request):

    if request.method == 'POST':

        bname       = request.POST.get("bname")
        rparty      = request.POST.get("rparty")
        amount      = request.POST.get("amount")
        debit       = request.POST.get("debit")
        fdSelect    = request.POST.get("fdSelect")
        credit      = request.POST.get("credit")
        csSelect    = request.POST.get("csSelect")
        cname       = request.POST.get("cname")
        address2    = request.POST.get("address2")
        if not address2:
            address2="NIL"
        contact2    = request.POST.get("contact2")
        if not contact2:
            contact2="NIL"
        mobileX     = "qq"
        faxX        = "qq"
        email2      = request.POST.get("email2")
        if not email2:
            contact2="NIL@NIL.com"
        debitX      = int(debit)/int(amount)

        fd=ClientDetail(business_name=bname,
                        reffering_party=rparty,
                        ammount_request=amount,
                        debit_for=debit,
                        payment_plan=fdSelect,
                        credit_score=credit,
                        current_status=csSelect,
                        contact_name=cname,
                        mailing_address=address2,
                        office_number=contact2,
                        mobile_number=mobileX,
                        fax_number=faxX,
                        email=email2,
                        debit_ratio=debitX)
        fd.save()



    clientDetailRP   = ClientDetail.objects.values('reffering_party').distinct()


    template = loader.get_template('flowlendercms/clientdetail.html')

    context = {
        'clientDetailRP': clientDetailRP,
    }

    return HttpResponse(template.render(context, request))

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
