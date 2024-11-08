from django.forms import ModelForm
from .models import Post

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