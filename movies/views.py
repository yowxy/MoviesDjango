from django.http import HttpResponse
from django.shortcuts import render


data = {
    'movies': [
        {
            'id': 1,
            'title': 'The Shawshank Redemption',
            'year': 1994
        },
        {
            'id': 2,
            'title': 'The Godfather',
            'year': 1972
        },
        {
            'id': 3,
            'title': 'The Dark Knight',
            'year': 2008
        },
        {
            'id': 4,
            'title': '12 Angry Men',
            'year': 1957
        },
        {
            'id': 5,
            'title': "Schindler's List",
            'year': 1993
        }
    ]
}

def movies (request):
    return  render(request,'movies/movies.html', data)


def home(request):
    return HttpResponse('Home  Page')


#.\\.venv\Scripts\activate.bat