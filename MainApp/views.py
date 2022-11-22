from django.http import Http404
from django.shortcuts import render, redirect
from MainApp.models import Snippet
from django.core.exceptions import ObjectDoesNotExist


def index_page(request):
    context = {'pagename': 'PythonBin'}
    return render(request, 'pages/index.html', context)


def add_snippet_page(request):
    context = {'pagename': 'Добавление нового сниппета'}
    return render(request, 'pages/add_snippet.html', context)


def snippets_page(request):
    snipps = Snippet.objects.all()
    context = {'snipps': snipps}
    # context = {'pagename': 'Просмотр сниппетов'}
    return render(request, 'pages/view_snippets.html', context)

def snippet_detail(request, id):
    try:
        snipp = Snippet.objects.get(id=id)
    except ObjectDoesNotExist:
        raise Http404(f"Сниппет с id={id} не найден")
    context = {
        "snipp": snipp
    }
    return render(request, 'pages/snippet-detail.html', context)
