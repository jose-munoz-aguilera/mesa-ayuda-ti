from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render

from .forms import TicketForm
from .models import Ticket


@login_required
def lista(request):
    tickets = Ticket.objects.filter(creado_por=request.user)
    return render(request, 'tickets/lista.html', {'tickets': tickets})


@login_required
def detalle(request, pk):
    ticket = get_object_or_404(Ticket, pk=pk, creado_por=request.user)
    return render(request, 'tickets/detalle.html', {'ticket': ticket})


@login_required
def crear(request):
    if request.method == 'POST':
        form = TicketForm(request.POST)
        if form.is_valid():
            ticket = form.save(commit=False)
            ticket.creado_por = request.user
            ticket.save()
            return redirect('tickets:lista')
    else:
        form = TicketForm()
    return render(request, 'tickets/crear.html', {'form': form})