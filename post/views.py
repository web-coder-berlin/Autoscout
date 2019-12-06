
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, ListView

from post.forms import postForm
from .models import post


class postListView(ListView):
    model = post
    context_object_name = 'all_the_posts'
    template_name = 'post-list.html'


class postDetailView(DetailView):
    model = post
    context_object_name = 'that_one_post'
    template_name = 'post-detail.html'


class postCreateView(CreateView):
    model = post
    form_class = postForm
    template_name = 'post-create.html'
    success_url = reverse_lazy('post-list')
    print("im in create")

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
