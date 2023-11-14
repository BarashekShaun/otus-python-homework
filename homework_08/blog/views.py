from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView
from .models import Lesson
from .forms import LessonCreateForm


class LessonsList(ListView):
    model = Lesson

    def get_queryset(self):
        qs = super().get_queryset()
        return qs

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        context['page_title'] = 'Main page'
        return context


class LessonsCreate(CreateView):
    model = Lesson
    form_class = LessonCreateForm
    success_url = reverse_lazy('lessons:index')