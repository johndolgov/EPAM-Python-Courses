from django.shortcuts import render
from django.http import HttpResponse

from music.models import Artist

# Create your views here.

def index(request):

    queryset = Artist.objects.all()

    return render(request, 'index.html', {'artist_list': 'queryset'})
