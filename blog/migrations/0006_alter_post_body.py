# Generated by Django 4.0.5 on 2022-06-27 11:43

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_post_likes_alter_post_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='body',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
    ]
