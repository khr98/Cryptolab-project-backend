from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _

class User(AbstractUser):
    email = models.EmailField(_("email address"), blank=False, unique=True)
    created_at = models.DateTimeField(auto_now_add=True,null=True)
    REQUIRED_FIELDS = ["email", "password"]

    class Meta:
        db_table = 'User'

class Qrcode(models.Model):
    seqId = models.AutoField(db_column='idQRcode', primary_key=True)  # Field name made lowercase.
    #user = models.ForeignKey('User',models.DO_NOTHING,max_length=45, blank=True, null=True, db_column='user')
    latitude = models.FloatField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)

    class Meta:
       db_table = 'Qrcode'