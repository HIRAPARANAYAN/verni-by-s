from django.shortcuts import render

def Dashboard(request):
    return render(request,'adminDashboard/index.html')

def Search(request):
    return render(request,'adminDashboard/Search.html')
def Digitalbloan(request):

    return render(request,'adminDashboard/Digitalbloan.html')
def Digitalploan(request):
    return render(request,'adminDashboard/Digitalploan.html')
def Premiumploan(request):
    return render(request,'adminDashboard/Premiumploan.html')
def Premiumbloan(request):
    return render(request,'adminDashboard/Premiumbloan.html')
def Customers(request):
    return render(request,'adminDashboard/Customers.html')
def Createaccount(request):
    return render(request,'adminDashboard/Createaccount.html')
def Cardoffer(request):
    return render(request,'adminDashboard/Cardoffer.html')
def Specialoffer(request):
    return render(request,'adminDashboard/Specialoffer.html')
def Bumperoffer(request):
    return render(request,'adminDashboard/Bumperoffer.html')
def Staroffer(request):
    return render(request,'adminDashboard/Staroffer.html')
def Loanlist(request):
    return render(request,'adminDashboard/Loanapplicationlist.html')
def Loanapproved(request):
    return render(request,'adminDashboard/Loanapproved.html')
def Loanreapply(request):
    return render(request,'adminDashboard/Loanreapply.html')
def Loanquery(request):
    return render(request,'adminDashboard/Loanquery.html')
def Loanrejected(request):
    return render(request,'adminDashboard/Loanrejected.html')
def Marvelcard(request):
    return render(request,'adminDashboard/Marvelcardlist.html')
def Universalcard(request):
    return render(request,'adminDashboard/Universalcardlist.html')
def Customerreferrals(request):
    return render(request,'adminDashboard/Customerreferrals.html')
def Allleads(request):
    return render(request,'adminDashboard/Allleads.html')
def Personalleads(request):
    return render(request,'adminDashboard/Personalloanleads.html')
def Businessleads(request):
    return render(request,'adminDashboard/Businessloanleads.html')
def Customerleads(request):
    return render(request,'adminDashboard/Custmorregleads.html')
def GSTData(request):
    return render(request,'adminDashboard/GSTdata.html')
def Bank(request):
    return render(request,'adminDashboard/Bank.html')
def Applybank(request):
    return render(request,'adminDashboard/Applybank.html')
def Currentopenning(request):
    return render(request,'adminDashboard/Currentopenning.html')
def Careerenquiry(request):
    return render(request,'adminDashboard/Currentenquiry.html')
def BulkOTPs(request):
    return render(request,'adminDashboard/BulkSMSlist.html')
def SupportReq(request):
    return render(request,'adminDashboard/Supportrequest.html')
def ConntactEnq(request):
    return render(request,'adminDashboard/Contactenquiry.html')
def NewsletterSub(request):
    return render(request,'adminDashboard/Newslettersub.html')
def SentOTPs(request):
    return render(request,'adminDashboard/Sentotps.html')
def Importantupdate(request):
    return render(request,'adminDashboard/Importantupdate.html')
def SiteSettings(request):
    return render(request,'adminDashboard/SiteSettings.html')
def SMSMessages(request):
    return render(request,'adminDashboard/SMSMessages.html')
def Accountmessage(request):
    return render(request,'adminDashboard/Accountmessage.html')

