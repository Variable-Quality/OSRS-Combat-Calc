from bs4 import BeautifulSoup
import requests
import csv

URLS = {"One Handed":"https://oldschool.runescape.wiki/w/Weapon_slot_table",
        "Two Handed":"https://oldschool.runescape.wiki/w/Two-handed_slot_table"}

data = requests.get(URLS["One Handed"]).text
soup = BeautifulSoup(data, 'html.parser')

table = soup.find_all("tbody")[1]
i = 0
for row in table.find_all("tr")[1:]:
        row_info = row.find_all("td")
        item_name = row_info[1].text
        item_stats = row_info[3:]

        print(f"\n{item_name}: \n")
        print(item_stats)


