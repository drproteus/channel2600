from django.shortcuts import render, get_object_or_404, redirect
from django.core.urlresolvers import reverse
from django.http import Http404, HttpResponse
from chan.models import *
from chan.forms import *
import cloudinary

def index(request):
    boards = Board.objects.all()
    return render(request, 'index.html', {'title': "Index", 'boards': boards})

def board_index(request, slug):
    boards = Board.objects.all()
    board = get_object_or_404(Board, slug=slug)
    threads = board.thread_set.order_by("-id")
    return render(request, 'board.html', {'title': board.name,
        'boards': boards, 'board': board, 'threads': threads})

def thread(request, id):
    boards = Board.objects.all()
    thread = get_object_or_404(Thread, id=id)
    board = thread.board
    posts = thread.posts.all()
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
            image = ""
            if request.FILES.get('image'):
                upload_response = cloudinary.uploader.upload(request.FILES['image'])
                image = upload_response['public_id']
            new_thread = Thread.objects.create(subject=subject, board=board)
            new_post = Post.objects.create(author=author, body=body, 
                    image=image, thread=new_thread, id=new_thread.id)
            for reply in replies:
                Reply.objects.create(parent_post=new_post, post=reply)
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
        form = PostForm(initial={'author': "Anonymous"})
    else:
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            author = form.cleaned_data['author']
            body, replies = process_replies(form.cleaned_data['body'])
            image = ""
            if request.FILES.get('image'):
                upload_response = cloudinary.uploader.upload(request.FILES['image'])
                image = upload_response['public_id']
            new_post = Post.objects.create(author=author, body=body, image=image, thread=thread)
            for reply in replies:
                Reply.objects.create(parent_post=new_post, post=reply)
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
        if lines[i][0] == ">":
            try:
                if Post.objects.filter(id=lines[i][2:]).count() > 0:
                    post_id = lines[i][2:].strip()
                    post = Post.objects.get(id=post_id)
                    lines[i] = ">[>>{}](/thread/{}/#{})\n".format(post_id, post.thread.id, post_id)
                    replies.append(post)
                else:
                    lines[i] = ">\>\>{}".format(lines[i][2:])
            except:
                lines[i] = ">\>\>{}".format(lines[i][2:])
        lines[i] += "\n"
    return "\n".join(lines), replies
