
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, ListView

from autos.forms import autosForm
from .models import autos


class autosListView(ListView):
    model = autos
    context_object_name = 'all_the_autoss'
    template_name = 'autos-list.html'


class autosDetailView(DetailView):
    model = autos
    context_object_name = 'that_one_autos'
    template_name = 'autos-detail.html'


class autosCreateView(CreateView):
    model = autos
    form_class = autosForm
    template_name = 'autos-create.html'
    success_url = reverse_lazy('autos-list')
    print("im in create")

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
