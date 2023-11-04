from django.contrib import admin
from .models import Board, ClassLesson, Content


@admin.register(Board)
class BoardAdmin(admin.ModelAdmin):
    list_display = "pk", "name"
    list_display_links = "pk", "name"


@admin.register(ClassLesson)
class ClassLesson(admin.ModelAdmin):
    list_display = "pk", "name", "description", "board"
    list_display_links = "pk", "name"


@admin.register(Content)
class Content(admin.ModelAdmin):
    list_display = "date", "photo", "text", "lesson"

