## IMPLEMENT COMPETITIVE ASWELL, THIS IS ONLY SOLOQ INFO

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

####

def assemble_matchup_url(champ1, champ2, lane, rank):
    url = "https://app.mobalytics.gg/lol/champions/{}/counters/{}/vs-{}?rank={}".format(champ1, lane, champ2, rank)
    return url

def get_matchup(url):
    chrome_options = Options()
    chrome_options.add_argument("--incognito")

    driver = webdriver.Chrome(options=chrome_options)

    driver.get(url)

####

champ1 = input("First champion: ")
champ2 = input("Second champion: ")
lane = input("Lane: ")
rank = input ("Rank: ")

url = assemble_matchup_url(champ1, champ2, lane, rank)

print(url)
get_matchup(url)
