from django.db import models
# import user model
from django.contrib.auth.models import User
# import cloudinary field for images
from cloudinary.models import CloudinaryField

# create blog post class based model inheriting from standard model


class BlogPost(models.Model):

    # define a BlogPost model with a status field that can have one of two
    # choices: 'Draft' or 'Posted'
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
    # likes = models.ManyToManyField(User, related_name='post_likes', blank=True)
    likes = models.IntegerField(default=0)

    # return string representation of title
    def __str__(self):
        return self.title

    # apply descending ordering to posts
    class Meta:
        ordering = ["-date_created"]

    # helper method to return num of likes on a post
    # def number_of_likes(self):
    #    return self.likes.count()
    def get_likes(self):
        return self.likes

# create a comment class based model inheriting from the standard model


class Comment(models.Model):
    post = models.ForeignKey('BlogPost', on_delete=models.CASCADE)
    author = models.CharField(max_length=100)
    text = models.TextField()
    date_created = models.DateTimeField(auto_now=True)
    approved = models.BooleanField(default=False)

    def __str__(self):
        return f'Comment by {self.author} on {self.post.title}'


# apply descending ordering to comments
# update later to order by popularity


    class Meta:
        ordering = ["-date_created"]

