from django.contrib import admin

from psychology.tools.models import Activity


@admin.register(Activity)
class ActivityAdmin(admin.ModelAdmin):
    list_display = (
        "day",
        "activity",
        "started_at",
        "ended_at",
        "expectation",
        "pleasure",
        "achievement",
        "created",
    )
