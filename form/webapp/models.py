from django.db import models

class registration(models.Model):
    first_name=models.CharField(max_length=50,null=True)
    last_name=models.CharField(max_length=50,null=True)
    gender=models.CharField(max_length=10,null=True)
    phone=models.CharField(max_length=15,null=True)
    email=models.CharField(max_length=50,null=True)
    birthday=models.DateField(null=True)
    address=models.TextField(max_length=250,null=True)
    file=models.FileField(null=True)
    state=models.CharField(max_length=15,null=True)
    service=models.CharField(max_length=100,null=True)
    
    
    
