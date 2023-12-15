from django.shortcuts import render,HttpResponse,HttpResponseRedirect

from wscubetech.settings import BASE_DIR

from .forms import userForm
from service.models import Service
from courses.models import Courses
from About.models import About
from android.models import Android
from uiux.models import UIUX
from contactEnquiry.models import contactEnquiry
from web.models import Web
from enquiry.models import Enquiry

def home(request):
    if request.method=="POST":
       name = request.POST.get('name')
       email = request.POST.get('email')
       number = request.POST.get('number')
       qu= Enquiry(name=name,email=email,number=number)
       qu.save()
        
    data={
        'title':'Design Dynamiics',
        'bdata':'Welcome To Design Dynamiics',
        'clist':['Django','Angular','React'],
        'student':[
            {
                'name':'Shrinath','phone':'9883323121'
               
            },{            
               'name': 'Viju' ,'phone':'9372394236'
              }
        ],
        'number':[10,20,30,40],
        
        
        }
          
    return render(request,"index.html",data)

def web(request):
      if request.method=="POST":
       name = request.POST.get('name')
       email = request.POST.get('email')
       number = request.POST.get('number')
       qu= Enquiry(name=name,email=email,number=number)
       qu.save()
      webData = Web.objects.all()
      we = {
            'webData': webData
        }
      return render(request,"webdesignservice.html",we)

def uiux(request):
    if request.method=="POST":
       name = request.POST.get('name')
       email = request.POST.get('email')
       number = request.POST.get('number')
       qu= Enquiry(name=name,email=email,number=number)
       qu.save()
    uiuxData = UIUX.objects.all()
    ix = {
            'uiuxData': uiuxData
        }
    return render(request,"uiux.html",ix)

def appdev(request):
    if request.method=="POST":
       name = request.POST.get('name')
       email = request.POST.get('email')
       number = request.POST.get('number')
       qu= Enquiry(name=name,email=email,number=number)
       qu.save()
    return render(request,"appdev.html",)

def aboutUs(request):
    if request.method=="POST":
       name = request.POST.get('name')
       email = request.POST.get('email')
       number = request.POST.get('number')
       qu= Enquiry(name=name,email=email,number=number)
       qu.save()
    AboutData= About.objects.all()
    about ={
        'AboutData':AboutData
    }
    return render(request,"about.html",about)

def services(request):
    if request.method=="POST":
       name = request.POST.get('name')
       email = request.POST.get('email')
       number = request.POST.get('number')
       qu= Enquiry(name=name,email=email,number=number)
       qu.save()
    servicesData = Service.objects.all().order_by('-service_title')[:3]
    ser ={
        'servicesData':servicesData
    }
    return render(request,"services.html",ser)



def contactus(request):
    if request.method=="POST":
       name = request.POST.get('name')
       email = request.POST.get('email')
       message = request.POST.get('message')
       en= contactEnquiry(name=name,email=email,message=message)
       en.save()
       
    return render(request,"contact.html")

    

def courses(request):
    return HttpResponse("Welcome to Courses")

def coursedetail(request,coursename):
    return HttpResponse(coursename)

def calculator(request):
    c=""
    try:
        if request.method =="POST":
            n1 = eval(request.POST.get('n1'))
            op = request.POST.get('op')
            n2 = eval(request.POST.get('n2'))
            if op =="+":
               c= n1+n2
            elif op=="-":
               c = n1-n2
            elif op=="*":
               c = n1*n2
            elif op=="/":
               c = n1/n2
    except:
        c = "Invalid "
    return render(request,"calculator.html",{'c':c})

def saveevenodd(request):
    c=''
    if request.method =="POST":
            if request.POST.get('n1')=="":
                return render(request,"evenodd.html",{'error':True})
            n1 = eval(request.POST.get('n1'))
            if n1%2==0:
                c ="Number is Even"
            else :
               c ="Number is Odd"
    return render(request,"evenodd.html",{'c':c})

def marklist(request):
   
    if request.method =="POST":
            s1 = eval(request.POST.get('s1'))
            s2 = eval(request.POST.get('s2'))
            s3 = eval(request.POST.get('s3'))
            s4 = eval(request.POST.get('s4'))
            s5 = eval(request.POST.get('s5'))
            t = s1+s2+s3+s4+s5
            p = t*100/500
            d ={
                'total':t,
                'per': p
            }
            return render(request,"marklist.html",d)
    return render(request,"marklist.html")
   
def enquiry(request):
    if request.method=="POST":
       name = request.POST.get('name')
       email = request.POST.get('email')
       number = request.POST.get('number')
       qu= Enquiry(name=name,email=email,number=number)
       qu.save()
    return render(request,"index.html")
          