from django.shortcuts import render
from .models import Events
from homepage.models import Contact

from django.core.paginator import Paginator

# Create your views here.

def events(request):
    event_list = Events.objects.all()
    contact_list = Contact.objects.all()
    paginator = Paginator(event_list, 6)
    page = request.GET.get('page')
    event_list_filter = paginator.get_page(page)
    event_dict = {'event_list_filter': event_list_filter, 'contact': contact_list[0]}
    return render(request, 'events/events.html', event_dict)


def detail(request, event_id):
    contact_list = Contact.objects.all()
    detail_list = Events.objects.get(pk=event_id)
    detail_dict = {'contact': contact_list[0], 'detail': detail_list}
    return render(request, 'events/details.html', detail_dict)