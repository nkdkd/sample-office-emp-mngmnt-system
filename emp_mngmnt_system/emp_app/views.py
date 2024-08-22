from django.shortcuts import render,HttpResponse,get_object_or_404
from .models import Employee,Department,Role
from django.db.models import Q
# Create your views here.
def index(request):
    return render(request,'index.html')

def remove_emp(request, emp_id=0):
    if emp_id:
        try:
            emp_id_to_remove=Employee.objects.get(id=emp_id)
            print(emp_id_to_remove)
            emp_id_to_remove.delete()
            
            return HttpResponse("Employee removed successfully !! ")
        except:
            return HttpResponse("plz select a valid id ")
    emps=Employee.objects.all()
    context={
        'emps':emps
    }
    
    return render(request,'remove_emp.html',context)



def add_emp(request):
    if request.method == "POST":
        # Extract POST data
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        salary = request.POST.get('salary')
        dept_id = request.POST.get('dept')
        role_id = request.POST.get('role')
        phone = request.POST.get('phone')
        bonus = request.POST.get('bonus')
        hire_date = request.POST.get('hire_date')

        # # Debugging output
        # print(f"Received POST data: {request.POST}")

        # Validate numeric fields
        try:
            salary = int(salary)
            dept_id = int(dept_id)
            role_id = int(role_id)
            phone = int(phone)
            bonus = int(bonus)
        except (ValueError, TypeError) as e:
            print(f"Conversion error: {e}")
            return HttpResponse("Invalid input for numeric fields.", status=400)

        # Fetch related model instances
        department = get_object_or_404(Department, id=dept_id)
        role = get_object_or_404(Role, id=role_id)

        # Create and save new Employee instance
        new_emp = Employee(
            first_name=first_name,last_name=last_name,salary=salary,dept=department,role=role, phone=phone,
            bonus=bonus,
            hire_date=hire_date
        )
        new_emp.save()

        return HttpResponse("Employee added successfully!")

    elif request.method == "GET":
        departments = Department.objects.all()
        roles = Role.objects.all()
        return render(request, 'add_emp.html', {
            'departments': departments,
            'roles': roles,
        })

    else:
        return HttpResponse("Unknown error", status=400)

def all_emp(request):
    emp=Employee.objects.all()
    context={
        'emp':emp
    }
    
    return render(request,'list_all_emp.html',context)

from django.shortcuts import render
from django.db.models import Q
from .models import Employee, Department, Role

def filter_emp(request):
    if request.method == 'POST':
        name = request.POST['name']
        dept = request.POST['dept']
        role = request.POST['role']
        emps = Employee.objects.all()
        if name:
            emps = emps.filter(Q(first_name__icontains = name) | Q(last_name__icontains = name))
            print(emps)
        if dept:
            emps = emps.filter(dept__name__icontains = dept)
        if role:
            emps = emps.filter(role__name__icontains = role)

        context = {
            'emps': emps
        }
        return render(request, 'list_all_emp.html', context)

    elif request.method == 'GET':
        return render(request, 'filter_emp.html')
    else:
        return HttpResponse('An Exception Occurred')
