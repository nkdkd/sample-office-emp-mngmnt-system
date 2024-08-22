from django.db import models

# Create your models here.
class Department(models.Model):
    name=models.CharField(max_length=50,null=False)
    location=models.CharField(max_length=100)
    
    def __str__(self) :
        return self.name
    
class Role(models.Model):
    name=models.CharField(max_length=100)
    def __str__(self) :
        return self.name
    
class Employee(models.Model):
    first_name=models.CharField(max_length=100,null=False)
    last_name=models.CharField(max_length=100,null=False)
    dept=models.ForeignKey(Department,on_delete=models.CASCADE)
    salary=models.IntegerField(default=0)
    bonus=models.IntegerField(default=0)
    role=models.ForeignKey(Role,on_delete=models.CASCADE)
    phone=models.IntegerField(default=0)
    hire_date=models.DateField()
    
    def __str__(self):
        # Return a string that includes all relevant fields
        return (f"{self.first_name} {self.last_name} - Dept: {self.dept} - "
                f"Role: {self.role} - Salary: ${self.salary} - Bonus: ${self.bonus} - "
                f"Phone: {self.phone} - Hire Date: {self.hire_date}")
