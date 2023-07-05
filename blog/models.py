from django.db import models
from django.core.validators import MinLengthValidator

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=150)
    excerpt = models.CharField(max_length=200, blank=True)
    content = models.TextField(validators=[MinLengthValidator(10)])
    date = models.DateTimeField(auto_now=True)
    image_name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True)


class Author(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField()

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
    

class Tag(models.Model):
    caption = models.CharField(max_length=20)

    def __str__(self):
        return self.caption