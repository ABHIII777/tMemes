from fetcher import getRandomMeme
from renderer import supportVIU, renderImageAsAscii, renderImageWithViu
from utils import loadingSpinner

def main():
    print("Fetching a random programming meme...")
    loadingSpinner("Fetching meme")

    memeURL, memeName = getRandomMeme()
    print

    if supportVIU():
        try:
            renderImageWithViu(memeURL)
            return
        except Exception as e:
            print(f"Failed to render with viu: {e}")

    renderImageAsAscii(memeURL)

if __name__ == "__main__":
    main()