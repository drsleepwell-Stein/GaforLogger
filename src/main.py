from datetime import datetime
from fetch import fetch_html
from parse import parse_gafor
from excel import append_row

def main():
    html = fetch_html()
    gafor = parse_gafor(html)
    timestamp = datetime.now().strftime("%Y-%m-%d 08:00")
    append_row(timestamp, gafor)

if __name__ == "__main__":
    main()
