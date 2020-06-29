from django.contrib import admin

from app.models import Announcement


@admin.register(Announcement)
class AnnouncementAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}

