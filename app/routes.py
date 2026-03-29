from flask import Blueprint, render_template, request
from app.api.riot_api import get_puuid

main = Blueprint("main", __name__)

@main.route("/", methods=["GET", "POST"])
def home():
    puuid = None

    if request.method == "POST":
        game_name = request.form.get("game_name")
        tag_line = request.form.get("tag_line")

        puuid = get_puuid(game_name, tag_line)

        print("PUUID:", puuid)

    return render_template("index.html", puuid=puuid)