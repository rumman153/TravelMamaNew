"""Travelmama URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static

from AdminManagement import views as admin_views
from ManageVisitor import views as visitor_views
from PostManagement import views as post_views


urlpatterns = [

    path('admin/', admin.site.urls),
    path('contact-us/', admin_views.showAdmin, name='Admin'),
    path('profile/', visitor_views.show_profile, name='showProfile'),
    path('updateprofile/', visitor_views.createProfile, name='createProfile' ),

    path('post/<int:post_id>', post_views.showDetails, name='detail_view'),


    path('review/<int:post_id>', post_views.review_after_complete, name='review'),
    path('post/', post_views.showPost, name='Post'),

    path('my_post/', post_views.index_page, name='posts'),

    path('insertpost/', post_views.insertPost, name='insertPost'),
    path('', post_views.showHome, name='Homepage'),


    path('registration/', visitor_views.registration, name='registration'),
    path('registration/', post_views.registration, name='registration'),
    path('registration/', admin_views.registration, name='registration'),

    path('accounts/', include('django.contrib.auth.urls')),






]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)