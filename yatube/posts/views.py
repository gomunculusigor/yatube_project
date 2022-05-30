from django.http import HttpResponse


def index(request):
    return HttpResponse('ОНО ЖИВОЕ!!!')


def groups_posts(request, slug):
    return HttpResponse('ДАЖЕ ТУТ ЖИВОЕ')
# Create your views here.
