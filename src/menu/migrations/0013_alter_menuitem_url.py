# Generated by Django 4.2.7 on 2023-11-04 14:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0012_alter_menuitem_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menuitem',
            name='url',
            field=models.CharField(default='default_url_item_menu', max_length=100),
        ),
    ]
