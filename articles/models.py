from django.db import models

# Create your models here.
class Question(models.Model):
    title = models.CharField(max_length=50)
    content = models.CharField(max_length=100)
    user = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)

class Answer(models.Model):
    content = models.CharField(max_length=100)
    # CASCADE: 폭포같은 느낌, question이 사라지면 그에 따른 값들이 다 지워진다.
    question = models.ForeignKey(Question, on_delete=models.CASCADE)