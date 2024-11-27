from django.db import models
from django.contrib.auth.models import User


class Author(models.Model):
    name = models.CharField(max_length=200)
    birth_date = models.DateField(null=True, blank=True)
    death_date = models.DateField(null=True, blank=True)
    biography = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name

class Book(models.Model):
    STATUS_CHOICES = [
        ('available', 'Доступна'),
        ('checked_out', 'Занята'),
        ('reserved', 'Забронирована'),
        ('missing', 'Отсутствует'),
        ('under_repair', 'В ремонте'),
        ('being_viewed', 'Просматривается'),
    ]
    
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete = models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    year_of_publication = models.PositiveIntegerField(default=2000)
    description = models.TextField(null=True, blank=True)
    isbn = models.CharField(max_length=13, unique=True)  # International Standard Book Number
    available = models.CharField(max_length=20, choices=STATUS_CHOICES, default='available')  # Статус доступности книги 
    user = models.ForeignKey(User, on_delete = models.CASCADE, verbose_name='Пользователь' )

    def __str__(self):
        return self.title
