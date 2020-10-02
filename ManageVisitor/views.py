from django.shortcuts import render, redirect, get_object_or_404
from .models import Visitor
from .forms import VisitorForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.template import RequestContext


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
def updateProfile(request):

            visitor_list= Visitor.objects.get(user=request.user)
            if len(visitor_list) != 0:
                visitor = Visitor.objects.get(user=request.user)
                form = VisitorForm(initial={'Visitor_name': visitor.Visitor_name,
                                            'Visitor_email': visitor.Visitor_email,
                                            'Gender': visitor.Gender,
                                            'Visitor_picture': visitor.Visitor_picture,

                                            })
            else:
                visitor = None
                form = VisitorForm()

            if request.method == "POST":
                form = VisitorForm(request.POST, request.FILES)

                if form.is_valid:
                    instance = form.save(commit=False)
                    instance.user = request.user

                    if visitor == None:
                        instance.save()
                    else:
                        visitor.Visitor_email = instance.Visitor_email
                        visitor.Visitor_picture = instance.Visitor_picture
                        visitor.save()

                        return redirect('showProfile')

                    context = {
                        'form': form
                    }
                    return render(request, 'ManageVisitor/updateProfile.html', context=RequestContext(request))

@login_required
def show_profile(request):
    try:
        visitor = Visitor.objects.get(user=request.user)
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

            #return redirect(showProfile)

    context = {
        'form' : form

    }
    return render(request, 'ManageVisitor/registration.html', context)
