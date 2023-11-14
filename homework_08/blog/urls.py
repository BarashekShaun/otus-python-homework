from django.urls import path
import blog.views as blog

app_name = 'lessons'

urlpatterns = [
    path('', blog.LessonsList.as_view(), name='index'),
    path('create/', blog.LessonsCreate.as_view(), name='create'),
]