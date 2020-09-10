from django.shortcuts import render
from .models import Post, Category


# Create your views here.
def index_page(request):
    context = {
        'posts': Post.objects.all().order_by('-id')
    }
    return render(request, "pages/index.html", context)


def category_page(request, name):
    category = Category.objects.get(name=name)
    context = {
        'title': category.title,
        'posts': Post.objects.filter(category=category)
    }
    return render(request, "pages/category.html", context)


def post_page(request, post_id):
    context = {
        'post': Post.objects.get(id=post_id)
    }
    return render(request, "pages/post.html", context)

