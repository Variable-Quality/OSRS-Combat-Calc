from bs4 import BeautifulSoup
import requests
import configparser
import csv
from datetime import datetime
from os.path import exists
import item_api
import time

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

class Scraper():    

    def clear_cache(self):
        for key in url_dict.keys():
            with open(f"cache/{key}.csv", "w") as file:
                file.write("")

    def update(self):
        self.clear_cache()
        for key in url_dict.keys():
            data = requests.get(url_dict[key]).text
            soup = BeautifulSoup(data, 'html.parser')
            table = soup.find_all("tbody")[1]

            for row in table.find_all("tr")[1:]:
                #Need to revisit!!!!!!!
                #Code needs to deal with mage bonus as well as pos/neg values
                #Want to store these as integers, not strings

                row_info = row.find_all("td")
                item_info = dict()
                #row_info[2] is if its f2p or not, could be useful in the future?

                #Definitely gonna have to have it clean up the csv files in another function somehow
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
                    item_info["Speed"] = -1
            
                fieldnames = item_info.keys()
                #Need to fit a date in here somehow
                with open(f"cache/{key}.csv", "a") as csvfile:
                    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                    writer.writerow(item_info)
                print(item_info)

class Cache_Manager():

    def __init__(self):
        self.csv_fieldnames = ["Name", "Stab", "Slash", "Crush", "Magic", "Range", "Stab Def", "Slash Def", "Crush Def", "Magic Def", "Range Def", "Strength", "Ranged Strength", "Magic Strength", "Prayer", "Weight", "Speed"]
        
    def write_csv(csv_path, data, fieldnames, dict=True, append=True, ):
        if append:
            mode = "a"
        else:
            mode = "w"

        if dict:
            with open(f"{csv_path}.csv", mode) as csvfile:
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                writer.writerow(data)
        else:
            with open(f"{csv_path}.csv", mode) as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow(data)



    def read_csv(csv_path, fieldnames):
        ret = dict()
        with open(f"{csv_path}.csv", "r") as csvfile:
            reader = csv.DictReader(csvfile, fieldnames=fieldnames)
            for row in reader:
                ret = ret | row
        return ret

                
    def update(self):
        files = url_dict.keys()
        data = dict()
        for file in files:
            self.write_csv
            with open(f"cache/{file}.csv", "r") as csvfile:
                data[file] = csv.DictReader(csvfile, fieldnames=self.csv_fieldnames)

        return data

    def load_from_cache(self):
        names = dict()
        for file in url_dict.keys():
            data = dict()
            with open(f"cache/{file}.csv", "r") as csvfile:
                data[file] = csv.DictReader(csvfile, fieldnames=self.csv_fieldnames)

                for row in data[file]:
                    name = row["Name"]
                    del row["Name"]
                    names[name] = row

        return names

    def debug(self):
        pass

if __name__ == "__main__":
    c = Cache_Manager()
    c.debug()