# Generated by Django 5.1.1 on 2025-01-30 09:32

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('information', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='answer',
            name='author',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='answer_author', to=settings.AUTH_USER_MODEL, verbose_name='Автор'),
        ),
        migrations.AddField(
            model_name='article',
            name='negative_grade',
            field=models.ManyToManyField(blank=True, related_name='minus', to=settings.AUTH_USER_MODEL, verbose_name='Отрицательные оценки'),
        ),
        migrations.AddField(
            model_name='article',
            name='positive_grade',
            field=models.ManyToManyField(blank=True, related_name='plus', to=settings.AUTH_USER_MODEL, verbose_name='Положительные оценки'),
        ),
        migrations.AddField(
            model_name='article',
            name='category',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='article', to='information.category', verbose_name='Категория'),
        ),
        migrations.AddField(
            model_name='comment',
            name='answer',
            field=models.ManyToManyField(blank=True, related_name='comment_answer', to='information.answer', verbose_name='Ответ'),
        ),
        migrations.AddField(
            model_name='comment',
            name='author',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='comment', to=settings.AUTH_USER_MODEL, verbose_name='Автор'),
        ),
        migrations.AddField(
            model_name='offer',
            name='answer',
            field=models.ManyToManyField(blank=True, related_name='offer_answer', to='information.answer', verbose_name='Ответ'),
        ),
        migrations.AddField(
            model_name='offer',
            name='author',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='offer', to=settings.AUTH_USER_MODEL, verbose_name='Автор'),
        ),
    ]
