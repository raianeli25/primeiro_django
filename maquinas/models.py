from django.conf import settings
from django.db import models
from django.utils import timezone


class Maquinas(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    nome = models.CharField(max_length=200)
    status = models.CharField(max_length=200)
    causa = models.TextField()
    data_inicio = models.DateTimeField()
    data_fim = models.DateTimeField()
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.nome
