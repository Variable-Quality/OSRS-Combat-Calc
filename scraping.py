from bs4 import BeautifulSoup
import requests
import configparser
import csv
from datetime import datetime
from os.path import exists

configPath = r'cfg/config.cfg'
cfgParser = configparser.ConfigParser()
cfgParser.read_file(open(configPath))

url_dict = cfgParser["URL"]
exempt_items = str(cfgParser["EXEMPT"]).split(",")

#Ensures all cache csv files exist
for key in url_dict.keys():
    if not exists(f"cache/{key}.csv"):
        temp = open(f"cache/{key}.csv", "w")
        temp.close()

def clear_cache():
    for key in url_dict.keys():
        with open(f"cache/{key}.csv", "w") as file:
            file.write("")

def update():
    clear_cache()
    for key in url_dict.keys():
        data = requests.get(url_dict[key]).text
        soup = BeautifulSoup(data, 'html.parser')
        table = soup.find_all("tbody")[1]

        for row in table.find_all("tr")[1:]:
            #Need to revisit!!!!!!!
            #Code needs to deal with mage bonus as well as pos/neg values
            #Want to store these as integers, not strings

            row_info = row.find_all("td")
            item_info = {}
            #row_info[2] is if its f2p or not, could be useful in the future?
            temp = row_info[1].text.split("#")[0]
            if "last man standing" in temp.lower() or temp.lower() in exempt_items:
                continue

            item_info["Name"] = row_info[1].text
            item_info["Stab"] = row_info[3].text
            item_info["Slash"] = row_info[4].text
            item_info["Crush"] = row_info[5].text
            item_info["Magic"] = row_info[6].text
            item_info["Range"] = row_info[7].text
            item_info["Stab Def"] = row_info[8].text
            item_info["Slash Def"] = row_info[9].text
            item_info["Crush Def"] = row_info[10].text
            item_info["Magic Def"] = row_info[11].text
            item_info["Range Def"] = row_info[12].text
            item_info["Strength"] = row_info[13].text
            item_info["Ranged Strength"] = row_info[14].text
            #Magic Str is a percentage as opposed to an integer
            item_info["Magic Strength"] = row_info[15].text
            item_info["Prayer"] = row_info[16].text
            item_info["Weight"] = row_info[17].text
            try:
                item_info["Speed"] = row_info[18].text
            except IndexError:
                print("Item is not a weapon and thus does not have a speed identifier.")
            
            fieldnames = item_info.keys()
            #Need to fit a date in here somehow
            with open(f"cache/{key}.csv", "a") as csvfile:
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                writer.writerow(item_info)
            print(item_info)

if __name__ == "__main__":
    update()