from django import forms
from .models import Visitor

class VisitorForm(forms.ModelForm):
    class Meta:
        model = Visitor
        fields = ('Visitor_name','Visitor_email','Gender','Visitor_picture')