from django.db import models
import requests


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
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="anket")

    def __str__(self):
        return str(self.name)


class Like(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="likeds"
    )  # likers it's who submit like
    partner = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="likes",
    )  # it's whom likers sub. like

    class Meta:
        unique_together = ('user', 'partner',)

    def save(
        self, force_insert=False, force_update=False, using=None, update_fields=None
    ):
        if Like.objects.filter(user=self.partner, partner=self.user):
            Match.objects.create(who_like=self.user, whom_like=self.partner)
        return super().save(
            force_insert=force_insert,
            force_update=force_update,
            using=using,
            update_fields=update_fields,
        )

    def __str__(self) -> str:
        return f"{self.user}:{self.partner}"


class Dislike(models.Model):
    who_dislike = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="author_dislike"
    )
    whom_dislike = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="dislike_partner",
    )

    class Meta:
        unique_together = ('who_dislike', 'whom_dislike',)

    def __str__(self) -> str:
        return f"{self.who_dislike}:{self.whom_dislike}"


class Match(models.Model):
    who_like = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="creators"
    )
    whom_like = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="favorits"
    )

    def save(
        self, force_insert=False, force_update=False, using=None, update_fields=None):
        # json_data = {'first':{"id_chat":self.who_like.id_chat,"username": self.who_like.username, "photo":self.who_like.anket.file_unique_id},
        # 'second':{"id_chat":self.whom_like.id_chat,"username": self.whom_like.username, "photo":self.whom_like.anket.file_unique_id}}
        # requests.post("http://127.0.0.1:5000/match", json=json_data)
        return super().save(
            force_insert=force_insert,
            force_update=force_update,
            using=using,
            update_fields=update_fields,)

    def __str__(self) -> str:
        return f"{self.who_like}:{self.whom_like}"
