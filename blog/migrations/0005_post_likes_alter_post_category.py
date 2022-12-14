# Generated by Django 4.0.5 on 2022-06-27 07:00

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0004_category_post_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='likes',
            field=models.ManyToManyField(related_name='blog_likes', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.CharField(choices=[('News', 'News'), ('Sport', 'Sport'), ('Entertainment', 'Entertainment'), ('Celebrity Gist', 'Celebrity Gist')], default='Test', max_length=200),
        ),
    ]
