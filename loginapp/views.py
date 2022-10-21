from django.contrib.auth import authenticate
from django.shortcuts import render

# Create your views here.
from django.http import HttpResponseRedirect
from .forms import UserCreationForm


def register(request):
    # if this is a post then we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request
        form = UserCreationForm(request.POST)
        # check wheter it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            form.save()
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            user = authenticate(username=username, email=email)
            return render(request, 'test.html', {'username': username})

            # return HttpResponseRedirect('registration.html')
    # if a GET (or any other method) we'll create a blank form
    else:
        form = UserCreationForm()

    return render(request, 'registration.html', {'form': form})
