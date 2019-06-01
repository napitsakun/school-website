from django.db import models

# Create your models here.

class Aboutus(models.Model):
    feature_image = models.FileField(upload_to='about/')
    about_title = models.CharField(max_length=200)
    about_description = models.TextField()

    def __str__(self):
        return self.about_title