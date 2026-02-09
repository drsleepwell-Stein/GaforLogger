from bs4 import BeautifulSoup

def parse_gafor(html):
    soup = BeautifulSoup(html, "html.parser")
    gafor = {f"G{str(i).zfill(2)}": None for i in range(1, 85)}

    table = soup.find("table")
    rows = table.find_all("tr")[1:]

    for row in rows:
        cols = [c.get_text(strip=True) for c in row.find_all("td")]
        if len(cols) >= 2 and cols[0].isdigit():
            key = f"G{cols[0].zfill(2)}"
            if key in gafor:
                gafor[key] = cols[1]

    return gafor
