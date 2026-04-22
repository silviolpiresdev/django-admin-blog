from django.db import models
from django.contrib.auth.models import User


class Tecnologia(models.Model):
    nome = models.CharField(max_length=100, null=False, blank=False)
    
    def __str__(self):
        return self.nome
    
    
class Post(models.Model):
    titulo = models.CharField(max_length=300, null=False, blank=False)
    descricao = models.CharField(max_length=500, null=False, blank=False)
    conteudo = models.TextField(null=False, blank=False)
    autor = models.ForeignKey(User, on_delete=models.CASCADE, null=False, blank=False)
    tecnologias = models.ManyToManyField(Tecnologia, blank=False)
    


    def __str__(self):
        return self.titulo
    
    
     