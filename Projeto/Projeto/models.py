from django.db import models

# Create your models here.


class Contato(models.Model):

    nome = models.CharField(
        max_length=255,
        null=False,
        blank=False
    )

    sobrenome = models.CharField(
        max_length=255,
        null=False,
        blank=False
    )

    email = models.CharField(
        max_length=255,
        null=False,
        blank=False
    )

    telefone = models.CharField(
        max_length=9,
        null=False,
        blank=False
    )


objetos = models.Manager()

def __str__(self):
    return self.nome + ''

