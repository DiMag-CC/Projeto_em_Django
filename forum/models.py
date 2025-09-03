import datetime
from django.db import models
from django.utils import timezone

class Pergunta(models.Model):
    titulo = models.CharField(max_length=200, null=False)
    detalhe = models.TextField(null=False)
    tentativa = models.TextField(blank=True, null=True)
    data_criacao = models.DateTimeField("Criado em ")
    usuario = models.CharField(max_length=200, null=False, default="anônimo")

    def __str__(self):
        return f"[{self.id}] {self.titulo}"

    def foi_publicado_recentemente(self):
        return self.data_criacao >= timezone.now() - datetime.timedelta(days=1)

    def string_detalhada(self):
        return (
            f"id: {self.id}; titulo: {self.titulo}; detalhe: {self.detalhe}; "
            f"tentativa: {self.tentativa}; data criação: {self.data_criacao}; "
            f"usuario: {self.usuario}"
        )

class Resposta(models.Model):
    pergunta = models.ForeignKey(Pergunta, on_delete=models.CASCADE)
    texto = models.TextField(null=False)
    votos = models.IntegerField(default=0)
    data_criacao = models.DateTimeField("Criado em ")
    usuario = models.CharField(max_length=200, null=False, default="anônimo")

    def __str__(self):
        return f"[{self.id}] {self.texto}"

    def foi_publicado_recentemente(self):
        return self.data_criacao >= timezone.now() - datetime.timedelta(days=1)
