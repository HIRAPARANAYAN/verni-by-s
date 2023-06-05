from django.shortcuts import render

def CustomerDashboard(request):
    return render(request,'Customer\index.html')
def MyProfile(request):
    return render(request,'Customer\myprofile.html')
def KYCDocument(request):
    return render(request,'Customer\KYCDocument.html')
