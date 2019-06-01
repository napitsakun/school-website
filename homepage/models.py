from django.db import models

# Create your models here.

class Slider(models.Model):
    image = models.FileField(upload_to='home-slider/')
    title = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.title


class Contact(models.Model):
    header_logo = models.FileField(upload_to='logo/')
    footer_logo = models.FileField(upload_to='logo/')
    slogan = models.CharField(max_length=200, blank=True)
    address = models.CharField(max_length=100, blank=False)
    email = models.EmailField(max_length=200)
    phone_number = models.CharField(max_length=30)

    def __str__(self):
        return self.address


class Testimonial(models.Model):
    testimonial_reviewer = models.CharField(max_length=100)
    testimonial_comment = models.TextField()

    def __str__(self):
        return self.testimonial_reviewer