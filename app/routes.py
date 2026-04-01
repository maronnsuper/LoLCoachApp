from flask import Blueprint, render_template, request
from app.api.riot_api import RiotAPIError, get_puuid, get_match_ids
from app.services.match_service import extract_support_match_summaries

main = Blueprint("main", __name__)

@main.route("/", methods=["GET", "POST"])
def home():
    puuid = None
    match_ids = None
    support_matches = []
    error_message = None
    info_message = None

    if request.method == "POST":
        game_name = request.form.get("game_name")
        tag_line = request.form.get("tag_line")

        try:
            puuid = get_puuid(game_name, tag_line)
            match_ids = get_match_ids(puuid, count=20)
            support_matches = extract_support_match_summaries(match_ids, puuid)

            if len(support_matches) == 0:
                info_message = "直近20試合にSUP試合がありませんでした。"
        except RiotAPIError as error:
            error_message = error.user_message

        print("PUUID:", puuid)
        print("MATCH IDS:", match_ids)
        print("SUPPORT MATCH COUNT:", len(support_matches))

    return render_template(
        "index.html",
        puuid=puuid,
        match_ids=match_ids,
        support_matches=support_matches,
        error_message=error_message,
        info_message=info_message,
    )
