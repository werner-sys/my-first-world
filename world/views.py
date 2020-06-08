from world.models import Post
from django.utils import timezone
from django.shortcuts import render, get_object_or_404
from .forms import PostForm
from django.shortcuts import redirect


def post_list(request):
    var = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'world/post_list.html', {'var' : var})

def post_detail(request, ok):
    det = get_object_or_404(Post, pk=ok)
    return render(request, 'world/post_detail.html', {'det': det})

def post_new(request):
            if request.method == "POST":
                form = PostForm(request.POST)
                if form.is_valid():
                    post = form.save(commit=False)
                    post.author = request.user
                    post.published_date = timezone.now()
                    post.save()
                    det = Post.objects.get(pk=post.pk)
                    return render(request, 'world/post_detail.html', {'det': det})
            else:
                form = PostForm()
            return render(request, 'world/post_edit.html', {'form': form})

def post_edit(request, pk):
        post = get_object_or_404(Post, pk=pk)
        if request.method == "POST":
            form = PostForm(request.POST, instance=post)
            if form.is_valid():
                post = form.save(commit=False)
                post.author = request.user
                post.save()
                det = Post.objects.get(pk=post.pk)
                return render(request, 'world/post_detail.html', {'det': det})
        else:
            form = PostForm(instance=post)
        return render(request, 'world/post_edit.html', {'form': form})
   
