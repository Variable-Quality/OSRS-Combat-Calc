from bs4 import BeautifulSoup
import requests
import csv
from player import Player
from equipment import Equipment, Loadout
from scraping import Scraper

#TODO:
#Need to be able to calculate max hit, attack roll, defence roll, and hit chance
#Do different calculations for with/without prayer, present all to user
#Dont worry about niche cases yet, just get the basics working
#Cache weapons in a local csv on first run, update periodically




s = Scraper()




p = Player(97,100,0,1,0)

print(p.max_hit())

