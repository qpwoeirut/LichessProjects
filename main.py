from get_unique_players_in_tournament_list import get_unique_players_in_tournament_list


OFFERSPILL_URLS = [
    "https://lichess.org/tournament/2uxfAuV1",
    "https://lichess.org/tournament/qF84vQWm",
    "https://lichess.org/tournament/6DfPQlEe",
    "https://lichess.org/tournament/xcIBrZbv",
    "https://lichess.org/tournament/Wz9ObpES",
    "https://lichess.org/tournament/BA0Byus4",
    "https://lichess.org/tournament/aslHRVp0",
    "https://lichess.org/tournament/YGPCw4xa",
    "https://lichess.org/tournament/OE7uEqBW",
    "https://lichess.org/tournament/1Wq9Joao",
    "https://lichess.org/tournament/S0YCiird",
    "https://lichess.org/tournament/xk8iSpOX",
    "https://lichess.org/tournament/9sFX7euH",
    "https://lichess.org/tournament/HxEoq9DB",
    "https://lichess.org/tournament/agkmo7ne",
    "https://lichess.org/tournament/wJXGPisV",
    "https://lichess.org/tournament/YwZWZXKx",
    "https://lichess.org/tournament/94FjgAzk",
    "https://lichess.org/tournament/60VmiN8x",
    "https://lichess.org/tournament/lgaqg0j1",
    "https://lichess.org/tournament/kw3CyxCp",
    "https://lichess.org/tournament/NxuJiYJR",
    "https://lichess.org/tournament/Vnvsx1EJ",
    "https://lichess.org/tournament/VDQE0xzP",
    "https://lichess.org/tournament/lGyNRRcW",
    "https://lichess.org/tournament/MPlFPqJu",
    "https://lichess.org/tournament/XtHuXjt7",
    "https://lichess.org/tournament/Le1B6ms3",
    "https://lichess.org/tournament/ANOcMEXm",
    "https://lichess.org/tournament/5dI1M2MK"
]
CCC_NACCL_URLS = [
    "https://lichess.org/tournament/nE8sEgZU",
    "https://lichess.org/tournament/bneCBdZ9",
    "https://lichess.org/tournament/6nTKRwoN",
    "https://lichess.org/tournament/SiuqPsSi",
    "https://lichess.org/tournament/hRWyCvd9",
    "https://lichess.org/tournament/GNQyCg0J",
    "https://lichess.org/tournament/76brxWWC",
    "https://lichess.org/tournament/tad2cbrO",
    "https://lichess.org/tournament/beJjDv3P",
    "https://lichess.org/tournament/bNV9sFMA",
    "https://lichess.org/tournament/UM98d1P4",
    "https://lichess.org/tournament/U3Qe6Ja5",
    "https://lichess.org/tournament/2fq8y5Ae",
    "https://lichess.org/tournament/eqqYAwat",
    "https://lichess.org/tournament/1aLvHqnR",
    "https://lichess.org/tournament/sTPQz39I",
    "https://lichess.org/tournament/ibtXfyWM",
    "https://lichess.org/tournament/IGtuwhPS",
    "https://lichess.org/tournament/HHjozKBd",
    "https://lichess.org/tournament/rTwnePZF",
    "https://lichess.org/tournament/hR9gnRZw",
    "https://lichess.org/tournament/WHMtArwG",
    "https://lichess.org/tournament/2WileAoA",
    "https://lichess.org/tournament/CYDHdFoT",
    "https://lichess.org/tournament/1akOmfyj",
    "https://lichess.org/tournament/LJXB4Kbv",
    "https://lichess.org/tournament/LEox0jKB",
    "https://lichess.org/tournament/eQ7IiLqq",
    "https://lichess.org/tournament/v7xMQUk7",
    "https://lichess.org/tournament/MuVtmdah"
]


OFFERSPILL_IDS = [url.removeprefix("https://lichess.org/tournament/") for url in OFFERSPILL_URLS]
CCC_NACCL_IDS = [url.removeprefix("https://lichess.org/tournament/") for url in CCC_NACCL_URLS]

ct = get_unique_players_in_tournament_list(OFFERSPILL_IDS + CCC_NACCL_IDS)
print(len(ct))
print(ct.most_common(20))
