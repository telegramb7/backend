# Generated by Django 3.2.9 on 2021-12-21 19:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0007_alter_user_id_chat"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="username",
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
