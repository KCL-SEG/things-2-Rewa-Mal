from django.shortcuts import render, redirect
from .forms import ThingForm

def home(request):
    if request.method == 'POST':
        form = ThingForm(request.POST)
        if form.is_valid():
            return redirect('home')
    else:
        form = ThingForm()

    return render(request, 'home.html', {'form': form})

