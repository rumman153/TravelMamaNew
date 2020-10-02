from django.shortcuts import render, redirect, get_object_or_404
from .models import Visitor
from .forms import VisitorForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm


@login_required
def createProfile(request):
   message = ""
   form = VisitorForm()

   if request.method == "POST":
       form = VisitorForm(request.POST, request.FILES)
       message = "Invalid input. Please try again!"
       if form.is_valid():

           Visitor = form.save(commit=False)

           Visitor.user = request.user

           Visitor.save()

           message = "Profile is created!"
           form = VisitorForm()

   context = {
       'form' : form,
       'message' : message
   }
   return render(request, 'ManageVisitor/createProfile.html', context)


@login_required
def show_profile(request):
    global Visitor
    try:
        visitor = Visitor.objects.filter(user=request.user)
    except Visitor.DoesNotExist:
        visitor = "Please complete your profile to view"

    context = {
        'Visitor': visitor
    }

    return render(request, 'ManageVisitor/showProfile.html', context)

def registration(request):
    form = UserCreationForm()

    if request.method == 'POST':
        form = UserCreationForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()

    context = {
        'form' : form

    }
    return render(request, 'ManageVisitor/registration.html', context)
