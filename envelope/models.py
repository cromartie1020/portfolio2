from django.db import models
from datetime import datetime 
class Employee(models.Model):
    TITLE=(
        ('Mr.','Mr.'),
        ('Miss.','Miss'),
        ('',''),
    )

    job_title=models.CharField(max_length=75,null=True,blank=True)
    company_name=models.CharField(max_length=100,null=True,blank=True)
    title=models.CharField(max_length=6,choices=TITLE,default='',null=True)
    first_name=models.CharField(max_length=100,blank=True,null=True)
    last_name=models.CharField(max_length=100,null=True,blank=True)
    address=models.CharField(max_length=150,null=True,blank=True)
    address1=models.CharField(max_length=150,null=True,blank=True)
    address2=models.CharField(max_length=150,null=True,blank=True)
    city=models.CharField(max_length=75,null=True,blank=True)
    state=models.CharField(max_length=20,null=True,blank=True)
    zip_code=models.CharField(max_length=30,null=True,blank=True)
    date_updated=models.DateTimeField(auto_now=datetime.now, null=True)
    date_created = models.DateTimeField(auto_now_add=True,null=True)

    def __str__(self):
        return f"{self.title} {self.first_name} {self.last_name}"


    
    