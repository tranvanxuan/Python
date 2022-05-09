from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from home.models import Student
# Create your views here.
def index(request):
    try:
        students= Student.objects.all()
    except:
        raise Http404('No data')
    return render(request, 'home.html', context={'students': students} )

def register(request):
    return render(request, 'register.html')

def addrecord(request):
    try:
        if request.method=='POST':
            name=request.POST['name']
            age=request.POST['age']
            sex=request.POST['sex']
            phone=request.POST['phone']
            address=request.POST['address']
            classname=request.POST['classname']
            students=Student(name=name, age= age,sex= sex,phone= phone,address=address, ClassName= classname)
            students.save()
    except:
        raise Http404('Error Excute!!!')
    finally:
        return HttpResponseRedirect(reverse('index'))
    
