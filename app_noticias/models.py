from django.db import models

# Create your models here.
class Noticia(models.Model):
    conteudo = models.TextField()
    titulo = models.CharField('título', max_length = 128, blank=True, null=True)
    autor = models.TextField("Autor",max_length = 128, blank=True, null=True)
    class Meta:
        verbose_name = "Notícia"
        verbose_name_plural = 'Notícias'
    

    def __str__(self):
        return self.conteudo



