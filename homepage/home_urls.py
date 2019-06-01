from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),

    path('dashboard/addevent/', views.add_event, name='add_event'),
    path('dashboard/addnotice/', views.add_notice, name='add_notice'),

    path('dashboard/updateevent/', views.update_event, name='update_event'),
    path('dashboard/updatenotice/', views.update_notice, name='update_notice'),

    path('dashboard/deleteevent/<event_id>/', views.delete_event, name='delete_event'),
    path('dashboard/deletenotice/<notice_id>/', views.delete_notice, name='delete_notice'),

    path('dashboard/deletenotice/con/<notice_id>/', views.confirm_delete_notice, name='confirm_delete_notice'),
    path('dashboard/deleteevent/con/<event_id>/', views.confirm_delete_event, name='confirm_delete_event'),


    path('dashboard/editevent/<event_id>/', views.edit_event, name='delete_event'),
    path('dashboard/editnotice/<notice_id>/', views.edit_notice, name='delete_notice'),

    path('dashboard/updatenotice/notice/<notice_id>/', views.detail_notice, name='detail_notice'),
    path('dashboard/updateevent/event/<event_id>/', views.detail_event, name='detail_event'),

    path('dashboard/addtestimonial/', views.add_testimonial, name='add_testimonial'),
]