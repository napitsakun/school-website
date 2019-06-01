from django.db import models

# Create your models here.

class Events(models.Model):
    event_title = models.CharField(max_length=200)
    event_description = models.TextField(default='')
    event_image = models.FileField(upload_to='events')
    event_date_time = models.DateTimeField(auto_now_add=True)

    class Meta():
        ordering = ['-event_date_time']

    def __str__(self):
        return self.event_title