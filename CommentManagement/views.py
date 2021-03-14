from django.shortcuts import render
from .models import Comment
from .forms import CommentForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm



def showComment(request):
    commentList = Comment.objects.all()
    context = {
        'Comment': commentList
    }
    return render(request, 'CommentManagement/CommentList.html', context)

def registration(request):
    form = UserCreationForm()

    if request.method == 'POST':
        form = UserCreationForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()

    context = {
        'form' : form

    }
    return render(request, 'CommentManagement/registration.html', context)

@login_required
def insertComment(request):
    message = ""
    form = CommentForm()

    if request.method == "POST":
        form = CommentForm(request.POST,request.FILES)
        message = "you are wrong!!!!!"
        if form.is_valid():
            form.save()
            message = "Comment added Successfully,Thanks."
            form = CommentForm()

    context = {
        'form' : form,
        'message' : message
    }
    return render(request,'CommentManagement/insertComment.html', context)
