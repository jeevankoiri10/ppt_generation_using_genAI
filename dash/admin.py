from django.contrib import admin

from .models import GenerationHistory


@admin.register(GenerationHistory)
class GenerationHistoryAdmin(admin.ModelAdmin):
    pass
