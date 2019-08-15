from django.views import generic
from .models import Post
from .forms import PostForm
from django.shortcuts import render, redirect

class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'community/index.html'

class PostDetail(generic.DetailView):
    model = Post
    template_name = 'community/post_detail.html'

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()

    else:
        form = PostForm()
    return render(request, 'community/post_edit.html', {'form': form})