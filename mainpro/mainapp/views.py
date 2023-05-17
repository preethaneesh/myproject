from django.http import HttpResponse
from django.shortcuts import render
from .models import Place
from .models import Team

# Create your views here.
# def home(request):
#     return HttpResponse('My First Django project')
# def htmlpagerender(request):
#     return render(request,'mypage.html')
# def aboutpage(request):
#     return render(request,'about.html')
# def contactspage(request):
#     return HttpResponse('contacts html page')
# def demo(request):
#     name='india'
#     return render(request,'index1.html',{'obj':name})
# def addition(request):
#     x=int(request.GET['num1'])
#     y=int(request.GET['num2'])
#     res=x+y
    
#     return render(request,'result.html',{'result':res})
def demo(request):
    obj=Place.objects.all()
    tm=Team.objects.all()
    return render(request,"index.html",{'result':obj,'mem':tm})