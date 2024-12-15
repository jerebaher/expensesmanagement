from django.shortcuts import render, redirect
from forms import TransactionForm

def home(request):

    context = {
        "whatis": "Es un diccionario de python que se envía dentro de la funcion render para acceder a sus valores desde la plantilla"
    }
    return render(request, "home/index.html", context)

def create_transaction(request):
    if request.mehotd == 'POST':
        form = TransactionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_gastos')
    else:
        form = TransactionForm()
    return render(request, 'templates/home/transaction_created.html', {'form': form})
