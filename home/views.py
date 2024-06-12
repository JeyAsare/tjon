from django.shortcuts import render

def index(request):
    """ A view to reutn the index page """
    return render(request, 'home/index.html')
