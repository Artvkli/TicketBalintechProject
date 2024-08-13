from django.shortcuts import render , redirect
from .forms import TicketForm 

def send_ticket(request):
    if request.method == 'POST':
        form = TicketForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home : home')
    else:
        form = TicketForm()
        
    return render (request, 'ticket_app/sendTicket.html', {'form' : form })

