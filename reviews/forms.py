from django import forms
from djrichtextfield.widgets import RichTextWidget
from .models import Review


class ReviewForm(forms.ModelForm):
    """
    Form to create a product review
    """
    model = Review
    fields = [
        'rating',
        'content',
    ]

    content = forms.CharField(widget=RichTextWidget())

    labels = {
        'rating': 'Rating (1-5)',
        'content': 'Content',
    }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['rating'].widget.attrs['min'] = 1
        self.fields['rating'].widget.attrs['max'] = 5
