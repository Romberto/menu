import datetime

from django import template
from django.db.models import QuerySet
from django.shortcuts import render

from ..models import Menu, MenuItem

register = template.Library()


@register.simple_tag
def draw_menu(name_menu):
    menu_items = MenuItem.objects.select_related('menu').filter(menu__name=name_menu)
    menu_structure = build_menu_structure(menu_items)

    return menu_structure


def build_menu_structure(menu_items, parent=None):
    menu_structure = []

    for item in menu_items:

        if item.parent == parent:
            sub_menu = build_menu_structure(menu_items, item)
            if sub_menu:
                item.sub_menu = sub_menu
            menu_structure.append(item)

    return render_menu()

def render_menu():
    title = "<h1>Title</h2>"
    return render(title)




@register.simple_tag
def current_time(format_string):
    return datetime.datetime.now().strftime(format_string)


def render_menu(menu_items: QuerySet):
    for element in menu_items:
        print(element)
