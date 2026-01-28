from django.urls import path
from .views import status, receive_ack, landing_view

urlpatterns = [
    path("status/", status),
    path("api/ack/", receive_ack),
    path('', landing_view, name='home'),
]
