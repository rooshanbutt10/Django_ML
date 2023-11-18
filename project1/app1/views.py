from django.shortcuts import render

from .models import Person

def welcome(request):

    return render(request,"base.html")

def aboutme_fun(request):
    
    return render(request,"aboutme.html")

def contactus_fun(request):
    result=None
    print('hi')
    if request.method=='POST':
        mynum = int(request.POST['number'])
        result=mynum *100
        print(mynum)

        myinstance=Person(userinputvalue=mynum,usercalvalue=result)
        myinstance.save()
        print ("Data Entered")
   
    return render(request,"contactus.html",{'result':result})
