from django.shortcuts import render, get_object_or_404
from .models import Post, Group


def index(request):
    template = 'posts/index.html'
    text = 'Это будет главная страница сайта Yatube'
    title = 'Последние обновления на сайте'
    posts = Post.objects.order_by('-pub_date')[:10]
    context = {
        'text': text,
        'posts': posts,
        'title': title
    }
    return render(request, template, context)


def group_post(request, slug):
    group = get_object_or_404(Group, slug=slug)
    groups = Post.objects.filter(group=group).order_by('-pub_date')[:10]
    template = 'posts/group_list.html'
    context = {
        'group': group,
        'groups': groups,
        'title': group.title,
        'chosen_group': group.slug
    }
    return render(request, template, context)
