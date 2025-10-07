from django.shortcuts import render

# Create your views here.
from django.shortcuts import get_object_or_404, redirect
from .models import Movie
from .forms import MovieForm

def movie_list(request):
    q = request.GET.get('q', '')
    movies = Movie.objects.all()
    if q:
        movies = movies.filter(MovieTitle__icontains=q)
    return render(request, 'movies/movie_list.html', {'movies': movies, 'q': q})

def movie_create(request):
    if request.method == "POST":
        form = MovieForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('movie_list')
    else:
        form = MovieForm()
    return render(request, 'movies/movie_form.html', {'form': form})

def movie_update(request, pk):
    movie = get_object_or_404(Movie, pk=pk)
    if request.method == "POST":
        form = MovieForm(request.POST, instance=movie)
        if form.is_valid():
            form.save()
            return redirect('movie_list')
    else:
        form = MovieForm(instance=movie)
    return render(request, 'movies/movie_form.html', {'form': form, 'movie': movie})

def movie_delete(request, pk):
    movie = get_object_or_404(Movie, pk=pk)
    if request.method == "POST":
        movie.delete()
        return redirect('movie_list')
    return render(request, 'movies/movie_confirm_delete.html', {'movie': movie})
