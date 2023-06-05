import random
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from .models import Temp,Signup,Loan_registration,Order
from django.conf import settings
from .constants import PaymentStatus
import requests
import razorpay
import json

# Create your views here.

def login(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        temp = Temp.objects.filter(phone=phone).first()
        if not temp:
            otp = random.randint(1000, 9999)
            tempnew = Temp(name=name,phone=phone,otp=otp,max_otp_try=2)
            tempnew.save()
            send_otp(phone, otp)
            request.session['name'] = name
            request.session['phone'] = phone
            context = {'phone': phone}
            return render(request, 'authentication/otp.html', context)
        else:
            finaluser = Signup.objects.filter(phone=phone).first()
            if not finaluser:
                if temp.max_otp_try > 0:
                    otp = random.randint(1000, 9999)
                    otemp = Temp.objects.get(phone=phone)
                    otemp.otp=otp
                    otemp.max_otp_try -=1
                    otemp.save()
                    send_otp(phone,otp)
                    request.session['name'] = name
                    request.session['phone'] = phone
                    context = {'phone':phone}
                    return render(request,'authentication/otp.html',context)
                else:
                    context={'message':'You Have Reach Your Maximum Try For OTP Verification'}
                    return render(request, 'authentication/loginform.html',context)
            else:
                context={'message':'User is Already Exits With This Phone Number'}
                return render(request, 'authentication/loginform.html',context)
    return render(request,'authentication/loginform.html')

def send_otp(phone,otp):


    url = "https://2factor.in/API/V1/172934ba-f7d2-11ed-addf-0200cd936042/SMS/{}/{}/otp".format(phone,otp)

    requests.post(url)



def verifyotp(request):
    if request.method=='POST':
        eotp = request.POST.get('otp')
        eotp += request.POST.get('otp1')
        eotp += request.POST.get('otp2')
        eotp += request.POST.get('otp3')
        phone=request.session['phone']
        name=request.session['name']
        current = Temp.objects.filter(phone=phone).values()
        if current[0]['otp'] == eotp:
            finaluser = Signup(name=name,phone=phone,is_verified=True)
            finaluser.save()
            # del request.session['phone']
            return render(request, 'authentication/multiform.html',{'name':name,'phone':phone})
        else:
            context = {'message': "OTP is invalid"}
            return render(request, 'authentication/otp.html', context)
    return render(request,'authentication/loginform.html')

def multiform(request):
    if request.method == 'POST':
        phone = request.session['phone']
        name = request.session['name']
        persontype = request.POST.get('persontype')
        name = request.POST.get('firstname')
        email = request.POST.get('email')
        require_loan_amount = request.POST.get('requireloanamount')
        cibil_score = request.POST.get('cibilScoree')
        monthly_income = request.POST.get('monthlyincome')
        monthly_emi_you_pay = request.POST.get('monthlyemi')
        loan_purpose = request.POST.get('loanpurpose')
        city = request.POST.get('city')
        state = request.POST.get('state')
        emi_tenure= request.POST.get('tenure')
        print(persontype,email,require_loan_amount,cibil_score,monthly_income,monthly_emi_you_pay,loan_purpose,
              city,state,emi_tenure)
        robj = Loan_registration(name=name,phone=phone,persontype=persontype,email=email,require_loan_amount=require_loan_amount,cibil_score=cibil_score,monthly_income=monthly_income,
                                 monthly_emi_you_pay=monthly_emi_you_pay,loan_purpose=loan_purpose,city=city,state=state,emi_tenure=emi_tenure)
        robj.save()
        return render(request,'Customer/index.html')
    return render(request,'authentication/multiform.html')


def payment_home(request):
    return render(request, "authentication/payment_index.html")

def order_payment(request):
    if request.method == "POST":
        name = request.POST.get("name")
        amount = request.POST.get("amount")
        client = razorpay.Client(auth=(settings.RAZORPAY_KEY_ID, settings.RAZORPAY_KEY_SECRET))
        razorpay_order = client.order.create(
            {"amount": int(amount) * 100, "currency": "INR", "payment_capture": "1"}
        )
        order = Order.objects.create(
            name=name, amount=amount, provider_order_id=payment_order["id"]
        )
        order.save()
        return render(
            request,
            "payment.html",
            {
                "callback_url": "http://" + "127.0.0.1:8000" + "/razorpay/callback/",
                "razorpay_key": settings.RAZORPAY_KEY_ID,
                "order": order,
            },
        )
    return render(request, "authentication/payment.html")

@csrf_exempt
def callback(request):
    def verify_signature(response_data):
        client = razorpay.Client(auth=(settings.RAZORPAY_KEY_ID,settings.RAZORPAY_KEY_SECRET))
        return client.utility.verify_payment_signature(response_data)

    if "razorpay_signature" in request.POST:
        payment_id = request.POST.get("razorpay_payment_id", "")
        provider_order_id = request.POST.get("razorpay_order_id", "")
        signature_id = request.POST.get("razorpay_signature", "")
        order = Order.objects.get(provider_order_id=provider_order_id)
        order.payment_id = payment_id
        order.signature_id = signature_id
        order.save()
        if not verify_signature(request.POST):
            order.status = PaymentStatus.SUCCESS
            order.save()
            return render(request, "callback.html", context={"status": order.status})
        else:
            order.status = PaymentStatus.FAILURE
            order.save()
            return render(request, "callback.html", context={"status": order.status})
    else:
        payment_id = json.loads(request.POST.get("error[metadata]")).get("payment_id")
        provider_order_id = json.loads(request.POST.get("error[metadata]")).get(
            "order_id"
        )
        order = Order.objects.get(provider_order_id=provider_order_id)
        order.payment_id = payment_id
        order.status = PaymentStatus.FAILURE
        order.save()
        return render(request, "callback.html", context={"status": order.status})