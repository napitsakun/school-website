from django.shortcuts import render, HttpResponse, redirect
from django.core.paginator import Paginator
from django.contrib.auth import authenticate, login, logout

from .models import Slider, Contact, Testimonial, Aboutus, Events, Notices
from .forms import EventForm, NoticeForm, TestimonialForm

# Create your views here.


# view for homepage rendering
def home(request):
    slider_list = Slider.objects.all()
    contact_list = Contact.objects.all()
    testimonial_list = Testimonial.objects.all()
    home_dict = {'contact': contact_list[0],
                 'slider_list_first': slider_list[0],
                 'slider_list': slider_list[1:],
                 'testimonial_list_first': testimonial_list[0],
                 'testimonial_list': testimonial_list[1:]
                 }
    return render(request, 'homepage/homepage.html', home_dict)


# view for about us page
def aboutus(request):
    aboutus = Aboutus.objects.all()
    contact_list = Contact.objects.all()
    aboutus_dict = {'about': aboutus[0], 'contact': contact_list[0]}
    return render(request, 'homepage/aboutus.html', aboutus_dict)


# view for event page
def events(request):
    event_list = Events.objects.all()
    contact_list = Contact.objects.all()
    paginator = Paginator(event_list, 6)
    page = request.GET.get('page')
    event_list_filter = paginator.get_page(page)
    event_dict = {'event_list_filter': event_list_filter, 'contact': contact_list[0]}
    return render(request, 'homepage/events.html', event_dict)

def detail(request, event_id):
    contact_list = Contact.objects.all()
    detail_list = Events.objects.get(pk=event_id)
    detail_dict = {'contact': contact_list[0], 'detail': detail_list}
    return render(request, 'homepage/details.html', detail_dict)


# view for notice page
def notices(request):
    contact_list = Contact.objects.all()
    notice_list = Notices.objects.all()
    paginator = Paginator(notice_list, 4)
    page = request.GET.get('page')
    notice_list_filter = paginator.get_page(page)
    notice_dict = {'notice_list_filter': notice_list_filter, 'contact': contact_list[0]}
    return render(request, 'homepage/notices.html', notice_dict)


# user login and validation
def user_login(request):
    if request.user.is_authenticated:
        return render(request, "homepage/dashboard.html")
    if request.method == 'POST':
        username = request.POST['email-address']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return render(request, "homepage/dashboard.html")
        else:
            return render(request, 'homepage/login_error.html')
    else:
        return render(request, 'homepage/login.html')


# user logout process
def user_logout(request):
    logout(request)
    return render(request, 'homepage/logout.html')


# add an event after logging in
def add_event(request):
    form = EventForm(request.POST, request.FILES)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('/login/')
        else:
            return HttpResponse("<h2> There seems to be problem with adding data. Please Try Again</h1>")
    else:
        form = EventForm()

    return render(request, 'homepage/add_event.html', {'form': form})


# add a notice after logging in
def add_notice(request):
    form = NoticeForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('/login/')
        else:
            return HttpResponse("<h2> There seems to be problem with adding data. Please Try Again</h1>")
    else:
        form = NoticeForm()

    return render(request, 'homepage/add_notice.html', {'form': form})


# view to update selected event (event is selected on the basis of id)
def update_event(request):
    event_list = Events.objects.all()
    return render(request, 'homepage/update_event.html', {'event_list': event_list})


# view to update selected notice (notice is selected on the basis of id)
def update_notice(request):
    notice_list = Notices.objects.all()
    return render(request, 'homepage/update_notice.html', {'notice_list': notice_list})


# confirm whether the user wants to delete the data
def delete_notice(request, notice_id):
    notice = Notices.objects.get(pk=notice_id)
    return render(request, 'homepage/confirm_delete.html', {'notice': notice})


# view to delete selected notice (notice is selected on the basis of id)
def confirm_delete_notice(request, notice_id):
    notice_to_delete = Notices.objects.filter(pk=notice_id)
    if request.method == 'POST':
        notice_to_delete.delete()
        return redirect('/dashboard/updatenotice/')

    notice_list = Notices.objects.all()
    return render(request, 'homepage/update_notice.html', {'notice_list': notice_list})


# confirm whether the user wants to delete the data
def delete_event(request, event_id):
    event = Events.objects.get(pk=event_id)
    return render(request, 'homepage/confirm_delete_event.html', {'event': event})


# view to update selected event (event is selected on the basis of id)
def confirm_delete_event(request, event_id):
    event_to_delete = Events.objects.filter(pk=event_id)
    if request.method == 'POST':
        event_to_delete.delete()
        event_list = Events.objects.all()
        return redirect('/dashboard/updateevent/')

    event_list = Events.objects.all()
    return render(request, 'homepage/update_event.html', {'event_list': event_list})


# view to edit selected event (event is selected on the basis of id)
def edit_event(request, event_id):
    event = Events.objects.get(pk=event_id)
    if request.method == 'POST':
        form = EventForm(instance=event, data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/dashboard/updateevent/')
    else:
        form = EventForm(instance=event)

    return render(request, 'homepage/edit_event.html', {'event': event, 'form': form})


# view to edit selected notice (notice is selected on the basis of id)
def edit_notice(request, notice_id):
    notice = Notices.objects.get(pk=notice_id)
    if request.method == 'POST':
        form = NoticeForm(instance=notice, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('/dashboard/updatenotice/')
    else:
        form = NoticeForm(instance=notice)

    return render(request, 'homepage/edit_notice.html', {'notice': notice, 'form': form})


# to show the detail of selected notice
def detail_notice(request, notice_id):
    detail = Notices.objects.get(pk=notice_id)
    return render(request, 'homepage/detail_notice.html', {'detail': detail})


# to show the detail of selected event
def detail_event(request, event_id):
    detail = Events.objects.get(pk=event_id)
    return render(request, 'homepage/detail_event.html', {'detail': detail})


# add a testimonial
def add_testimonial(request):
    form = TestimonialForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('/login/')
        else:
            return HttpResponse("<h2> There seems to be problem with adding data. Please Try Again</h1>")
    else:
        form = TestimonialForm()
    return render(request, 'homepage/add_testimonial.html', {'form': form})