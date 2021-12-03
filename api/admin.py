from django.contrib import admin
from .models import User, Anket, Like, Match


admin.site.register(User)
admin.site.register(Anket)
admin.site.register(Like)
admin.site.register(Match)
