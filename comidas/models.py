from django.db import models
from django.conf import settings


class Post(models.Model):
    titulo = models.CharField(max_length=255)
    conteudo = models.TextField()
    data = models.DateTimeField(auto_now_add=False)
    def __str__(self):
        return f'{self.titulo} ({self.data})'
    class Meta:
        ordering = ['-data']
    
class Comment(models.Model):
    autor= models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    texto=models.CharField(max_length=1000)
    data = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    def __str__(self):
        return f'{self.texto} - {self.autor.username}'
    class Meta:
        ordering = ['-data']
