# Generated by Django 3.0.5 on 2020-05-20 14:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0005_auto_20200520_1638'),
    ]

    operations = [
        migrations.RenameField(
            model_name='place',
            old_name='id',
            new_name='name',
        ),
    ]