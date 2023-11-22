from django.urls import path
from eTicket import views

urlpatterns = [
    path("", views.bookticket, name="bookticket"),   
]