from django.db import models

class Marca(models.Model):
    nome = models.CharField(max_length=50)
    descricao = models.CharField(max_length=50)
    nacionalidade = models.CharField(max_length=50)



    def __str__(self) -> str:
        return f"{self.descricao} {self.id}".upper()