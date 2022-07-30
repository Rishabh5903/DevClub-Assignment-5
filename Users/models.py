from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class user(models.Model):
    Instructor=models.ForeignKey(User, on_delete=models.CASCADE)
    Student=models.ForeignKey(User, on_delete=models.CASCADE)
    Course = models.fields.CharField(max_length=6)
    admin=models.ForeignKey(User, on_delete=models.CASCADE)