from django import forms
from .models import Post,Review

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('Post_title','Post_location','Post_catagory','Post_tags','Post_image','Post_description')


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ('rating', 'comment')


