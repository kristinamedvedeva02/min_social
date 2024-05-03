from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Task(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    owner = models.ForeignKey('users.User', on_delete=models.CASCADE)


class TaskScore(models.Model):
    task_id = models.ForeignKey(Task, on_delete=models.CASCADE)
    user_id = models.ManyToManyField('users.User', default = None)
    team_id = models.ManyToManyField('post_app.Team', default = None)
    end_score = models.IntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(100)])




# class TaskScore(models.Model):
#     task = models.ForeignKey(Task, on_delete=models.CASCADE)
#     user = models.ForeignKey('users.User', on_delete=models.CASCADE, default = None)
#     score = models.IntegerField(default=0, min_value=0, max_value = 100, default = 0)

#     def save(self, *args, **kwargs):
#         super().save(*args, **kwargs)   

#     def clean(self):
#         super().clean()

#         if TaskScore.objects.filter(task=self.task, user=self.user).exists():
#             raise ValidationError('Error message')


#     def __str__(self):  
#         return self.name
    

    
