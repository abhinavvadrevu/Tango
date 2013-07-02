from django.db import models

class Test(models.Model):
    question = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')