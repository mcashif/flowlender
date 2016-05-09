from django.shortcuts import render
from django.template import loader
from flowlendercms.models import ClientDetail
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from .forms import ClientDetailForm
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import get_object_or_404, render
from django.contrib.auth.decorators import login_required

@login_required(login_url='/login/')
def viewdata(request):

    clientData   = ClientDetail.objects.all()


    template = loader.get_template('flowlendercms/viewdata.html')

    context = {
        'clientData': clientData,
    }

    return HttpResponse(template.render(context, request))

@login_required(login_url='/login/')
def data(request):

    if request.method == 'POST':

        bname       = request.POST.get("bname")
        rparty      = request.POST.get("rparty")
        amount      = request.POST.get("amount")
        amount=str(amount).replace(",","")
        debit       = request.POST.get("debit")
        debit= str(debit).replace(",","")
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
        debitX      = float(debit)/float(amount)

        fd=ClientDetail(business_name=bname,
                        reffering_party=rparty,
                        ammount_request=float(amount),
                        debit_for=float(debit),
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

def logout(request):
    return HttpResponseRedirect('/login')

def login(request):
    return HttpResponseRedirect('/login')
