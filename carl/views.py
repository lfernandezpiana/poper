from django.shortcuts import render


# Create your views here.

from carl.models import Comediante

def index(request):
    """View function for home page of site."""
    poperos = Comediante.objects.all()

    # Number of visits to this view, as counted in the session variable.
    num_visits=request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits+1

    context = {
        'poperos_nombre': poperos[2].nombre,
        'poperos_apellido': poperos[2].apellido,
        'poperos_especialidad': poperos[2].especialidad,
        'poperos_bio': poperos[2].bio,
        'num_visits': num_visits,
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)


from django.views import generic
from django.views.generic import ListView

class ComedianteList(ListView):
    model = Comediante
    template_name = 'integrantes/comediante_list.html'
    content_object_name = "comediante_list"
