from django.shortcuts import render, get_object_or_404
from django.http import Http404, HttpResponse
from chan.models import *

def index(request):
    boards = Board.objects.all()
    return render(request, 'index.html', {'title': "Index", 'boards': boards})

def board_index(request, slug):
    boards = Board.objects.all()
    board = get_object_or_404(Board, slug=slug)
    threads = board.thread_set.all()
    return render(request, 'board.html', {'title': board.name,
        'boards': boards, 'board': board, 'threads': threads})

def thread(request, id):
    boards = Board.objects.all()
    thread = get_object_or_404(Thread, id=id)
    posts = thread.posts.all()
    return render(request, 'thread.html', {
        'title': thread.board.name,
        'boards': boards,
        'thread': thread,
        'posts': posts
        })

