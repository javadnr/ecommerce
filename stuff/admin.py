from django.contrib import admin
from .models import Stuff, Tag, Questions, Comment
# Register your models here.

admin.site.register(Stuff)
admin.site.register(Tag)
admin.site.register(Questions)
admin.site.register(Comment)
