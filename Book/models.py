from django.db import models



class Libro(models.Model):
    titulo = models.CharField(max_length=150)
    autor = models.CharField(max_length=150)
    valoracion = models.IntegerField()

    def __str__(self):
        return self.titulo


class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    published_date = models.DateField()

    class Meta:
        permissions = [
            ("development", "Permiso como Desarrollador"),
            ("scrum_master", "Permiso como Scrum Master"),
            ("product_owner", "Permiso como Product Owner"),
        ]

    def __str__(self):
        return self.title