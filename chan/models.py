from django.db import models

class Board(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=80)
    slug = models.CharField(max_length=15)

class Thread(models.Model):
    board = models.ForeignKey(Board, on_delete=models.CASCADE)

class Post(models.Model):
    thread = models.ForeignKey(Thread, on_delete=models.CASCADE)
    body = models.TextField()

class Reply(models.Model):
    parent_post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="replies")
    post = models.ForeignKey(Post, related_name="post_reply")

class Ban(models.Model):
    pass
