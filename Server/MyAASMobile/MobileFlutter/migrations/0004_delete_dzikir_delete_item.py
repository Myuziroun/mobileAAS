# Generated by Django 5.0.4 on 2024-07-01 12:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('MobileFlutter', '0003_alter_item_options'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Dzikir',
        ),
        migrations.DeleteModel(
            name='Item',
        ),
    ]