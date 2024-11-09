from django.shortcuts import render, get_object_or_404
from .models import Post, Comment
from django.urls import reverse
from .forms import PostForm, CommentForm
from django.views import generic

class ListView(generic.ListView):
    model=Post
    template_name='comidas/index.html'

class DetailView(generic.DetailView):
    model=Post
    template_name='comidas/detail.html'

def search_post(request):
    context = {}
    if request.GET.get('query', False):
        search_term = request.GET['query'].lower()
        post_list = Post.objects.filter(titulo__icontains=search_term)
        context = {"post_list": post_list}
    return render(request, 'comidas/search.html', context)

class CreatView(generic.CreateView):
    model= Post
    template_name= 'comidas/create.html'
    form_class=PostForm
    def get_success_url(self):
        return reverse('comidas:detail', args=[self.object.pk])

class UpdateView(generic.UpdateView):
    model= Post
    template_name= 'comidas/update.html'
    form_class=PostForm
    def get_success_url(self):
        return reverse('comidas:detail', args=[self.object.pk])

class DeleteView(generic.DeleteView):
    model=Post
    template_name='comidas/delete.html'
    def get_success_url(self):
        return reverse('comidas:index')

class CommentCreateView(generic.CreateView):
    model = Comment
    form_class = CommentForm
    template_name = 'comidas/comment.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        post_id = self.kwargs['pk']
        #post = Post.objects.get(pk=post_id) get_object_or_404(Post, pk=post_id)
        post = get_object_or_404(Post, pk=post_id)
        context['post'] = post
        return context
    def form_valid(self, form):
        #post = Post.objects.get(pk=self.kwargs['pk'])
        post = get_object_or_404(Post,pk=self.kwargs['pk'])
        form.instance.post = post
        return super().form_valid(form)
    def get_success_url(self):
        post_id = self.kwargs['pk']
        return reverse('comidas:detail', args=[post_id])