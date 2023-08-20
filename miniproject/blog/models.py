from django.db import models
from django.utils.text import slugify
from django_quill.fields import QuillField
from django.utils.crypto import get_random_string

class Category(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name

class Blog(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=200, blank=True)
    content = QuillField()
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='articles/')
    slug = models.SlugField(max_length=150, unique=True, blank=True, null=True)
    published = models.BooleanField(default=True)
    
    class Meta:
        ordering = ['-created_at']

    def save(self, *args, **kwargs):
        unique_slug = self.title + " " + get_random_string(length=5)
        self.slug = slugify(unique_slug)
        super(Blog, self).save(*args, **kwargs)

    def __str__(self):
        return self.title
    
    