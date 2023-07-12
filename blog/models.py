from django.db import models
from django.core.validators import MinLengthValidator

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=150)
    excerpt = models.CharField(max_length=200, blank=True)
    content = models.TextField(validators=[MinLengthValidator(10)])
    date = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to="posts", null=True)
    slug = models.SlugField(max_length=100, unique=True)
    author = models.ForeignKey('Author', on_delete=models.SET_NULL, null=True, related_name='posts')
    tags = models.ManyToManyField('Tag', related_name='posts')

    def __str__(self) -> str:
        return self.title


class Author(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email_address = models.EmailField()

    def full_name(self):
        return f'{self.first_name} {self.last_name}'

    def __str__(self):
        return self.full_name()
    

class Tag(models.Model):
    caption = models.CharField(max_length=20)

    def __str__(self):
        return self.caption
    

class Comment(models.Model):
    user_name = models.CharField(max_length=30)
    user_email = models.EmailField()
    text = models.TextField(max_length=400)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")