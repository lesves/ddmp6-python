# Generated by Django 3.0.5 on 2020-05-20 14:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0004_auto_20200513_1556'),
    ]

    operations = [
        migrations.AddField(
            model_name='character',
            name='place',
            field=models.CharField(max_length=128, null=True),
        ),
        migrations.AlterField(
            model_name='place',
            name='id',
            field=models.CharField(max_length=128, primary_key=True, serialize=False),
        ),
    ]