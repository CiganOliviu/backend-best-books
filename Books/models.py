from django.db import models


class Categorie(models.Model):
    name = models.CharField(max_length=50, default=None)

    def __str__(self):
        return self.name


class Nationalitie(models.Model):
    name = models.CharField(max_length=50, default=None)

    def __str__(self):
        return self.name


class Field(models.Model):
    name = models.CharField(max_length=50, default=None)

    def __str__(self):
        return self.name


class Author(models.Model):
    profile = models.ImageField(upload_to='authors-profile-images/', default='authors-profile-images/default.jpg',
                                blank=True)
    first_name = models.CharField(max_length=100, default=None, blank=True)
    last_name = models.CharField(max_length=100, default=None, blank=True)
    age = models.CharField(max_length=2, default=None, blank=True)
    nationality = models.ForeignKey(Nationalitie, on_delete=models.CASCADE, blank=True)
    field = models.ForeignKey(Field, on_delete=models.CASCADE, default=1, blank=True)
    website = models.URLField(max_length=150, blank=True)

    def __str__(self):
        return self.first_name + ' ' + self.last_name


class Book(models.Model):
    authors = models.ManyToManyField(Author, default=None)
    title = models.CharField(max_length=150, default=None, unique=True)
    description = models.TextField(default=None)
    mark = models.CharField(max_length=2, default=None)
    cover = models.ImageField(upload_to='books-cover-images/', default='books-cover-images/default.jpg')
    current_market_price = models.CharField(max_length=3, default=None)
    pages = models.CharField(max_length=3, default=None)
    category = models.ForeignKey(Categorie, on_delete=models.CASCADE)
    virtually_owned = models.BooleanField(default=False)
    physically_owned = models.BooleanField(default=False)

    def __str__(self):
        return self.title
