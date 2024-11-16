from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    context: dict = {
        'title': 'Home - Главная',
        'content': 'Магазин мебели Home'
    }
    return render(request, 'main/index.html', context)

def about(request):
    context: dict = {
        'title': 'Home - о нас',
        'content': 'О нас',
        'text_on_page': "Текст о том, какой это сасный магазин, а его директор просто пиздатый."
    }
    return render(request, 'main/about.html', context)
