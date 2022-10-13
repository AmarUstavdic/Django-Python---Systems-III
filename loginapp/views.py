from django.shortcuts import render

# Create your views here.
from django.http import HttpResponseRedirect
from .forms import UserForm

def register(request):
    # if this is a post then we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request
        form = UserForm(request.POST)
        # check wheter it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL
            return HttpResponseRedirect('registration.html')
    # if a GET (or any other method) we'll create a blank form
    else:
        form = UserForm()

    return render(request, 'registration.html', {'form': form})
