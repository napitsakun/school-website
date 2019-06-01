from django.shortcuts import render
from .models import Aboutus
from homepage.models import Contact
# Create your views here.

def aboutus(request):
    aboutus = Aboutus.objects.all()
    contact_list = Contact.objects.all()
    aboutus_dict = {'about': aboutus[0], 'contact': contact_list[0]}
    return render(request, 'aboutus/aboutus.html', aboutus_dict)