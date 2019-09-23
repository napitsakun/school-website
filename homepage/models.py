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


class Aboutus(models.Model):
    feature_image = models.FileField(upload_to='about/')
    about_title = models.CharField(max_length=200)
    about_description = models.TextField()

    def __str__(self):
        return self.about_title


class Events(models.Model):
    event_title = models.CharField(max_length=200)
    event_description = models.TextField(default='')
    event_image = models.FileField(upload_to='events')
    event_date_time = models.DateTimeField(auto_now_add=True)

    class Meta():
        ordering = ['-event_date_time']

    def __str__(self):
        return self.event_title


class Notices(models.Model):
    notice_title = models.CharField(max_length=200, default='')
    notice_description = models.TextField(max_length=600, default='')
    notice_date_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering= ['-notice_date_time']

    def __str__(self):
        return self.notice_title