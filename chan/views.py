from django.shortcuts import render, get_object_or_404, redirect
from django.core.urlresolvers import reverse
from django.core.paginator import Paginator
from django.http import Http404, HttpResponse
from chan.models import *
from chan.forms import *
import cloudinary

def index(request):
    boards = Board.objects.all()
    return render(request, 'index.html', {'title': "Index", 'boards': boards})

def board_index(request, slug, page=1):
    boards = Board.objects.all()
    board = get_object_or_404(Board, slug=slug)
    all_threads = Paginator(board.thread_set.order_by("-sticky", "-updated_at"), 10)
    threads = all_threads.page(page)
    next_page = min(int(page)+1, all_threads.num_pages)
    return render(request, 'board.html', {'title': board.name,
        'boards': boards, 'board': board, 'threads': threads,
        'page': int(page), 'pages': range(1, all_threads.num_pages+1),
        'next_page': next_page})

def thread(request, id):
    boards = Board.objects.all()
    thread = get_object_or_404(Thread, id=id)
    board = thread.board
    posts = thread.posts.order_by("id")
    if request.method == 'GET':
        form = PostForm(initial={'author': "Anonymous"})
    else:
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            author = form.cleaned_data['author']
            image = ""
            if request.FILES.get('image'):
                upload_response = cloudinary.uploader.upload(request.FILES['image'])
                image = upload_response['public_id']
            new_post = Post.objects.create(author=author, body=body, image=image, thread=thread)
            return redirect('/thread/{}/'.format(thread.id))
    return render(request, 'thread.html', {
        'title': thread.board.name,
        'board': board,
        'boards': boards,
        'thread': thread,
        'posts': posts,
        'form': form
        })

def new_thread(request, slug):
    boards = Board.objects.all()
    board = get_object_or_404(Board, slug=slug)
    if request.method == 'GET':
        form = ThreadForm(initial={'author': "Anonymous"})
    else:
        form = ThreadForm(request.POST, request.FILES)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            author = form.cleaned_data['author']
            body, replies = process_replies(form.cleaned_data['body'])
            image = filename = ""
            height = width = filesize = 0
            if request.FILES.get('image'):
                upload_response = cloudinary.uploader.upload(request.FILES['image'])
                image = upload_response['public_id']
                filename = request.FILES['image'].name
                height = upload_response['height']
                width = upload_response['width']
                filesize = upload_response['bytes'] / 1024.0
            new_thread = Thread.objects.create(subject=subject, board=board)
            new_post = Post.objects.create(id=new_thread.id, author=author, body=body, image=image, thread=new_thread,
                    filename=filename, height=height, width=width, filesize=filesize)
            for reply in replies:
                Reply.objects.create(parent_post=reply, post=new_post)
            return redirect('/thread/{}/#{}'.format(new_thread.id, new_thread.id))
    return render(request, 'new_thread.html', {
        'form': form,
        'boards': boards,
        'board': board,
        'title': board.name
        })

def reply(request, id):
    boards = Board.objects.all()
    thread = get_object_or_404(Thread, id=id)
    board = thread.board
    if request.method == 'GET':
        return redirect('/thread/{}/'.format(thread.id))
    else:
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            if thread.locked:
                raise ValidationError, "Thread is locked. You cannot reply."
            author = form.cleaned_data['author']
            body, replies = process_replies(form.cleaned_data['body'])
            image = filename = ""
            height = width = filesize = 0
            if request.FILES.get('image'):
                upload_response = cloudinary.uploader.upload(request.FILES['image'])
                image = upload_response['public_id']
                filename = request.FILES['image'].name
                height = upload_response['height']
                width = upload_response['width']
                filesize = upload_response['bytes'] / 1024.0
            new_post = Post.objects.create(author=author, body=body, image=image, thread=thread,
                    filename=filename, height=height, width=width, filesize=filesize)
            thread.save()
            for reply in replies:
                Reply.objects.create(parent_post=reply, post=new_post)
            return redirect('/thread/{}/#{}'.format(thread.id, new_post.id))
    return render(request, 'thread.html', {
        'form': form,
        'thread': thread,
        'boards': boards,
        'board': board,
        'title': board.name
        })

def process_replies(body):
    lines = body.split("\n")
    replies = []
    for i in range(len(lines)):
        if lines[i][:1] == ">":
            try:
                if Post.objects.filter(id=lines[i][2:]).count() > 0:
                    post_id = lines[i][2:].strip()
                    post = Post.objects.get(id=post_id)
                    lines[i] = ">[>>{}](/thread/{}/#{})\n".format(post_id, post.thread.id, post_id)
                    replies.append(post)
                else:
                    lines[i] = ">{}\n".format(lines[i].replace('>', '\>'))
            except:
                lines[i] = ">{}\n".format(lines[i].replace('>', '\>'))
    return "\n".join(lines), replies

def full_thread(request, id):
    thread = get_object_or_404(Thread, id=id)
    board = thread.board
    posts = thread.preview_inverse()
    return render(request, 'thread-embed.html', {
        'thread': thread,
        'board': board,
        'posts': posts
        })

def post_body(request, id):
    post = get_object_or_404(Post, id=id)
    return render(request, 'post-body.html', {'post': post})
