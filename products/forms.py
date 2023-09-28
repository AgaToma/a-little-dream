from django import forms
from djrichtextfield.widgets import RichTextWidget
from .models import Product, Category, TargetAge


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = '__all__'

    target_ages = forms.ModelMultipleChoiceField(
        queryset=TargetAge.objects.all(),
        widget=forms.CheckboxSelectMultiple)
    author = forms.CharField(required=False)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        categories = Category.objects.all()
        friendly_names = [(c.id, c.get_friendly_name()) for c in categories]

        self.fields['category'].choices = friendly_names
