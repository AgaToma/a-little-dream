from django.db import models
from djrichtextfield.models import RichTextField
from django_resized import ResizedImageField
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils.crypto import get_random_string
from django.contrib.postgres.fields import ArrayField


class Category(models.Model):

    class Meta:
        verbose_name_plural = 'Categories'
      
    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


def random_sku():
    """Generates random sku string with store prefix"""
    prefix = 'ald'
    random_string = get_random_string(5, allowed_chars='0123456789')
    random_sku = f'{prefix}{random_string}'
    return random_sku


class TargetAge(models.Model):
    """Model to be referenced for multiple selection
    of product target age groups"""
    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Product(models.Model):
    category = models.ForeignKey(
        'Category', null=True, blank=True, on_delete=models.SET_NULL,
    )
    sku = models.CharField(max_length=8, unique=True, default=random_sku,
                           editable=True)
    name = models.CharField(max_length=254)
    author = models.CharField(max_length=200)
    highlights = RichTextField(max_length=500, null=False, blank=False)
    description = RichTextField(max_length=10000, null=False, blank=False)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = ResizedImageField(
        size=[400, None],
        quality=75,
        upload_to="products/",
        force_format="WEBP",
        blank=False,
        null=False,
    )
    image_alt = models.CharField(max_length=100, null=False, blank=False)
    target_ages = models.ManyToManyField(TargetAge)
    stock_level = models.IntegerField(
        default=1, validators=[MinValueValidator(0), MaxValueValidator(1000)]
    )
    in_stock = models.BooleanField(default=True)

    class Meta:
        """order by name in admin"""
        ordering = ("name",)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        """Override default save method
        to update stock level
        """
        if self.stock_level <= 0:
            self.in_stock = False
        else:
            self.in_stock = True
        super().save(*args, **kwargs)
