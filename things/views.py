from django.shortcuts import render, redirect
from .forms import thing_form

def home(request):
    if request.method == 'POST':
        form = thing_form(request.POST)
        if form.is_valid():
            return redirect('home')
    else:
        form = thing_form()

    return render(request, 'home.html', {'form': form})

