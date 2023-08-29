from django import forms
from .models import Category, Post

# Form for naming categories
class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ('name', )

# Form for naming posts
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'category', 'content', )
