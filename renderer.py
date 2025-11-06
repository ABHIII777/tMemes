import requests
import shutil
import subprocess
import ascii_magic 

def supportVIU():
    return shutil.which("viu") is not None

def renderImageWithViu(url):
    resp = requests.get(url, stream=True)
    resp.raise_for_status()

    terminal_width = str(shutil.get_terminal_size().columns)

    # process = subprocess.Popen(["viu", "-b", "--width", terminal_width, "-"], stdin=subprocess.PIPE)
    process = subprocess.Popen(["timg", "-"], stdin=subprocess.PIPE);
    process.stdin.write(resp.content)
    process.stdin.close()
    process.wait()

def renderImageAsAscii(url):
    resp = requests.get(url)
    resp.raise_for_status()

    img = ascii_magic.from_image(resp.content, columns=80, char="#")
    ascii_magic.to_terminal(img)
