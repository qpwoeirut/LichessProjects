import berserk
import json
import os
from collections import Counter
from typing import Iterable

client = berserk.Client()


def get_tournament_results(tournament_id: str) -> Iterable:
    if os.path.exists(f"cache/tournament/{tournament_id}/results.json"):
        with open(f"cache/tournament/{tournament_id}/results.json", "r") as cache_file:
            return json.load(cache_file)
    else:
        return client.tournaments.stream_results(tournament_id)


def get_unique_players_in_tournament_list(tournament_ids: list[str], include_players_with_no_games=False) -> Counter[str]:
    players = Counter()
    total_players_with_duplicates = 0
    for tournament_id in tournament_ids:
        print(f"Fetching players for tournament id {tournament_id}")
        tournament_info = client.tournaments.get_tournament(tournament_id)
        player_count = tournament_info["nbPlayers"]
        parsed = 0
        results = []
        for player in get_tournament_results(tournament_id):
            if include_players_with_no_games or "performance" in player:
                players[player["username"]] += 1
            parsed += 1
            if parsed % 250 == 0:
                print(f"{parsed}/{player_count}")

            results.append(player)

        if not os.path.exists(f"cache/tournament/{tournament_id}"):
            os.mkdir(f"cache/tournament/{tournament_id}")
        with open(f"cache/tournament/{tournament_id}/results.json", "w+") as cache_file:
            json.dump(results, cache_file)

        # for some reason these don't match at the end
        # perhaps player_count includes players that withdrew?
        print(parsed, player_count)

        total_players_with_duplicates += player_count

    print("Total, including duplicates:", total_players_with_duplicates)
    return players


if __name__ == "__main__":
    ct = get_unique_players_in_tournament_list(["MuVtmdah"])
    print(len(ct))
    assert max(ct.values()) == 1
