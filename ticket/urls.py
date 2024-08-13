from django.urls import path
from . import views

app_name = 'ticket'

urlpatterns = [
    path ('ticket/',views.send_ticket, name='ticket'),   
]



