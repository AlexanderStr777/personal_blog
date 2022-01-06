# posts/models.py
from django.db import models
from django.contrib.auth import get_user_model
from pytils.translit import slugify
from tinymce import HTMLField

User = get_user_model()


class Category(models.Model):
    title = models.CharField(
        'Название категории',
        max_length=200
    )
    description = models.TextField(
        'Описание категории',
        blank=True
    )
    slug = models.SlugField(
        'URL',
        max_length=70,
        blank=True,
        help_text='Максимальная длина - 70 символов. '
        'Если вы не заполните это поле, оно будет сформировано автоматически'
    )
    image = models.ImageField(
        'Изображение',
        upload_to='posts/',
        blank=True
    )

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
            if len(self.slug) > 70:
                self.slug = self.slug[:71]
        super(Category, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Post(models.Model):
    title = models.CharField('Заголовок', max_length=200)
    text = HTMLField('Текст')
    pub_date = models.DateTimeField('Дата публикации', auto_now_add=True)
    slug = models.SlugField(
        'URL',
        max_length=100,
        blank=True,
        help_text='Максимальная длина - 100 символов. '
        'Если вы не заполните это поле, оно будет сформировано автоматически'
        )
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        related_name='posts',
        blank=True,
        null=True,
        verbose_name='Категория',
    )

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
            if len(self.slug) > 70:
                self.slug = self.slug[:101]
        super(Post, self).save(*args, **kwargs)

    class Meta:
        ordering = ('-pub_date',)
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'
