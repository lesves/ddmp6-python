# Generated by Django 3.0.5 on 2020-04-29 14:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0002_auto_20200429_1651'),
    ]

    operations = [
        migrations.AlterField(
            model_name='option',
            name='next_place',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='web.Place'),
        ),
    ]