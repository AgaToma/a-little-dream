from django.shortcuts import render


def index(request):
    """
    View that returns the home page
    """
    context = {}
    return render(request, "home/index.html", context)
