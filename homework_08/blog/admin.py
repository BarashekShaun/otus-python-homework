from django.contrib import admin
from .models import Board, Lesson, Content


@admin.register(Board)
class BoardAdmin(admin.ModelAdmin):
    list_display = "pk", "name"
    list_display_links = "pk", "name"


@admin.register(Lesson)
class Lesson(admin.ModelAdmin):
    list_display = "pk", "name", "description", "board"
    list_display_links = "pk", "name"


@admin.register(Content)
class Content(admin.ModelAdmin):
    list_display = "date", "photo", "text", "lesson"

