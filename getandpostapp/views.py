from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def getinput(request):
    return render(request,"getinput.html")
def postinput(request):
    return render(request,"postinput.html")
def add(request):
    if request.method=="GET":
        x=int(request.GET['t1'])
        y=int(request.GET['t2'])
        z=x+y
        return HttpResponse("<html><body bgcolor=yellow>sum is:" +str(z) + "</body></html>")
    else:
        x = int(request.POST['t1'])
        y = int(request.POST['t2'])
        z = x + y
        return HttpResponse("<html><body bgcolor=yellow>sum is:" + str(z) + "</body></html>")



