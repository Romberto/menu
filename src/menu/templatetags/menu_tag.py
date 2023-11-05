import datetime

from django import template
from django.db.models import QuerySet
from django.shortcuts import render
from django.template.defaultfilters import pprint

from ..models import Menu, MenuItem

register = template.Library()


@register.filter
def draw_menu(name_menu, current_url):
    menu_items = MenuItem.objects.select_related('menu', 'parent').filter(menu__name=name_menu)
    menu_structure = build_menu_structure(menu_items)
    html = ""
    for item in menu_structure:
        html += '<li class="position-relative">'
        if 'sub_menu' in item:
            html += f'<a href="#" class="btn btn-info menu__item menu__select">{item["title"]}</a>'
            html += '<ul class="menu__inner_list">'
            for sub_item in item['sub_menu']:
                html += '<li class="position-relative">'
                if 'sub_menu' in sub_item:
                    html += f'<a href="#" class="menu__inner_item btn btn-danger mb-1 js_menu__inner_item">{sub_item["title"]}</a>'
                    html += f'<ul class="menu__inner_item_list">'
                    for sub_sub_item in sub_item['sub_menu']:
                        # здесь добавляем класс menu_selected если элемент в меню выбран
                        if str(sub_sub_item["url"]) == current_url[1:]:
                            html += f'<li><p class=" bg-secondary text-light pt-2 pb-2 rounded text-center mb-1 menu_selected" id="{sub_sub_item["id"]}">{sub_sub_item["title"]}</p></li>'
                        else:
                            html += f'<li><a href="{sub_sub_item["url"]}" class="btn btn-success  mb-1" id="{sub_sub_item["id"]}">{sub_sub_item["title"]}</a></li>'
                    html += "</ul>"
                else:
                    html += f'<a href="{sub_item["url"]}/" class="btn btn-success mb-1 menu__inner_item mb-1">{sub_item["title"]}</a>'
                html += "</li>"
            html += '</ul>'
        else:
            html += f'<a href="{item["url"]}/" class="btn btn-success menu__item">{item["title"]}</a>'
            html += '</li>'

    return html


def build_menu_structure(menu_items, parent=None):
    menu_structure = []

    for item in menu_items:
        if item.parent == parent:
            menu_item = {
                'id': item.id,
                'title': item.title,
                'url': item.url,
                'menu': item.menu.name if item.menu else None
            }

            sub_menu = build_menu_structure(menu_items, item)
            if sub_menu:
                menu_item['sub_menu'] = sub_menu

            menu_structure.append(menu_item)

    return menu_structure
