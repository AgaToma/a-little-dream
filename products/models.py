from django.db import models
from djrichtextfield.models import RichTextField
from django_resized import ResizedImageField


class Category(models.Model):

    class Meta:
        verbose_name_plural = 'Categories'
        
    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


# Choice Fields
TARGET_AGE = (
    ('all', 'All'),
    ('toddlers', 'Toddlers'),
    ('preschoolers', 'Preschoolers'),
    ('junior schoolers', 'Junior Schoolers'),
    ('pre-teens', 'Pre-teens'),
)


class Product(models.Model):
    category = models.ForeignKey(
        'Category', null=True, blank=True, on_delete=models.SET_NULL,
    )
    sku = models.CharField(
        max_length=254, null=True, blank=True,
    )
    name = models.CharField(max_length=254)
    author = models.CharField(max_length=200)
    highlights = RichTextField(max_length=500, null=False, blank=False)
    description = RichTextField(max_length=10000, null=False, blank=False)
    price = models.DecimalField(max_digits=3, decimal_places=2)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = ResizedImageField(
        size=[400, None],
        quality=75,
        upload_to="rooms/",
        force_format="WEBP",
        blank=False,
        null=False,
    )
    image_alt = models.CharField(max_length=100, null=False, blank=False)
    target_age = models.CharField(max_length=50, choices=VIEW_TYPES,
                                  default='all')
    stock_level = models.IntegerField(
        default=1, validators=[MinValueValidator(0), MaxValueValidator(1000)]
    )
    in_stock = models.BooleanField(default=True)

    def __str__(self):
        return self.name