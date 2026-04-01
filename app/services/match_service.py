from app.api.riot_api import get_match_detail


SUPPORT_POSITIONS = {"UTILITY", "SUPPORT"}


def format_game_duration(seconds):
    if not isinstance(seconds, int) or seconds < 0:
        return "-"
    minutes = seconds // 60
    remain_seconds = seconds % 60
    return f"{minutes}:{remain_seconds:02d}"


def extract_support_match_summaries(match_ids, puuid):
    if not match_ids or not puuid:
        return []

    summaries = []

    for match_id in match_ids:
        match_data = get_match_detail(match_id)
        if not match_data:
            continue

        info = match_data.get("info", {})
        participants = info.get("participants", [])
        me = next((p for p in participants if p.get("puuid") == puuid), None)
        if not me:
            continue

        if me.get("teamPosition") not in SUPPORT_POSITIONS:
            continue

        game_end_timestamp = info.get("gameEndTimestamp")
        if game_end_timestamp is None:
            game_end_timestamp = info.get("gameStartTimestamp", 0)

        summaries.append(
            {
                "match_id": match_id,
                "win": "Win" if me.get("win") else "Lose",
                "win_class": "win" if me.get("win") else "lose",
                "champion_name": me.get("championName", "-"),
                "kills": me.get("kills", 0),
                "deaths": me.get("deaths", 0),
                "assists": me.get("assists", 0),
                "kda": f"{me.get('kills', 0)} / {me.get('deaths', 0)} / {me.get('assists', 0)}",
                "game_duration": format_game_duration(info.get("gameDuration")),
                "vision_score": me.get("visionScore", 0),
                "wards_placed": me.get("wardsPlaced", 0),
                "wards_killed": me.get("wardsKilled", 0),
                "game_end_timestamp": game_end_timestamp,
            }
        )

    summaries.sort(key=lambda x: x.get("game_end_timestamp") or 0, reverse=True)
    return summaries
