from django.contrib.auth import admin
from django.urls import path
from .views import MainView, DetailItemView

urlpatterns = [
    path('', MainView.as_view()),
    path('<int:pk>', DetailItemView.as_view(), name="detail_item")
]