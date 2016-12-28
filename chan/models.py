from django.db import models
from django.contrib import admin
from cloudinary.models import CloudinaryField

class Board(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=80)
    slug = models.CharField(max_length=15)

    def __str__(self):
        return self.name

class Thread(models.Model):
    board = models.ForeignKey(Board, on_delete=models.CASCADE)
    subject = models.CharField(max_length=80, default="")
    locked = models.BooleanField(default=False)
    sticky = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        next_id = max(Thread.last_id(), Post.last_id()) + 1
        self.id = next_id
        super(Thread, self).save(*args, **kwargs)
        
    def preview_posts(self):
        posts = []
        posts.append(self.posts.first())
        all_posts = self.posts.all()
        post_count = self.posts.count()
        if post_count < 6:
            posts.extend(all_posts[1:])
        else:
            posts.extend(all_posts[post_count-5:])
        return posts

    def __str__(self):
        return self.subject

    @classmethod
    def last_id(klass):
        if not klass.objects.last():
            return 0
        else:
            return klass.objects.last().id

class Post(models.Model):
    thread = models.ForeignKey(Thread, on_delete=models.CASCADE, related_name="posts")
    body = models.TextField(blank=True)
    author = models.CharField(max_length=80, default="Anonymous")
    image = models.CharField(max_length=200, blank=True)
    filename = models.CharField(max_length=200, blank=True)
    width = models.IntegerField(default=0, blank=True)
    height = models.IntegerField(default=0, blank=True)
    filesize = models.DecimalField(default=0, decimal_places=1, max_digits=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.id:
            next_id = max(Thread.last_id(), Post.last_id()) + 1
            self.id = next_id
        super(Post, self).save(*args, **kwargs)

    @classmethod
    def last_id(klass):
        if not klass.objects.last():
            return 0
        else:
            return klass.objects.last().id

class Reply(models.Model):
    parent_post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="replies")
    post = models.ForeignKey(Post, related_name="post_reply")
    created_at = models.DateTimeField(auto_now_add=True)

class Ban(models.Model):
    pass

admin.site.register(Board)
admin.site.register(Thread)
admin.site.register(Post)
admin.site.register(Reply)
