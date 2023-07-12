from django.shortcuts import render
from app.forms import *
from django.http import HttpResponse
# Create your views here.
def validate(request):
    sfo=StudentForm()
    d={'sfo':sfo}
    if request.method=="POST":
        sfd=StudentForm(request.POST)
        if sfd.is_valid():
            return HttpResponse(str(sfd.cleaned_data))
        else:
            return HttpResponse('invalid')
    return render(request,'validate.html',d)