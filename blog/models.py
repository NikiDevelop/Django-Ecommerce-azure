from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from ckeditor.fields import RichTextField


# Create your models here.



class Post(models.Model):
    titulo = models.CharField(max_length=50, default='Apple')
    contenido = RichTextField()
    imagen = models.ImageField(upload_to="blog", null=True, blank=True)
    autor = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    #category = models.ForeignKey(Category, on_delete=models.PROTECT)
    created = models.DateTimeField(null=False, default=timezone.now)
    updated = models.DateTimeField(null=False, default=timezone.now)

    class Meta:
        verbose_name='post'
        verbose_name_plural='posts'

    def __str__(self):
        return self.titulo

   
class Categoria(models.Model):
    name = models.CharField(max_length=255, unique=True)
    
    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias' 
    
    

    def __str__(self):
        return self.name