from django.contrib import admin

from app.models import Room, Blog, Comment, User, Feedback

admin.site.register(User)
admin.site.register(Room)
admin.site.register(Blog)
admin.site.register(Comment)
admin.site.register(Feedback)