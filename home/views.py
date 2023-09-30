from django.shortcuts import render


def index(request):
    """
    View that returns the home page
    """
    context = {}
    return render(request, "home/index.html", context)


def privacy(request):
    """A view to return the privacy policy page"""
    return render(request, "home/privacy.html")


def terms(request):
    """A view to return the terms and conditions page"""
    return render(request, "home/terms.html")