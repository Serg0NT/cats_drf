# Generated by Django 5.1.1 on 2024-10-02 15:47

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kittensApp', '0002_remove_kitten_birthdate_remove_kitten_gender_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RemoveField(
            model_name='kitten',
            name='owner',
        ),
        migrations.AddField(
            model_name='kitten',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='owners', to=settings.AUTH_USER_MODEL, verbose_name='Хозяин'),
        ),
        migrations.DeleteModel(
            name='Owner',
        ),
    ]