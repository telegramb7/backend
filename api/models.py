from django.contrib.auth.models import AbstractBaseUser
from django.db import models

class User(models.Model):
    id_chat = models.IntegerField(unique=True)  # it's chat id from Telegram API
    username = models.CharField(max_length=100, blank=True)
    
    def __str__(self):
        return str(self.id)

class Anket(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    description = models.TextField(max_length=2000)
    file_unique_id = models.CharField(max_length=100)
    sex = models.BooleanField()  # ex. true it's male, false it's female
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='anket')

    def __str__(self):
        return str(self.name)

class Like(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="likeds"
    )  # likers it's who submit like
    partner = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="likes",
    )  # it's whom likers sub. like

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        if Like.objects.filter(user=self.partner, partner=self.user):
            Match.objects.create(who_like=self.user, whom_like=self.partner)
        return super().save(force_insert=force_insert, force_update=force_update, using=using, update_fields=update_fields)

    def __str__(self) -> str:
        return f"{self.user}:{self.partner}"


class Dislike(models.Model):
    who_dislike = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='author_dislike'
    )
    whom_dislike = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='dislike_partner',
    )

    def __str__(self) -> str:
        return f"{self.who_dislike}:{self.whom_dislike}"

class Match(models.Model):
    who_like = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="creators"
    )
    whom_like = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="favorits"
    )

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        #requests.post(link_match, json={'who_like':chat_id, whom_like:chat_id})
        return super().save(force_insert=force_insert, force_update=force_update, using=using, update_fields=update_fields)

    def __str__(self) -> str:
        return f"{self.who_like}:{self.whom_like}"
