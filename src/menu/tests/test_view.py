from django.test.testcases import TestCase
from django.urls import reverse
from ..models import Menu, MenuItem


class TestCaseMenuView(TestCase):

    def setUp(self):
        self.menu = Menu.objects.create(name="title-1")
        self.item_menu_1 = MenuItem.objects.create(title="item_title_1", menu=self.menu)

    def test_veiw_get_main_view(self):
        url = reverse('menu')
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'menu/main.html')

    def test_view_get_DetailItemView(self):
        url = reverse('detail_item', kwargs={'pk': self.item_menu_1.id})
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'menu/detailItem.html')

    def test_view_get_AboutView(self):
        url = reverse('about')
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response,'menu/about.html')
