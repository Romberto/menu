from django.contrib.auth import admin
from django.urls import path
from .views import MainView, DetailItemView, AboutView, DefaultItemView

urlpatterns = [
    path('', MainView.as_view(), name="menu"),
    path('<int:pk>', DetailItemView.as_view(), name="detail_item"),
    path('about/', AboutView.as_view(), name="about"),
    path('default_url_item_menu/', DefaultItemView.as_view(), name="default_item")
]