from dataclasses import fields
from django import forms
from .models import Category, Post, Comments


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ['user', 'views_number']


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ['content']
        widgets = {
            'text': forms.Textarea(attrs={'class': 'form-control', 'rows': '3'}),
        }


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'
        