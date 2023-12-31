from django.shortcuts import render
from django.views import View
from django.views.generic import DetailView

from .models import MenuItem


class MainView(View):

    def get(self, request):
        curret_url = request.path
        return render(request, "menu/main.html", {'curret_url': curret_url})


class DetailItemView(DetailView):
    model = MenuItem
    template_name = 'menu/detailItem.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["curret_url"] = self.request.path
        return context


class AboutView(View):
    def get(self, request):
        return render(request, 'menu/about.html')


class DefaultItemView(View):
    def get(self, request):
        return render(request, 'menu/default_item_menu.html')
