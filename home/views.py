from django.shortcuts import render


def index(request):
    """ A view to return landing page """

    return render(request, "home/index.html")
