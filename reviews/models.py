from django.db import models
from djrichtextfield.models import RichTextField
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth.models import User
from products.models import Product


class Review(models.Model):
    """
    Model to create reviews
    """
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    content = RichTextField(max_length=10000, null=False, blank=False)
    rating = models.IntegerField(
        default=5, validators=[MaxValueValidator(5), MinValueValidator(1)])
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        """
        Returns author and product name
        """
        return f"{self.user.username} - {self.product.name}"
