from django.shortcuts import render 
from employee.models import employee

def home(request):
    employees = employee.objects.all()
    context = {
        'employee': employees
    }
    return render(request,'index.html',context)