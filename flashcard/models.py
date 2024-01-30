from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name
    
class Flashcard(models.Model):
    DIFFICULTY_CHOICES = (('H', 'Hard'), ('N', 'Normal'), ('E', 'Easy'))
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    question = models.CharField(max_length=100)
    answer = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING)
    difficulty = models.CharField(max_length=1, choices=DIFFICULTY_CHOICES)
    
    def __str__(self):
        return self.question
