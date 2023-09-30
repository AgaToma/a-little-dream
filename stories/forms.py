from django import forms
from djrichtextfield.widgets import RichTextWidget
from products.models import Product, TargetAge
from .models import Story


class StoryForm(forms.ModelForm):
    """
    Form to add a story
    """
    class Meta:
        model = Story
        fields = '__all__'

        excerpt = forms.CharField(widget=RichTextWidget())
        content = forms.CharField(widget=RichTextWidget())

        age_match = forms.ModelMultipleChoiceField(
                    queryset=TargetAge.objects.all(),
                    widget=forms.CheckboxSelectMultiple)

        product_match = forms.ModelMultipleChoiceField(
                    queryset=Product.objects.all(),
                    widget=forms.CheckboxSelectMultiple)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)