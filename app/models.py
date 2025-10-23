from django.db import models

class MonTruc(models.Model):
    name = models.CharField(max_length=200)
    path = models.FileField(upload_to='trucs/')