from .models import *


def calculate_score(user):
    score = 0
    for task in Task.objects.all():
        if task.owner == user:
            score += task.score
    return score