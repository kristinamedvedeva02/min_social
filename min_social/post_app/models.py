from django.db import models
from django.core.exceptions import ValidationError

class Company(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(max_length=200, blank=True)
    
    class Meta:
        verbose_name = 'Company'
        verbose_name_plural = 'Companies'

    def __str__(self):
        return self.name


class Office(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(max_length=200, blank=True)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Office'
        verbose_name_plural = 'Offices'

    def __str__(self):
        return self.name
    

class Team(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=200, blank=True)
    office = models.ForeignKey(Office, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Team'
        verbose_name_plural = 'Teams'

    def __str__(self):
        return self.name
    


class Uniqate(models.Model):
    name = models.CharField()
    branch = models.ForeignKey(Office, on_delete=models.CASCADE)
    
    def clean(self):
       super().clean()
       
       if Uniqate.objects.filter(name=self.name, office__company=self.office.company).exists():
          raise ValidationError('Error message')
 
    def save(self, *args, **kwargs):
       # Forces the clean method to be called
       self.full_clean()
       super().save(*args, **kwargs)