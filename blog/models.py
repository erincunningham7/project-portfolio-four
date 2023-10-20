from django.db import models
# import user model
from django.contrib.auth.models import User
# import cloudinary field for images
from cloudinary.models import CloudinaryField
from django_quill.fields import QuillField

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
    content = QuillField()
    image = CloudinaryField('image', default='placeholder')
    status = models.CharField(
        max_length=6, choices=STATUS_CHOICES, default=DRAFT)
    slug = models.SlugField(max_length=250, unique=True, blank=True, null=True)
    likes = models.ManyToManyField(
        User, related_name='blogpost_like', blank=True)

    # return string representation of title
    def __str__(self):
        return self.title

    def number_of_likes(self):
        return Comment.objects.filter(post=self, approved=True).count()

    # apply descending ordering to posts
    class Meta:
        ordering = ["-date_created"]

    # helper method to return num of likes on a post
    def number_of_likes(self):
        return self.likes.count()


# create a comment class based model inheriting from the standard model


class Comment(models.Model):
    post = models.ForeignKey('BlogPost', on_delete=models.CASCADE)
    author = models.CharField(max_length=100)
    text = models.TextField()
    date_created = models.DateTimeField(auto_now=True)
    approved = models.BooleanField(default=False)
    upvotes = models.IntegerField(default=0)

    def __str__(self):
        return f'Comment by {self.author} on {self.post.title}'

# apply descending ordering to comments
# update later to order by popularity
    class Meta:
        ordering = ["-date_created"]


# class BlogPostLike(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     blog_post = models.ForeignKey('BlogPost', on_delete=models.CASCADE)
#     liked_at = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return f'{self.user.username} likes {self.blog_post.title}'
