from django.db import models


class BlogPost(models.Model):
    title = models.CharField(max_length=120)
    content = models.TextField(null=True, blank=True)
    slug = models.SlugField(unique=True)
