from django.db import models


class Categorie(models.Model):
    name = models.CharField(max_length=50, default=None)

    def __str__(self):
        return self.name


class Nationalitie(models.Model):
    name = models.CharField(max_length=50, default=None)

    def __str__(self):
        return self.name


class Author(models.Model):
    profile = models.ImageField(upload_to='authors-profile-images/', default='authors-profile-images/default.jpg')
    first_name = models.CharField(max_length=100, default=None)
    last_name = models.CharField(max_length=100, default=None)
    age = models.CharField(max_length=2, default=None, blank=False)
    nationality = models.ForeignKey(Nationalitie, on_delete=models.CASCADE)
    occupation = models.CharField(max_length=50, default=None)
    website = models.URLField(max_length=150)

    def __str__(self):
        return self.first_name + ' ' + self.last_name


class Book(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    title = models.CharField(max_length=150, default=None)
    description = models.TextField(default=None)
    mark = models.CharField(max_length=2, default=None)
    cover = models.ImageField(upload_to='books-cover-images/', default='books-cover-images/default.jpg')
    current_market_price = models.CharField(max_length=2, default=None)
    pages = models.CharField(max_length=3, default=None)
    category = models.ForeignKey(Categorie, on_delete=models.CASCADE)
    owned = models.BooleanField(default=False)

    def __str__(self):
        return self.title
