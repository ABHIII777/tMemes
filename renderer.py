import os
import requests
import shutil
import subprocess
import ascii_magic 

def supportVIU():
    return shutil.which("viu") is not None

def renderImageWithViu(url):
    resp = requests.get(url, stream=True)
    resp.raise_for_status()

    process = subprocess.Popen(["viu", "-"], stdin=subprocess.PIPE)
    process.stdin.write(resp.content)
    process.stdin.close()
    process.wait()

def renderImageAsAscii(url):
    resp = requests.get(url)
    resp.raise_for_status()

    img = ascii_magic.from_image(img, columns=80, char="#")
    ascii_magic.to_terminal(img)