from django.db import models
from django.db.models import permalink
from django.utils import timezone

#
# class Post(models.Model):
#     author = models.ForeignKey('auth.User')
#     title = models.CharField(max_length=200)
#     text = models.TextField()
#     created_date = models.DateTimeField(
#             default=timezone.now)
#     published_date = models.DateTimeField(
#             blank=True, null=True)
#
#     def publish(self):
#         self.published_date = timezone.now()
#         self.save()
#
#     def __str__(self):
#         return self.title

class Blog(models.Model):
    title = models.CharField(max_length=200, unique=True)
    body = models.TextField()
    posted = models.DateField(db_index=True,auto_now_add=True)
    slug = models.SlugField(max_length=200, unique=True)
    category = models.ForeignKey('blog.category')

    @property
    def __unicode__(self):
        return '%s' % self.title

    @permalink
    def get_absolute_url(self):
        return ('view_blog_post', None, { 'slug': self.slug })

class Category(models.Model):
    title = models.CharField(max_length=200,unique=True, db_index=True)
    slug = models.SlugField(max_length=200, unique=True, db_index=True)

    def __unicode__(self):
        return '%s' % self.title

    @permalink
    def get_absolute_url(self):
        return ('view_blog_category', None, { 'slug': self.slug })

