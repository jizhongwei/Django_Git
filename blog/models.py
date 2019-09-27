from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils.html import strip_tags

class Tag(models.Model):
    name = models.CharField(max_length= 100)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length= 100)

    def __str__(self):
        return self.name

class Blog(models.Model):
    CHOICES = (
        ('p', 'published'),
        ('d', 'draft'),
    )
    title = models.CharField(max_length= 100)
    body = models.TextField()
    created_time = models.DateTimeField(auto_now_add= True)
    updated_time = models.DateTimeField(auto_now = True)
    category = models.ForeignKey(Category, on_delete= models.CASCADE)
    tags = models.ManyToManyField(Tag)
    excerpt = models.CharField(max_length= 200, blank= True)
    author = models.ForeignKey(User, on_delete= models.CASCADE)
    status = models.CharField(max_length= 1, choices= CHOICES)
    views = models.PositiveIntegerField(default= 0)

    class Meta:
        ordering = ('-created_time',)

    def __str__(self):
        return self.title

    def save(self, *args,**kwargs):
        if not self.excerpt:
            self.excerpt = strip_tags(self.body)[:50]
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('blog:detail', kwargs= {'pk': self.pk})

    def increase_views(self):
        self.views += 1
        super(Blog, self).save(update_fields= ['views'])