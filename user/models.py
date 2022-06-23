from django.db import models

# Create your models here.
class User(models.Model):
    seqId = models.AutoField(db_column='idUser', primary_key=True)  # Field name made lowercase.
    email = models.CharField(max_length=45, db_column='email')
    password = models.CharField(max_length=300,db_column='password')

    class Meta:
        managed = False
        db_table = 'User'

class Qrcode(models.Model):
    seqId = models.AutoField(db_column='idQRcode', primary_key=True)  # Field name made lowercase.
    user = models.ForeignKey('User',models.DO_NOTHING,max_length=45, blank=True, null=True, db_column='user')
    latitude = models.CharField(max_length=45, blank=True, null=True)
    longitude = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'QRcode'