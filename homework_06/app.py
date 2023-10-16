from os import getenv

from flask import Flask, render_template
from flask_migrate import Migrate

from views.about import about_app
from views.story import story_app
from models import db


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://user:pswrd@0.0.0.0:5432/story"
app.config['SECRET_KEY'] = '8f42a73054b1749f8f58848be5e6502c'
app.config.update(SQLALCHEMY_DATABASE_URI="postgresql://user:pswrd@0.0.0.0:5432/story")
# config_class_name = getenv("CONFIG_CLASS", "DevelopmentConfig")
# config_object = f"config.{config_class_name}"
# app.config.from_object(config_object)


db.init_app(app=app)
migrate = Migrate(app=app, db=db)

app.register_blueprint(about_app)
app.register_blueprint(story_app)


@app.get("/")
def get_index():
    return render_template("index.html")


if __name__ == '__main__':
    app.run(
        host="localhost",
        port=5000,
        debug=False,
    )
