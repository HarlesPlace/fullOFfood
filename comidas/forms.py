from django.forms import ModelForm
from .models import Post, Comment

class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = [
            'titulo',
            'data',
            'conteudo',
        ]
        labels = {
            'titulo': 'Título',
            'data': 'Data publicação',
            'conteudo': 'Conteúdo do Post',
        }

class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = [
            'autor',
            'texto',
        ]
        labels = {
            'autor': 'Usuário',
            'texto': 'Comentário',
        }