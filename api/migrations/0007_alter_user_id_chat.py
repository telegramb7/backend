# Generated by Django 3.2.9 on 2021-12-17 18:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_auto_20211213_1859'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='id_chat',
            field=models.IntegerField(unique=True),
        ),
    ]
