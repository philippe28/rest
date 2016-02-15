from django.db import models
from django.core.urlresolvers import reverse_lazy

from django.conf import settings

class Produto(models.Model):

    nome = models.ForeignKey(settings.AUTH_USER_MODEL,
                             null=True, blank=True)
    cpu = models.IntegerField(default=1)
    memoria = models.IntegerField(default=4)
    disco = models.IntegerField(default=250)
    so = models.CharField(max_length=50)
    preco = models.DecimalField(max_digits=9, decimal_places=2)
    provedores = models.CharField(max_length=150)
    release = models.DateTimeField(u'lançamento')

    class Meta:
        verbose_name = 'Produto'
        verbose_name_plural = 'Produtos'
        ordering = ['preco']

    def get_absolute_url(self):
        return reverse_lazy('produto_detales', kwargs={'pk': self.pk})

    def __str__(self):
        return 'Produto: ' + self.provedores
