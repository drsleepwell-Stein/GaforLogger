import requests

URL = "https://www.dwd.de/DE/fachnutzer/luftfahrt/teaser/luftsportberichte/fbeu40_node.html"

def fetch_html():
    r = requests.get(URL, timeout=15)
    r.raise_for_status()
    return r.text
