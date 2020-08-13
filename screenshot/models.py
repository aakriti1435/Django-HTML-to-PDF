from django.db import models

# Create your models here.


class digi_sign(models.Model):
    digital_sign = models.ImageField( upload_to='images/',null=True, height_field=None, width_field=None, max_length=None)