from pprint import pprint
from unittest import TestCase

from menu.models import Menu, MenuItem
from menu.templatetags.menu_tag import draw_menu


class TestTagMenu(TestCase):
    def setUp(self):
        self.menu = Menu.objects.create(name="title-1")
        self.item_menu_1 = MenuItem.objects.create(title="item_title_1", menu=self.menu)
        self.item_sub_item_1 = MenuItem.objects.create(title="sub_item_title_1", parent=self.item_menu_1,
                                                       menu=self.menu)

    def test_tag(self):
        response = draw_menu('title-1', '')
        expected = '''<li class="position-relative"><a href="#" class="btn btn-info menu__item menu__select">item_title_1</a><ul class="menu__inner_list"><li class="position-relative"><a href="default_url_item_menu" class="btn btn-success mb-1 menu__inner_item mb-1">sub_item_title_1</a></li></ul>'''
        self.assertEquals(response, expected)
