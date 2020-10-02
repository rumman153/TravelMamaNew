from django.shortcuts import render
from .models import Post
from .forms import PostForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm


def showPost(request):
    postList = Post.objects.all()
    context = {
        'Post': postList
    }
    return render(request, 'PostManagement/PostList.html', context)

def registration(request):
    form = UserCreationForm()

    if request.method == 'POST':
        form = UserCreationForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()

    context = {
        'form' : form

    }
    return render(request, 'PostManagement/registration.html', context)

@login_required
def insertPost(request):
    message = ""
    form = PostForm()

    if request.method == "POST":
        form = PostForm(request.POST,request.FILES)
        message = "Invalid Post Input!!!!!"
        if form.is_valid():
            post = form.save(commit=False)
            post.User = request.user
            post.save()

            message = "Post submitted successfully"
            form = PostForm()

    context = {
        'form' : form,
        'message' : message
    }
    return render(request,'PostManagement/insertPost.html', context)
