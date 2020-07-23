from django.views.generic import CreateView, UpdateView
from .models import Person
from .forms import PersonForm



class PersonCreateView(CreateView):
    model = Person
    fields = ('name', 'email', 'job_title', 'bio')


class PersonUpdateView(UpdateView):
    model = Person
    form_class = PersonForm
    template_name = 'people/person_update_form.html'