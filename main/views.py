from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

from .models import Post, Category
from .forms import CommentForm


# Create your views here.
def index_page(request):
    posts = Post.objects.all().order_by('-id')
    if 'page' in request.GET:
        page = request.GET['page']
    else:
        page = 1
    paginator = Paginator(posts, 15)
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    context = {
        'posts': posts
    }
    return render(request, "pages/index.html", context)


def category_page(request, name):
    category = Category.objects.get(name=name)

    posts = Post.objects.filter(category=category).order_by('-id')
    if 'page' in request.GET:
        page = request.GET['page']
    else:
        page = 1
    paginator = Paginator(posts, 15)
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    context = {
        'title': category.title,
        'posts': posts
    }
    return render(request, "pages/category.html", context)


def post_page(request, post_id):
    post = Post.objects.get(id=post_id)

    if request.method == "POST":
        comment = CommentForm(request.POST)
        if comment.is_valid():
            post.comments.add(comment.save())
            return HttpResponseRedirect(str(post_id))

    form = CommentForm()
    context = {
        'post': post,
        'form': form,
        'comments': post.comments.all()
    }
    return render(request, "pages/post.html", context)

