from unittest import TestCase

from ..models import Menu, MenuItem
from ..templatetags.menu_tag import draw_menu, build_menu_structure


class TestMenuTag(TestCase):

    def setUp(self):
        self.menu = Menu.objects.create(name="title-1")
        self.item_menu_1 = MenuItem.objects.create(title="item_title_1", menu=self.menu)

    def test_draw_menu(self):
        data = draw_menu(name_menu='title-1', current_url='/')
        expected_data = '<li class="position-relative"><a href="default_url_item_menu/" class="btn btn-success menu__item">item_title_1</a></li><li class="position-relative"><a href="default_url_item_menu/" class="btn btn-success menu__item">item_title_1</a></li>'
        self.assertEquals(data, expected_data)

    def test_build_menu_structure(self):
        query = MenuItem.objects.select_related('menu', 'parent').filter(menu__name=self.menu.name)
        data = build_menu_structure(query)
        expected_data = [{'id': 1, 'title': 'item_title_1', 'url': 'default_url_item_menu', 'menu': 'title-1'}]
        self.assertEquals(data, expected_data)
