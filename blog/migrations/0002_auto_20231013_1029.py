# Generated by Django 3.2.22 on 2023-10-13 10:29

from django.db import migrations, models
import django_quill.fields


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blogpost',
            name='likes',
        ),
        migrations.AddField(
            model_name='blogpost',
            name='slug',
            field=models.SlugField(blank=True, max_length=250, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='comment',
            name='upvotes',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='blogpost',
            name='content',
            field=django_quill.fields.QuillField(),
        ),
    ]
