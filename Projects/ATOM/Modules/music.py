import webbrowser
import urllib.parse

def play(cmd):
    q = cmd.replace("play", "").strip()
    webbrowser.open(f"https://open.spotify.com/search/{urllib.parse.quote(q)}")
    return f"Searching Spotify: {q}"
