from django.contrib.auth.models import AbstractBaseUser
from django.db import models

class User(models.Model):
    id_chat = models.CharField(max_length=50,unique=True)  # it's chat id from Telegram API
    
    def __str__(self):
        return str(self.id_chat)

class Anket(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    description = models.TextField(max_length=2000)
    file_unique_id = models.CharField(max_length=100)
    sex = models.BooleanField()  # ex. true it's male, false it's female
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.name)

class Like(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="likeds"
    )  # likers it's who submit like
    partner = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="likes"
    )  # it's whom likers sub. like

    def __str__(self) -> str:
        return f"{self.user}:{self.partner}"


class Match(models.Model):
    who_like = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="creators"
    )
    whom_like = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="favorits"
    )

    def __str__(self) -> str:
        return f"{self.who_like}:{self.whom_like}"
