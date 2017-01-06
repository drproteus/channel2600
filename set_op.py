from chan.models import Post

# Sets the is_op boolean on each model if the thread id and post id match.
for post in Post.objects.all():
    if post.id == post.thread.id:
        post.is_op = True
        post.save(update_fields['is_op']
