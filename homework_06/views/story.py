from flask import Blueprint, render_template, request, redirect, flash, url_for
from sqlalchemy import select
from sqlalchemy.exc import IntegrityError
from models.story import Story
from models.database import db
from typing import Sequence

story_app = Blueprint(
    "story_app",
    __name__,
    url_prefix="/story",
)


@story_app.get("/", endpoint="list")
def story_list():
    stmt = select(Story).order_by(Story.id)
    storys: Sequence[Story] = db.session.scalars(stmt)
    return render_template(
        "story/index.html",
        storys=storys
    )


@story_app.route("/add/", methods={"GET", "POST"}, endpoint="add")
def create_story():
    if request.method == "GET":
        return render_template("story/add.html")
    title = request.form.get("story-title")
    description = request.form.get("story-description")
    print(title)
    print(description)
    story = Story(title=title, description=description)
    db.session.add(story)

    try:
        db.session.commit()
    except IntegrityError:
        flash(f"Sorry, something went wrong", category="warning")
        return redirect(request.path)

    flash(f"Story {story.title!r} created")
    url = url_for("story_app.detail", story_id=story.id)
    return redirect(url)


def get_story_by_id_or_raise(story_id: int) -> Story:
   story: Story = db.get_or_404(
        Story,
        story_id,
        description=f"Story #{story_id} not found!",
    )
   return story


@story_app.get("/<int:story_id>/", endpoint="detail")
def get_story_by_id(story_id: int):
    return render_template(
        "story/detail.html",
        story=get_story_by_id_or_raise(story_id),
    )


@story_app.route(
    "/<int:story_id>/confirm-delete/",
    methods=["GET", "POST"],
    endpoint="confirm_delete",
)
def confirm_delete_story(story_id: int):
    story = get_story_by_id_or_raise(story_id)
    if request.method == "GET":
        return render_template(
            "story/confirm-delete.html",
            story=story,
        )

    title = story.title
    db.session.delete(story)
    db.session.commit()
    flash(f"Story {title!r} deleted.", category="danger")
    return redirect(url_for("story_app.list"))