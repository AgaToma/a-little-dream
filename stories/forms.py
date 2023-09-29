from django import forms
from djrichtextfield.widgets import RichTextWidget
from models.products import Product, TargetAge
from .models import Story


class StoryForm(forms.ModelForm):
    """
    Form to add a story
    """
    class Meta:
        model = Story
        fields = ['title', 'author', 'excerpt',
                  'content', 'product_match',
                  'age_match', 'image', 'image_alt']

        content = forms.CharField(widget=RichTextWidget())

        age_match = forms.ModelMultipleChoiceField(
                    queryset=TargetAge.objects.all(),
                    widget=forms.CheckboxSelectMultiple)

        product_match = forms.ModelMultipleChoiceField(
                    queryset=Product.objects.all(),
                    widget=forms.CheckboxSelectMultiple)

        labels = {
            'title': 'Story Title',
            'author': 'Author',
            'excerpt': 'Excerpt',
            'content': 'Content',
            'product_match': 'Link Products',
            'age_match': 'Age Group',
            'image': 'Story Image',
            'image_alt': 'Describe Image'
        }