from django.shortcuts import render
from .models import Movies
from django.core.paginator import Paginator
# Create your views here.


def movie_list(request):
    movie_object = Movies.objects.all()
    movie_name = request.GET.get('movie_name')
    if movie_name != '' and movie_name is not None:
        movie_object = Movies.objects.filter(name_icontains=movie_name)
    paginator = Paginator(movie_object, 4)
    page = request.GET.get('page')
    movie_object = paginator.get_page(page)
    return render(request, 'reviews/movietemplate.html', {'movie_object': movie_object})

