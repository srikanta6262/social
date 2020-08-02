from django.shortcuts import render,redirect
from socialapp.models import contact as con
from socialapp.models import Data
# Create your views here.
#Loding First Page
def first(request):
    #update seen in database
    d=Data.objects.filter(status="confirm")
    for x in d:
        x.seen=x.seen+1
        x.save()
    d=Data.objects.filter(status="confirm")
    data1={"data":d}
    return render(request,'index.html',context=data1)

#Loading Photos page
def photos(request):
    d=Data.objects.filter(status="confirm")
    data1={"data":d}
    return render(request,'photos.html',context=data1)

#Loading contact page
def contact(request):
    return render(request,'contact.html')

#Loading about page
def about(request):
    return render(request,'about.html')

#Submitting Feedback
def feedback(request):
    if request.method=='POST':
        name=request.POST["name"]
        email=request.POST["email"]
        phone=request.POST["phone"]
        msg=request.POST["message"]
        data=con.objects.create(name=name,email=email,phone=phone,msg=msg)
        data.save()
        d=Data.objects.filter(status="confirm")
        data1={"msgcon":"feedback Submited","data":d}
        return render(request,'index.html',context=data1)
    else:
        return redirect('/index/')

#User Inserting Data
def data(request):
    if request.method=='POST':
        name=request.POST["name"]
        location=request.POST["loc"]
        msg=request.POST["message"]
        video=request.FILES.get("video")
        photo=request.FILES.get("photo")
        camera=request.FILES.get("camera")
        data=Data.objects.create(name=name,location=location,msg=msg,video=video,photo=photo,camera=camera)
        data.save()

        #update seen in database
        d=Data.objects.filter(status="confirm")
        for x in d:
            x.seen=x.seen+1
            x.save()

        d=Data.objects.filter(status="confirm")
        data1={"msgin":"Your Data Has Been uploaded Sucessfully...\n And Waiting Confirmation From Admin...","data":d}
        return render(request,'index.html',context=data1)
    else:
        return redirect('/index/')
