from flask import Blueprint, render_template

bp = Blueprint("pages", __name__)

@bp.route("/")
def home():
    # return "K.Y.S. Italian"
    return render_template("pages/home.html")

@bp.route("/about")
def about():
    # return "K.Y.S. Poland"
    return render_template("pages/about.html")