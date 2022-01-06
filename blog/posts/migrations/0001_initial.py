# Generated by Django 3.2.9 on 2021-11-30 17:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Название категории')),
                ('description', models.TextField(verbose_name='Описание категории')),
                ('slug', models.SlugField(max_length=100, unique=True, verbose_name='URL')),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Заголовок')),
                ('preview_text', models.TextField(verbose_name='Превью')),
                ('full_text', models.TextField(blank=True, verbose_name='Текст')),
                ('pub_date', models.DateTimeField(auto_now_add=True)),
                ('slug', models.SlugField(max_length=100, unique=True, verbose_name='URL')),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='posts', to='posts.category', verbose_name='Категория')),
            ],
            options={
                'verbose_name': 'Пост',
                'verbose_name_plural': 'Посты',
                'ordering': ('-pub_date',),
            },
        ),
    ]
