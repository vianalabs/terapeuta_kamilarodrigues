from django.db import models
from django.utils.text import slugify


class Post(models.Model):
    title = models.CharField(max_length=200, verbose_name="Título")
    slug = models.SlugField(unique=True, max_length=200)
    content = models.TextField(verbose_name="Conteúdo")
    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name="Data de Criação"
    )
    updated_at = models.DateTimeField(
        auto_now=True, verbose_name="Última atualização"
    )

    def __str__(self):
        return self.title

    def save(save, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)
