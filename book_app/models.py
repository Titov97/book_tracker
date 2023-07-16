from django.db import models


# Create your models here.

class Genre(models.Model):
    name = models.CharField(max_length=50)


class Author(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)

    def __str__(self):
        return f'First name: {self.first_name}'


class Book(models.Model):
    class State(models.IntegerChoices):
        READ = 1
        NOT_READ = 2
        ONGOING = 3

    title = models.CharField(max_length=50)
    authors = models.ManyToManyField(Author)
    genre = models.ForeignKey(Genre,
                              on_delete=models.DO_NOTHING)  # on_delete = in momentul in care un gen este sters o sa existe mai multe carti care referentiaza
    number_of_pages = models.IntegerField()  # genul respectiv. Atunci trebuie sa definim comportamentul pt o carte atunci cand genul ei este sters
    description = models.TextField()
    published = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    state = models.IntegerField(choices=State.choices)

    def __str__(self):
        return f'Id: {self.id}, Title: {self.title}, Author:{self.authors.first()}'
