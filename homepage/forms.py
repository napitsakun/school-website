from django import forms
from .models import Events, Notices
from .models import Testimonial

class EventForm(forms.ModelForm):
    class Meta:
        model = Events
        fields = ['event_title', 'event_description', 'event_image',]


class NoticeForm(forms.ModelForm):
    class Meta:
        model = Notices
        fields = ['notice_title', 'notice_description',]


class TestimonialForm(forms.ModelForm):
    class Meta:
        model = Testimonial
        fields = ['testimonial_reviewer', 'testimonial_comment',]