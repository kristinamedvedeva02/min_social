from django.db import models


class Task(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    owner = models.ForeignKey('users.User', on_delete=models.CASCADE)

    def __str__(self):  
        return self.name
    

    
