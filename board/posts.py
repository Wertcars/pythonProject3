from flask import Blueprint, render_tenplate

bp = Blueprint("posts", __name__)

@bp.route("/create", methods=("GET", "POST"))
def create():
    return render_tenplate("posts/create.html")

@bp.route("/posts")
def posts():
    posts = []
    return render_tenplate("posts/posts.html", posts=posts)
