from django.shortcuts import render, get_object_or_404
from django.http import Http404, HttpResponse
from chan.models import *

def index(request):
    boards = Board.objects.all()
    return render(request, 'index.html', {'title': "Index", 'boards': boards})

def board_index(request, slug):
    board = get_object_or_404(Board, slug=slug)
    return HttpResponse(board.name)
