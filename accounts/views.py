from django.shortcuts import render, redirect
from django.contrib.auth import login

#Ajax login
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import CreateView

#return a JSON
from django.contrib.auth.models import User
from django.http import JsonResponse

#Locals
from .forms import SignUpForm


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('add')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})



"""Now I will practice a ajax requests from
 https://simpleisbetterthancomplex.com/tutorial/2016/08/29/how-to-work-with-ajax-request-with-django.html"""
class SignUpView(CreateView):
    """Creating sighup View"""
    template_name = 'ajax/signup.html'
    form_class = UserCreationForm


def validate_username(request):
    """Create function to parse request, take username and return JSONresponce"""
    username = request.GET.get('username', None)
    data = {
        'is_taken':User.objects.filter(username__iexact = username).exists()
    }
    if data['is_taken']:
        data['error_message'] = 'A user with this username already exists.'
    return JsonResponse(data)
