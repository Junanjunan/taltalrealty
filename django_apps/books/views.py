from django.shortcuts import render
from django.http import JsonResponse
from django.core.paginator import Paginator
from django.apps import apps
from .models import *
import importlib
from .sort_list import table_list, sort_list, not_searching_list, contains_list, lte_list, gte_list, value_list, bool_list


def get_books_context(request, model, model_form):
    realtor = request.user.realtor_set.first()
    if realtor is None:
        return None
    field_list = model._meta.get_fields()
    field_list = sorted(field_list, key=lambda field: sort_list.index(field.name))
    searching_field_list = [field for field in field_list if not field.name in not_searching_list]
    table_field_list = [field.name for field in field_list if field.name in table_list]
    filter_kwargs = {}
    for k, v in request.GET.items():
        if v=='':
            continue
        elif k in contains_list:
            filter_kwargs[f'{k}__contains'] = v
        elif k in lte_list:
            filter_kwargs[f'{k}__lte'] = v
        elif k in gte_list:
            filter_kwargs[f'{k}__gte'] = v
        elif k in bool_list:
            filter_kwargs[k] = True
        elif k in value_list:
            filter_kwargs[k] = v
    all_items = list(model.objects.filter(**filter_kwargs, realtor=realtor).values_list(*table_field_list).order_by('-updated'))
    paginator = Paginator(all_items, 30)
    page = request.GET.get('page', 1)
    page_items = paginator.get_page(page)
    filtered_request = {k:v for k, v in request.GET.items() if v != ''}
    model_form = model_form(initial=filtered_request)
    context = {
        'searching_field_list': searching_field_list,
        'field_list': field_list,
        'table_field_list': table_field_list,
        'paginator': paginator,
        'page_items': page_items,
        'model_form': model_form,
    }
    return context


def book_list(request, model_name):
    app_label = 'books'
    try:
        imported_model = apps.get_model(app_label, model_name)
        form_module = importlib.import_module('django_apps.books.forms')
        form_name = f'{model_name.capitalize()}Form'
        imported_form = getattr(form_module, form_name)
    except:
        return JsonResponse({"response": "no model"})
    context = get_books_context(request, imported_model, imported_form)
    if context is None:
        return JsonResponse({"response":"no realtor"})
    return render(request, 'books/book_list.html', context)