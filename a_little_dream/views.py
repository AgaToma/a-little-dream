from django.shortcuts import render


def error_403(request, exception):
    """
    Handles HTTP 403 errors
    """

    return render(request, 'errors/403.html')


def error_404(request, exception):
    """ "
    Handles HTTP 404 errors
    """

    return render(request, 'errors/404.html')
