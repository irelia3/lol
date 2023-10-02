#### IMPORTS

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

#### FUNCTIONS

# Writes mobalytics.gg URL to get matchup data from using get_matchup
def assemble_matchup_url(champ1, champ2, lane, rank):
    url = "https://app.mobalytics.gg/lol/champions/{}/counters/{}/vs-{}?rank={}".format(champ1, lane, champ2, rank)
    return url

# Get matchup data
def get_matchup(url):
    chrome_options = Options()
    chrome_options.add_argument("--incognito")

    driver = webdriver.Chrome(options=chrome_options)

    driver.get(url)

# Lists matchup pairs from a game (Blue vs Red), 1v1 and XvX for jungler + lanes. "blue" and "red" arguments are arrays.
def list_matchups(blue, red):

    # This returns an "iterator" of tuples
    vs = list(zip(blue, red))

    for x in vs:
        print(x)

#############################################################################################################################

champ1 = input("First champion: ")
champ2 = input("Second champion: ")
lane = input("Lane: ")
rank = input ("Rank: ")

url = assemble_matchup_url(champ1, champ2, lane, rank)

print(url)
get_matchup(url)

blue = ["TOPB", "JNGB", "MIDB", "BOTB", "SUPB"]
red = ["TOPR", "JNGR", "MIDR", "BOTR", "SUPR"]

list_matchups(blue, red)

