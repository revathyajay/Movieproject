from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Movie
from .form import MovieForm


# Create your views here.
def index(request):
    movie = Movie.objects.all()
    context = {'movie_list': movie}
    return render(request, 'index.html', context)


def detail(request, id):
    movie1 = Movie.objects.get(id=id)
    return render(request, 'detail.html', {'movie': movie1})


def add_movie(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        desc = request.POST.get('desc')
        year = request.POST.get('year')
        img = request.FILES['img']
        # name = request.POST['name']
        # desc = request.POST['desc']
        # year = request.POST['year']
        # img = request.FILES['img']
        movie = Movie(name=name, desc=desc, year=year, img=img)
        movie.save()

    return render(request, 'add.html')


def update(request, id):
    movie = Movie.objects.get(id=id)
    form = MovieForm(request.POST or None, request.FILES, instance=movie)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request, 'edit.html', {'form': form, 'movie': movie})


def delete(request, id):
    if request.method == 'POST':
        movie = Movie.objects.get(id=id)
        movie.delete()
        return redirect('/')
    return render(request, 'delete.html')
