from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from .models import Post
from .forms import PostForm

# Create your views here.
def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'MyBlog/post_list.html', {'posts': posts})#request sent to render html post_list

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'MyBlog/post_detail.html', {'post': post})

def post_new(request):

    if request.method == "POST" :
        form = PostForm(request.POST)
        if form.is_valid() :
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk = post.pk)
    else :
        form = PostForm()

    return render(request, 'MyBlog/post_edit.html', {'form': form})

def post_edit(request, pk):
    post = get_object_or_404(Post, pk = pk)
    if request.method == 'POST':
        form = PostForm(request.POST, instance = post)
        if form.is_valid() :
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk = post.pk)
    else :
        form = PostForm(instance = post)
    return render(request, 'MyBlog/post_edit.html', {'form':form})

def draft_post_list(request):
    post = Post.objects.filter(published_date__is_null=True).order_by('created_date')
    return render(request, 'MyBlog/draft_post_list.html', {'post':post})

def post_published(request, pk):
    post = get_object_or_404(post, pk = pk)
    if request.method == 'POST':
        post.publish()
    return redirect('post_detail', pk = pk )

def post_delete(request, pk):
    post = get_object_or_404(pk = post.pk)
    if request.method == 'POST':
        post.delete()
    return redirect('post_detail', pk = post.pk)
