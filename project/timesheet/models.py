from django.db import models

SENDING_FREQUENCY = (('W', 'Weekly'),
                     ('D', 'Daily'),
                     ('M', 'Monthly'),
                     ('O', 'On Signal?'))
# Create your models here.
class Report(models.Model):
    content_template = models.TextField(max_length=2000)
    sending_frequence = models.CharField(max_length=1, choices=SENDING_FREQUENCY)
