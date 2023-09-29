# Generated by Django 3.2.20 on 2023-09-29 13:38

from django.conf import settings
from django.db import migrations, models
import django_resized.forms
import djrichtextfield.models
import stories.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('products', '0005_alter_product_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Story',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('author', models.CharField(max_length=50)),
                ('excerpt', djrichtextfield.models.RichTextField(max_length=600)),
                ('content', djrichtextfield.models.RichTextField()),
                ('image', django_resized.forms.ResizedImageField(crop=None, force_format='WEBP', keep_meta=True, quality=75, scale=None, size=[900, None], upload_to='stories/')),
                ('image_alt', models.CharField(max_length=100)),
                ('image_url', models.URLField(blank=True, max_length=1024, null=True)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('added_by', models.ForeignKey(limit_choices_to={'is_staff': True}, on_delete=models.SET(stories.models.get_sentinel_user), to=settings.AUTH_USER_MODEL)),
                ('age_match', models.ManyToManyField(to='products.TargetAge')),
                ('likes', models.ManyToManyField(blank=True, related_name='story_like', to=settings.AUTH_USER_MODEL)),
                ('product_match', models.ManyToManyField(blank=True, to='products.Product')),
            ],
            options={
                'ordering': ['-created_on'],
            },
        ),
    ]