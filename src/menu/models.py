from django.db import models


class Menu(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class MenuItem(models.Model):
    url = models.CharField(max_length=100, default='/elem')
    title = models.CharField(max_length=100)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.id}:{self.title}'
