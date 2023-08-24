from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Post
from .forms import PostForm


def get_posts(request):
    posts = Post.objects.all()
    template = "modernmb/posts.html"
    context = {
        "posts": posts,
    }
    return render(request, template, context)


def view_post(request, id):
    post = get_object_or_404(Post, id=id)
    template = "modernmb/post_details.html"
    context = {
        "post": post,
    }
    return render(request, template, context)


@login_required
def add_post(request):
    form = PostForm(request.Post or None)
    if request.method == "Post":
        if form.is_valid():
            form.instance.user = request.user
            form.save()
            messages.success(request, "Post added")
            return redirect(reverse("posts"))
        messages.error(request, "Error, Try again.")

    template = "modernmb/add_post.html"
    context = {
        "form": form,
    }
    return render(request, template, context)


@login_required
def update_post(request, id):
    post = get_object_or_404(Post, id=id)
    form = PostForm(request.Post or None, instance=post)
    if request.method == "Post":
        if form.is_valid():
            form.instance.user = request.user
            form.save()
            messages.success(request, "Post updated")
            return redirect(reverse("posts"))
        messages.error(request, "Error, Try again.")

    template = "modernmb/update_post.html"
    context = {
        "form": form,
        "post": post,
    }
    return render(request, template, context)


@login_required
def delete_post(request, id):
    post = get_object_or_404(Post, id=id)
    messages.success(request, "Post deleted")
    post.delete()       
    return redirect(reverse("posts"))