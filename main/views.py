from django.shortcuts import render
from .models import Reservoirs
from django.shortcuts import redirect
from .forms import ReservoirsForm
from .utils import get_reservoirs
from .models import ChemistryData
reservoirs = Reservoirs.objects.all()

def index(req):
    first_reservoir_title = reservoirs[0].title
    redirect_url = f"/{first_reservoir_title}"
    return redirect(redirect_url)

def nura(req, name):
    reservoirs = Reservoirs.objects.all()
    reserv_list = get_reservoirs(reservoirs)

    if name in reserv_list:
        reserv_current = reserv_list[name]
    else:
        reserv_current = False

    sort_order = req.GET.get('sort_order', 'asc') 
    filter = req.GET.get('filter', "") 

    data = {
        'reserv_current': reserv_current,
        'name': name,
        'reservoirs': reservoirs,
        'sort_order': sort_order,
        'filter': filter
    }
    return render(req, "main/nura.html", data)

def newReservoirs(req):
    if req.method == "POST":
        form = ReservoirsForm(req.POST)
        if form.is_valid():
            form.save()
            
            return redirect("/")
        else:
            print("Form errors:")
    form = ReservoirsForm()
    reservoirs = Reservoirs.objects.all()
    data = {
        "form": form,
        'reservoirs': reservoirs
    }
    return render(req, "main/new.html", data)

