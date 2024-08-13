from django.urls import path
from ticket.views import send_ticket

app_name = 'ticket'

urlpatterns = [
    path ('ticket/',send_ticket, name='ticket'),   
]



