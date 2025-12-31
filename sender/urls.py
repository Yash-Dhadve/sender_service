from django.urls import path
from .views import status,receive_ack

urlpatterns = [
    path("status/", status),
    path("api/ack/", receive_ack),
]
