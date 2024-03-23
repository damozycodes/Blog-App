from django.shortcuts import render
from .models import Post
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
    ListView, 
  DetailView, 
   UpdateView, 
    CreateView,
    DeleteView,
)
from django.urls import reverse, reverse_lazy


def home(request):
    context = {"posts": Post.objects.all()}
    return render(request, "blog/home.html", context,)


class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 10


class PostDetailView(DetailView):
    model = Post


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ["title", "content"]

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ["title", "content"]

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if post.author == self.request.user:
            return True
        return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = reverse_lazy('blog_home')

    def get_success_url(self):
        return reverse('blog_home')

    def test_func(self):
        post = self.get_object()
        if post.author == self.request.user:
            return True
        return False


def about(request):
    return render(request, "blog/about.html", {'title': 'About'})
