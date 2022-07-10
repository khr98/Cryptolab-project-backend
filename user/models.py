from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    email = models.EmailField(verbose_name="email_address", blank=False, unique=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        db_table = 'User'

class Qrcode(models.Model):
    seqId = models.AutoField(db_column='idQRcode', primary_key=True)  # Field name made lowercase.
    user = models.ForeignKey('User',models.DO_NOTHING,blank=True, null=True, db_column='user')
    latitude = models.FloatField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)

    class Meta:
       db_table = 'Qrcode'