# Generated by Django 4.2.6 on 2023-11-04 13:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Board",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name="ClassLesson",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=30)),
                ("description", models.TextField(blank=True, null=True)),
                (
                    "board",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="boards",
                        to="blog.board",
                    ),
                ),
                ("relatives", models.ManyToManyField(to="blog.board")),
            ],
        ),
        migrations.CreateModel(
            name="Content",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("date", models.DateField(auto_now_add=True)),
                ("photo", models.FileField(upload_to="uploads/%Y/%m/%d/")),
                ("text", models.TextField(max_length=500, null=True)),
                (
                    "lesson",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="contents",
                        to="blog.classlesson",
                    ),
                ),
                ("relatives", models.ManyToManyField(to="blog.classlesson")),
            ],
        ),
    ]