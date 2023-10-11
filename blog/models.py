from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


class BlogPost(models.Model):
    DRAFT = 'draft'
    POSTED = 'posted'

    STATUS_CHOICES = (
        (DRAFT, 'Draft'),
        (POSTED, 'Posted'),
    )

    title = models.CharField(max_length=250, unique=True)
    date_created = models.DateTimeField(auto_now=True)
    content = models.TextField()
    image = CloudinaryField('image', default='placeholder')
    status = models.CharField(
        max_length=6, choices=STATUS_CHOICES, default=DRAFT)
    likes = models.ManyToManyField(User, related_name='likes', blank=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ["-created_on"]

    def number_of_likes(self):
        return self.likes.count()
