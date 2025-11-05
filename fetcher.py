import requests
import random

REPO_API = "https://api.github.com/repos/deep5050/programming-memes/contents/memes/1"

def get_meme_list():
    res = requests.get(REPO_API)
    res.raise_for_status()
    items = res.json()

    memes = [
        item["download_url"]
        for item in items
        if item["type"] == "file" and item["name"].lower().endswith((".jpg", ".jpeg", ".png", ".gif"))
    ]

    if not memes:
        raise RuntimeError("No memes found in the GitHub folder!")

    return memes

def getRandomMeme():
    memes = get_meme_list()
    meme_url = random.choice(memes)
    meme_name = meme_url.split("/")[-1]
    return meme_url, meme_name
