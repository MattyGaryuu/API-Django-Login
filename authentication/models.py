from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

#usuario
class CustomUser(AbstractUser):
    ID = models.AutoField(primary_key=True)
    email = models.CharField(max_length=100)
    pass

#favoritos
class UserFav(models.Model):
    usuario = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    id_manga = models.IntegerField()