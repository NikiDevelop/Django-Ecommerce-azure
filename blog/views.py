from django.shortcuts import render, get_object_or_404
from blog.models import Post, Categoria
from django.db.models import Q
# Create your views here.

def blog(request):
    queryset = request.GET.get("buscar")    
    posts=Post.objects.all()

    if queryset:
        posts = Post.objects.filter(
            Q(titulo__icontains = queryset) 
           # Q(categoria__icontains = queryset) |
           # Q(fecha__icontains = queryset)
        ).distinct()
    return render(request, "blog/blog.html", {"posts": posts})





def post_detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    return render(request, 'blog/post_detail.html', {'post': post})


def categoria(request, categoria_id):
    categoria=Categoria.objects.get(id=categoria_id)
    if Categoria.objects.all().exists():            
            posts=Post.objects.filter(categorias=categoria)
                   
    return render(request,'blog/categoria.html', {'categoria': categoria, "posts":posts})
   
     