from django.core.management.base import NoArgsCommand
from chan.models import Post

# Sets the is_op boolean on each model if the thread id and post id match.
class Command(NoArgsCommand):
    def handle_noargs(self, **options):
        for post in Post.objects.all():
            if post.id == post.thread.id:
                post.is_op = True
                post.save(update_fields=['is_op'])
