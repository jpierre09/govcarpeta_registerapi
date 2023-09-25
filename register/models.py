from django.db import models

# Create your models here.

class UserRegister(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=100)
    email = models.EmailField()
    operatorId = models.IntegerField()
    operatorName = models.CharField(max_length=30)

    class Meta:
        db_table = 'userRegister'
        