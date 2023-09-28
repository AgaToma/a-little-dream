from django import forms
from djrichtextfield.widgets import RichTextWidget
from .models import Review


class ReviewForm(forms.ModelForm):
    """
    Product Review form
    """

    class Meta:

        model = Review
        fields = [
            'content',
            'rating',
        ]

        content = forms.CharField(widget=RichTextWidget())

        labels = {
            'content': 'Content',
            'rating': 'Rating (1-5)',
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['rating'].widget.attrs['min'] = 1
        self.fields['rating'].widget.attrs['max'] = 5
        
