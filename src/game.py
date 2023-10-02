blue = ["TOPB", "JNGB", "MIDB", "BOTB", "SUPB"]
red = ["TOPR", "JNGR", "MIDR", "BOTR", "SUPR"]

# Lists matchup pairs, 1v1 and XvX for jungler + lanes. "blue" and "red" arguments are arrays.

def list_matchups(blue, red):

    # This returns an "iterator" of tuples
    vs = list(zip(blue, red))

    for x in vs:
        print(x)

list_matchups(blue, red)

