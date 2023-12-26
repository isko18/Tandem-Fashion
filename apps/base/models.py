from django.db import models
from django.urls import reverse
from django.utils.text import slugify


class Index(models.Model):
    title = models.CharField(
        max_length=255, 
        verbose_name="Заголовок сайта",
        blank=True, null=True
    )
    description = models.TextField(
        verbose_name="Описание сайта", 
        blank=True, null=True
    )
    logo = models.ImageField(
        upload_to="image/",
        verbose_name="Лого сайта",
        blank=True, null=True
    )
    email = models.EmailField(
        verbose_name="Email",
        blank=True, null=True
    )
    number = models.CharField(
        max_length=15,
        verbose_name="Номер телефона",
        blank=True, null=True
    )
    locate = models.CharField(
        max_length=255,
        verbose_name="Адрес",
        blank=True, null=True
    )
    whatsapp = models.URLField(
        verbose_name="Ссылка на whatsapp",
        blank=True, null=True
    )
    telegram = models.URLField(
        verbose_name="Ссылка на telegram",
        blank=True, null=True
    )
    slug = models.SlugField( 
        max_length=255,
        unique=True,
        db_index=True,
        blank=True, null=True
        )

    def get_absolute_url(self):
        return reverse('index',  kwargs={'slug': self.slug})
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)
    

    class Meta:
        verbose_name = "Настройка сайта"
        verbose_name_plural = "Настройки сайта"


class Review(models.Model):
    name = models.CharField(
        max_length=155,
        verbose_name="Имя пользователя",
        null=True,blank=True
    )
    email = models.EmailField(
        verbose_name="Почта"
    )
    phone = models.CharField(
        max_length=155,
        verbose_name="Номер телефона",
        null=True,blank=True
    )

    class Meta:
        verbose_name = "Оставленная заявка"
        verbose_name_plural = "Оставленные заявки"