from django.shortcuts import render,get_object_or_404
from employee.models import employee
# Create your views here.
def employee_details(request,pk):
    employees = get_object_or_404(employee,pk=pk)
    context = {
        'employee': employees
    }
    return render(request,'employee_details.html',context)