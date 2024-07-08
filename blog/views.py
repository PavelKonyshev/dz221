from django.urls import reverse_lazy, reverse

from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from pytils.translit import slugify

from .models import Article


class ArticleCreateView(CreateView):
    model = Article
    fields = ('title', 'content', 'preview', 'created_at', 'published',)
    success_url = reverse_lazy('blog:blog_list')

    def form_valid(self, form):
        if form.is_valid():
            new_art = form.save()
            new_art.slug = slugify(new_art.title)
            new_art.save()
        return super().form_valid(form)


class ArticleUpdateView(UpdateView):
    model = Article
    fields = ('title', 'content', 'preview', 'created_at', 'published', 'number_views',)
    success_url = reverse_lazy('blog:blog_list')

    def form_valid(self, form):
        if form.is_valid():
            new_art = form.save()
            new_art.slug = slugify(new_art.title)
            new_art.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('blog:blog_detail', args=[self.kwargs.get('pk')])


class ArticleListView(ListView):
    model = Article

    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset(*args, **kwargs)
        queryset = queryset.filter(published=True)
        return queryset

class ArticleDetailView(DetailView):
    model = Article

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.number_views += 1
        self.object.save()
        return self.object


class ArticleDeleteView(DeleteView):
    model = Article
    success_url = reverse_lazy('blog:blog_list')
