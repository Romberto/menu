# Generated by Django 4.2.7 on 2023-11-03 11:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0007_menuitem_url'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='menuitem',
            name='url',
        ),
    ]
