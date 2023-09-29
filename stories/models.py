from django.db import models
from django.contrib.auth.models import User
from products.models import Product, TargetAge
from djrichtextfield.models import RichTextField
from django_resized import ResizedImageField


def get_sentinel_user():
    """
    Creates replacement for deleted story creator
    """
    return get_user_model().objects.get_or_create(username='deleted')[0]


class Story(models.Model):
    """
    Model to add stories
    """
    title = models.CharField(null=False, blank=False, max_length=100)
    author = models.CharField(max_length=50)
    excerpt = RichTextField(max_length=600, null=False, blank=False)
    content = RichTextField(null=False, blank=False)
    added_by = models.ForeignKey(
        User,
        on_delete=models.SET(get_sentinel_user),
        limit_choices_to={"is_staff": True},
    )
    image = ResizedImageField(
        size=[900, None],
        quality=75,
        upload_to="stories/",
        force_format="WEBP",
        blank=False,
        null=False,
    )
    image_alt = models.CharField(max_length=100, null=False, blank=False)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    likes = models.ManyToManyField(User, related_name='story_like', blank=True)
    product_match = models.ManyToManyField(Product, blank=True)
    age_match = models.ManyToManyField(TargetAge, blank=False)
