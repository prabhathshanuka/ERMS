from django.db import models
from django.urls import reverse
from account.models import Account

# Create your models here.
class student (models.Model):
    index_no        = models.CharField(max_length=15,unique=True)
    email           = models.EmailField(verbose_name="email", max_length=60, unique=True)
    first_name      = models.CharField(max_length=60)
    last_name       = models.CharField(max_length=60)
    phone_number    = models.CharField(max_length=60)

    def __str__(self):
        return str(self.index_no)
    def get_absolute_url(self):
        return reverse('home')

class subject (models.Model):
    index_no        = models.ForeignKey(student, to_field='index_no',on_delete = models.CASCADE)
    subject_code    = models.CharField(max_length=60)
    subject_name    = models.CharField(max_length=60)
    marks           = models.IntegerField(default=0)
    attendance      = models.IntegerField(default=0)
    

    class Meta:
        unique_together = (('index_no', 'subject_code'),)

    def __str__(self):
        return str(self.index_no)
    def get_absolute_url(self):
        return reverse('add_subjects')
    
	
       
 
