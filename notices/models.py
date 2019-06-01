from django.db import models

# Create your models here.

class Notices(models.Model):
    notice_title = models.CharField(max_length=200, default='')
    notice_description = models.TextField(max_length=600, default='')
    notice_date_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering= ['-notice_date_time']

    def __str__(self):
        return self.notice_title