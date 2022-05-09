from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
class BaseModel(models.Model):
    main_id = models.AutoField(primary_key=True)
    datetime = models.DateTimeField(auto_now_add=True)

class Shift(BaseModel):
    shiftname = models.CharField(max_length=20)
    shiftcode = models.CharField(max_length=4)
    starttime = models.TimeField()
    endtime = models.TimeField()

    def __str__(self):
        return f"{self.shiftcode} {self.shiftname}"

class DepartmentType(BaseModel):
    department_type = models.CharField(max_length=30)
    
    def __str__(self):
        return f"{self.department_type}"

class Department(BaseModel):
    departmentname = models.CharField(max_length=30)
    deaprtmentnumber = models.IntegerField()
    deaprtmenttype = models.ForeignKey(DepartmentType, on_delete=models.DO_NOTHING)

    def __str__(self):
        return f"{self.departmentname}"

class User(AbstractUser):
    empnumber = models.IntegerField(default=None, null=True)
    userdepartment = models.ForeignKey(Department, on_delete=models.DO_NOTHING, default=None, null=True)
    contactnumber = models.IntegerField(default=None, null=True)
    choices = (("1", "Admin"), ("2", "Supervisor"), ("3", "Expert"), ("4", "Operator"))
    usertype = models.CharField(choices=choices, max_length=12, default=1)

    def __str__(self):
        return self.username

class Admin(BaseModel):
    user_designation = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user_designation}"

class Supervisor(BaseModel):
    user_designation = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user_designation}"

class Expert(BaseModel):
    user_designation = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user_designation}"

class Operator(BaseModel):
    user_designation = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user_designation}"

class Operation(BaseModel):
    operationname = models.CharField(max_length=30)
    operationdepartment = models.ForeignKey(Department, on_delete=models.DO_NOTHING)

    def __str__(self):
        return f"{self.operationname}"

class Machine(BaseModel):
    machinename = models.CharField(max_length=30)
    machinenumber = models.IntegerField(unique=True)
    machinedescription = models.TextField()
    machineoperation = models.ForeignKey(Operation, on_delete=models.DO_NOTHING)

    def __str__(self):
        return f"{self.machinenumber}"


@receiver(post_save,sender=User)
def create_user_profile(sender,instance,created,**kwargs):
    if created:
        if instance.usertype==1:
            Admin.objects.create(user_designation=instance)
        if instance.usertype==2:
            Supervisor.objects.create(user_designation=instance)
        if instance.usertype==3:
            Expert.objects.create(user_designation=instance)
        if instance.usertype==4:
            Operator.objects.create(user_designation=instance)

@receiver(post_save,sender=User)
def save_user_profile(sender,instance,**kwargs):
    if instance.usertype==1:
        instance.admin.save()
    if instance.usertype==2:
        instance.supervisor.save()
    if instance.usertype==3:
        instance.expert.save()
    if instance.usertype==3:
        instance.operator.save()