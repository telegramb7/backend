# Generated by Django 3.2.9 on 2021-12-03 21:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0002_alter_user_anketa"),
    ]

    operations = [
        migrations.AlterField(
            model_name="anket",
            name="age",
            field=models.IntegerField(max_length=3),
        ),
    ]
