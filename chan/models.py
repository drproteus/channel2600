from django.db import models
from django.contrib import admin

class Board(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=80)
    slug = models.CharField(max_length=15)

    def __str__(self):
        return self.name

class Thread(models.Model):
    board = models.ForeignKey(Board, on_delete=models.CASCADE)
    subject = models.CharField(max_length=80, default="")
    created_at = models.DateTimeField(auto_now_add=True)

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

class Post(models.Model):
    thread = models.ForeignKey(Thread, on_delete=models.CASCADE, related_name="posts")
    body = models.TextField()
    author = models.CharField(max_length=80, default="Anonymous")
    created_at = models.DateTimeField(auto_now_add=True)

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
