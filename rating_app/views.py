from django.contrib.auth.decorators import login_required
from django.shortcuts import render, HttpResponseRedirect, HttpResponse
from django.urls import reverse
from .decorators import rate_film_required

from .models import Movie
from .forms import CreateForm
from .utils import get_films_data, get_film_by_id, FILM
from typing import Generator, Union


# Create your views here.
def start_page(request) -> HttpResponse:
    return render(request, 'index.html')


@login_required(login_url='users:login_page')
def show_rating(request) -> HttpResponse | HttpResponseRedirect:
    if request.POST.get('film'):
        movie_id: int = int(request.POST['film'])
        new_rating: float = float(request.POST['new_rating'])
        Movie.objects.filter(pk=movie_id).update(rating=new_rating)
        return HttpResponseRedirect(reverse('movies:rating_page'))
    else:
        order_generator: Generator = request.GET.items()
        order_type: Union[str, float] = 'title'
        for item in order_generator:
            order_type = item[0]
        user: str = request.user
        movies = Movie.objects.filter(movie_user=user).order_by(order_type)
    return render(request, 'marks.html', {'movies': movies})


@login_required(login_url='users:login_page')
def create_rating(request) -> HttpResponse:
    if request.POST.get('title'):
        title: str = request.POST['title']
        rating: str = request.POST['rating']
        return HttpResponseRedirect(reverse('movies:choose_page') + f'?title={title}&rating={rating}')
    form = CreateForm()
    return render(request, 'create_mark.html', {'form': form})


@rate_film_required
@login_required(login_url='users:login_page')
def choose_movie(request) -> HttpResponse:
    if request.POST.get('film'):
        movie_id: int = int(request.POST.get('film'))
        movie_data: FILM = get_film_by_id(movie_id)
        user: str = request.user
        rating: float = float(request.POST.get('rating'))
        query = Movie(title=movie_data.ru_name, year=movie_data.year, link=movie_data.kp_url,
                      kp_rating=movie_data.kp_rate,
                      rating=rating, movie_user=user)
        query.save()
        return HttpResponseRedirect(reverse('index_page'))
    else:
        rating: str = request.GET.get('rating')
        title: str = request.GET.get('title')
        films_data: list = get_films_data(title)
    return render(request, 'choose_movie.html', {'films_data': films_data,
                                                 'rating': rating})
