from . import views
from django.urls import path

urlpatterns = [
    path('', views.events, name='events'),
    path('<event_id>/', views.detail, name='detail'),
]