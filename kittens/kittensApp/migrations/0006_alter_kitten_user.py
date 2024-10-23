# Generated by Django 5.1.1 on 2024-10-23 15:13

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kittensApp', '0005_alter_kitten_options'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='kitten',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='kittens', to=settings.AUTH_USER_MODEL, verbose_name='Хозяин'),
        ),
    ]
