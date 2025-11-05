# import requests
# import random

# REPO_RAW = "https://raw.githubusercontent.com/deep5050/programming-memes/main/memes/1"
# REPO_API = "https://api.github.com/repos/deep5050/programming-memes/contents/memes/1"

# def getList():
#     res = requests.get(REPO_API)
#     res.raise_for_status()
#     files = [
#         f["name"] for f in res.json()
#         if f["name"].lower().endswith((".jpg", ".jpeg", ".png", ".gif"))
#     ]

#     return files


# def getRandomMeme():
#     memes = getList()
#     meme = random.choice(memes)

#     return REPO_RAW + meme, meme

import requests
import random

# Target folder (memes/1)
REPO_API = "https://api.github.com/repos/deep5050/programming-memes/contents/memes/1"

def get_meme_list():
    """Fetch meme download URLs directly from GitHub API."""
    res = requests.get(REPO_API)
    res.raise_for_status()
    items = res.json()

    memes = [
        item["download_url"]
        for item in items
        if item["type"] == "file" and item["name"].lower().endswith((".jpg", ".jpeg", ".png", ".gif"))
    ]

    if not memes:
        raise RuntimeError("❌ No memes found in the GitHub folder!")

    return memes

def getRandomMeme():
    """Pick a random meme URL and its name."""
    memes = get_meme_list()
    meme_url = random.choice(memes)
    meme_name = meme_url.split("/")[-1]
    return meme_url, meme_name
