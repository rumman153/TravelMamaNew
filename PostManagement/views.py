from django.shortcuts import render, get_object_or_404, redirect, HttpResponseRedirect
from .models import Post,Review
from .forms import PostForm, ReviewForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse
from django.contrib.auth.models import User



def showPost(request):
    postList = Post.objects.all()

    if request.method == 'POST':
        postList = Post.objects.filter(Post_title__icontains=request.POST['search'])
        postTags = Post.objects.filter(Post_tags__icontains=request.POST['search'])
        postcatagory =Post.objects.filter(Post_catagory__icontains=request.POST['search'])

        postList = postList | postTags |  postcatagory # C = A U B set operation

    context = {
        'Post': postList
    }
    return render(request, 'PostManagement/PostList.html', context)

@login_required
def showDetails(request, post_id):
    searched_post = get_object_or_404(Post, id=post_id)

    form = ReviewForm()

    if request.method == "POST":
        form = ReviewForm(request.POST)


        if form.is_valid:
            instance = form.save(commit=False)
            print(request.user)
            instance.User = request.user
            instance.save()

            searched_post.reviews.add(instance)
            searched_post.save()

    context = {
        'search': searched_post,
        'form': form
    }

    return render(request, 'PostManagement/detail_post_view.html', context)

# def showDetails(request, post_id):
#
#     searched_post = get_object_or_404(Post, id=post_id)
#     context = {
#         'search': searched_post
#     }
#     return render(request, 'PostManagement/detail_post_view.html', context)



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


def showHome(request):
    # postList = Post.objects.all()
    # context = {
    #     'Post': postList
    # }
    return render(request, 'PostManagement/homepage.html')


@login_required
def review_after_complete(request, post_id):

    already_reviewed = False

    searched_post = get_object_or_404(Post, id=post_id)

    user_list = searched_post.reviews.filter(user=request.user)
    print(user_list, len(user_list))
    if len(user_list) != 0:
        already_reviewed = True


    form = ReviewForm()

    if request.method == "POST":
        form = ReviewForm(request.POST)

        if form.is_valid:
            instance = form.save(commit=False)
            instance.user = request.user
            instance.save()

            searched_post.reviews.add(instance)
            searched_post.save()

            return redirect('Post')

    context = {
        'search': searched_post,
        'form': form,
        # 'already_reviewed': already_reviewed
    }
    return render(request, 'PostManagement/detail_post_view_review.html', context)


