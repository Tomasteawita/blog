from django import forms
from django.forms import ModelForm
from ckeditor.widgets import CKEditorWidget
from .models import *

class PostForm(ModelForm):

    class Meta:
        model = Post
        fields = '__all__'

        widgets = {
            'tags':forms.CheckboxSelectMultiple(),
            'body': CKEditorWidget(config_name='default'),
        }