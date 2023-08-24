from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


class Category(models.Model):
    name = models.CharField(max_length=25, unique=True)
    category = forms.ModelChoiceField(queryset=Category.objects.all(), empty_label="(Nothing)")

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=200)

    category = models.ForeignKey(Category, on_delete=SET_NULL)

    def __str__(self):
        return self.title
