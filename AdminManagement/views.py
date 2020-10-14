from django.shortcuts import render
from .models import Admin
from django.contrib.auth.forms import UserCreationForm



def showAdmin(request):
    adminList = Admin.objects.all()
    context = {
        'Admin': adminList
    }
    return render(request, 'AdminManagement/AdminList.html', context)
def registration(request):
    form = UserCreationForm()
    msg = ""
    if request.method == 'POST':
        form = UserCreationForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            msg = "Account created successfully!!"
    context = {
        'form' : form,
        'msg' : msg
    }
    return render(request, 'AdminManagement/registration.html', context)




