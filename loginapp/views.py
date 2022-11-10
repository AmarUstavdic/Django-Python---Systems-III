from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from django.shortcuts import render

# Create your views here.
from django.http import HttpResponseRedirect
from .forms import CustomUserCreationForm, CustomUserChangeForm


def register(request):
    if request.method == 'POST':
        # create a form instance and populate it with data from the request
        form = CustomUserCreationForm(request.POST)
        # check wheter it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            form.save()
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            user = authenticate(username=username, email=email)

            return render(request, 'test.html', {'username': username})

    # if a GET (or any other method) we'll create a blank form
    else:
        form = CustomUserChangeForm()

    return render(request, 'registration.html', {'form': form})



def home_view(request):

    return render(request, 'home.html')


@login_required()
def profile_view(request):

    return render(request, 'registration/renderme.html')

