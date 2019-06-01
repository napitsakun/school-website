from django.shortcuts import render
from .models import Notices
from homepage.models import Contact

from django.core.paginator import Paginator

# Create your views here.

def notices(request):
    contact_list = Contact.objects.all()
    notice_list = Notices.objects.all()
    paginator = Paginator(notice_list, 4)
    page = request.GET.get('page')
    notice_list_filter = paginator.get_page(page)
    notice_dict = {'notice_list_filter': notice_list_filter, 'contact': contact_list[0]}
    return render(request, 'notices/notices.html', notice_dict)