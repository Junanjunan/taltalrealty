from django.shortcuts import render
from django.http import JsonResponse
from django.core.paginator import Paginator
from django.apps import apps
from .models import *
from .sort_list import sort_list


def get_books_context(request, model):
    realtor = request.user.realtor_set.first()
    if realtor is None:
        return None
    all_field_list = [f.name for f in model._meta.get_fields()]
    all_field_list.remove('realtor')
    field_list = [item for item in sort_list if item in all_field_list]
    all_items = list(model.objects.filter(realtor=realtor).values_list(*field_list).order_by('-updated'))
    paginator = Paginator(all_items, 30)
    page = request.GET.get('page', 1)
    page_items = paginator.get_page(page)
    context = {
        'field_list': field_list,
        'paginator': paginator,
        'page_items': page_items,
    }
    return context


def book_list(request, model_name):
    app_label = 'books'
    try:
        model = apps.get_model(app_label, model_name)
    except:
        return JsonResponse({"response": "no model"})
    context = get_books_context(request, model)
    if context is None:
        return JsonResponse({"response":"no realtor"})
    return render(request, 'books/book_list.html', context)