from django.db import models


class Board(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class ClassLesson(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField(null=True, blank=True)
    board = models.ForeignKey(
        Board,
        on_delete=models.PROTECT,
        related_name="boards",
    )
    relatives = models.ManyToManyField(
        "blog.Board"
    )

    def __str__(self):
        return self.name


class Content(models.Model):
    date = models.DateField(auto_now_add=True)
    photo = models.FileField(upload_to="uploads/%Y/%m/%d/")
    text = models.TextField(max_length=500, null=True)
    lesson = models.ForeignKey(
        ClassLesson,
        on_delete=models.PROTECT,
        related_name="contents",
    )
    relatives = models.ManyToManyField(
        "blog.ClassLesson"
    )

