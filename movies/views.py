from django.http import HttpResponse

def movies (request):
    return  HttpResponse('Hello World')


def home(request):
    return HttpResponse('Home Page')