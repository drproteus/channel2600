from django.shortcuts import render, get_object_or_404, redirect
from django.core.urlresolvers import reverse
from django.http import Http404, HttpResponse
from chan.models import *
from chan.forms import *

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
    return render(request, 'thread.html', {
        'title': thread.board.name,
        'board': board,
        'boards': boards,
        'thread': thread,
        'posts': posts
        })

def new_thread(request, slug):
    boards = Board.objects.all()
    board = get_object_or_404(Board, slug=slug)
    if request.method == 'GET':
        form = ThreadForm(initial={'author': "Anonymous"})
    else:
        form = ThreadForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            author = form.cleaned_data['author']
            body = form.cleaned_data['body']
            new_thread = Thread.objects.create(subject=subject, board=board)
            new_post = Post.objects.create(author=author, body=body, thread=new_thread, id=new_thread.id)
            return redirect('/thread/{}/'.format(new_thread.id))
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
        form = PostForm(request.POST)
        if form.is_valid():
            author = form.cleaned_data['author']
            body = form.cleaned_data['body']
            new_post = Post.objects.create(author=author, body=body, thread=thread)
            return redirect('/thread/{}/'.format(thread.id))
    return render(request, 'reply.html', {
        'form': form,
        'thread': thread,
        'boards': boards,
        'board': board,
        'title': board.name
        })

