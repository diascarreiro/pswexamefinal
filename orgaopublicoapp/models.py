from django.db import models
from PIL import Image

# Create your models here.
class orgaopublico(models.Model):
	"""Representa a entidade orgaopublico"""
	nome_orgaopublico = models.CharField(max_length=200)
	foto = models.ImageField(null=True, blank=True)
	desc_orgaopublico = models.TextField
	tipo_orgaopublico = models.CharField(max_length=200)
	conceito_orgaopublico = models.CharField(max_length=200)

	def save(self, *args, **Kwargs):
		super().save(*args, **Kwargs)
		im = Image.open(self.foto.path)
		novo_tamanho =(50,50)
		im.thumbnail(novo_tamanho)
		im.save(self.foto.path)


	def foto_url(self):
		if self.foto and hasattr(self.foto, 'url'):
			print ("a url da foto é:", self.foto_url)
			return self.foto.url
		else:
			return "/static/img/img/PM-TO.jpg"


	def __str__(self):
		"""Retorna uma representação de um string do modelo"""
		return self.nome_orgaopublico