from django.shortcuts import redirect, render, get_object_or_404
from django.views.generic import DetailView, ListView, UpdateView, CreateView, DeleteView
from .models import Post, Category, Comment
from .forms import PostForm, EditForm, CommentForm
from django.urls import reverse, reverse_lazy
from django.http import HttpResponseRedirect

# Create your views here.
class PostListView(ListView):
    model = Post
    template_name = 'home.html'
    ordering = ['-publish']

    def get_context_data(self, *args, **kwargs):
        category_menu = Category.objects.all()
        context = super(PostListView, self).get_context_data(*args, **kwargs)
        context["category_menu"] = category_menu
        return context


class PostDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'

    def post(self, request, *args, **kwargs):
        form = CommentForm(request.POST)
        if form.is_valid():
            post = self.get_object()
            form.instsnce.user = request.user
            form.instsnce.post = post
            form.save()
            return redirect(reverse('post', kwargs={post.pk}))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = self.form
        return context

    def get_context_data(self, *args, **kwargs):
        category_menu = Category.objects.all()
        post_list = Post.objects.all()
        context = super(PostDetailView, self).get_context_data(*args, **kwargs)
        
        # Get total likes and render to page
        all_likes = get_object_or_404(Post, id=self.kwargs['pk'])
        total_likes = all_likes.total_likes()

        liked = False
        if all_likes.likes.filter(id=self.request.user.id).exists():
            liked = True

        context["category_menu"] = category_menu
        context["post_list"] = post_list
        context["total_likes"] = total_likes
        context["liked"] = liked
        return context

class PostCreateView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'post_create.html'

class AddCommentView(CreateView):
    model = Comment
    # form_class = PostForm
    template_name = 'add_comment.html'
    fields = "__all__"


class PostUpdateView(UpdateView):
    model = Post
    form_class = EditForm
    template_name = 'post_update.html'


class PostDeleteView(DeleteView):
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('home')


# Function based views for categories
def CategoryView(request, cats):
    category_menu = Category.objects.all()
    post_list = Post.objects.all()
    post_category = Post.objects.filter(category=cats)

    return render(request, 'categories.html', {'cats':cats.title(), 'post_category':post_category, 'category_menu':category_menu, 'post_list':post_list} )


def LikeView(request, pk):
    post = get_object_or_404(Post, id=request.POST.get('post_id'))
    liked = False
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
        liked = False
    else:
        post.likes.add(request.user)
        liked = True
   
    return HttpResponseRedirect(reverse('post_detail', args=[str(pk)]))

# def CommentView(request):
#     if request.method == 'POST' in request.POST: 
#         form = CommentForm()
#     else:
#         form = CommentForm()
#     context = {'form':form}
#     return render(request, 'blog/post_detail.html', context)