from django.contrib import admin
from .models import Review


class ReviewAdmin(admin.ModelAdmin):
    """
    Displaying reviews in admin UI
    """
    list_display = (
        'product',
        'user',
        'rating',
        'content',
    )
    search_fields = (
        'product',
        'user',
    )
    list_filter = (
        'rating',
    )

    admin.site.register(Review, ReviewAdmin)

