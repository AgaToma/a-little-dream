# Generated by Django 3.2.20 on 2023-09-05 16:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_auto_20230901_1151'),
    ]

    operations = [
        migrations.AddField(
            model_name='targetage',
            name='friendly_name',
            field=models.CharField(blank=True, max_length=254, null=True),
        ),
    ]