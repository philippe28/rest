from django.db import models


class Produto(models.Model):

    cpu = models.IntegerField(default=1)
    memoria = models.IntegerField(default=4)
    disco = models.IntegerField(default=250)
    so = models.CharField(max_length=50)
    preco = models.FloatField()
    provedores = models.CharField(max_length=150)

    class Meta:
        verbose_name = 'Produto'
        verbose_name_plural = 'Produtos'

    def __unicode__(self):
        return self.titulo
