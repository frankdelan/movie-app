from django.contrib.auth.decorators import login_required
from django.shortcuts import render, HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.db import transaction
from .models import Wish
from .forms import AddForm
from rating_app.models import Movie
from rating_app.decorators import rate_film_required
from rating_app.utils import get_film_by_id, FILM, get_films_data, filter_movie


# Create your views here.
@login_required(login_url='users:login_page')
def show_wishlist(request) -> HttpResponse | HttpResponseRedirect:
    if request.POST.get('film'):
        kp_id: int = int(request.POST['film'])
        rating: float = float(request.POST['rating'])
        film: FILM = get_film_by_id(kp_id)

        with transaction.atomic():
            Wish.objects.filter(kp_id=kp_id).delete()
            Movie.objects.create(title=film.ru_name, year=film.year, link=film.year, kp_rating=film.kp_rate,
                                 rating=rating, movie_user=request.user)

        return HttpResponseRedirect(reverse('wishlists:list_page'))
    else:
        order_type: str = filter_movie(request)
        movies = Wish.objects.filter(wish_user=request.user).order_by(order_type)
    return render(request, 'wishlist_app/wishlist.html', {'movies': movies})


@login_required(login_url='users:login_page')
def add_movie(request) -> HttpResponse:
    if request.POST.get('title'):
        title: str = request.POST['title']
        return HttpResponseRedirect(reverse('wishlists:choose_page') + f'?title={title}')
    form = AddForm()
    return render(request, 'wishlist_app/add_movie.html', {'form': form})


@rate_film_required
@login_required(login_url='users:login_page')
def choose_movie(request) -> HttpResponse:
    if request.POST.get('film'):
        movie_id: int = int(request.POST.get('film'))
        movie_data: FILM = get_film_by_id(movie_id)
        user: str = request.user

        Wish.objects.create(kp_id=movie_id, poster=movie_data.poster_preview, title=movie_data.ru_name,
                            year=movie_data.year, link=movie_data.kp_url, kp_rating=movie_data.kp_rate, wish_user=user)
        return HttpResponseRedirect(reverse('index_page'))
    else:
        title: str = request.GET.get('title')
        films_data: list = get_films_data(title)
    return render(request, 'wishlist_app/select_movie.html', {'films_data': films_data})
