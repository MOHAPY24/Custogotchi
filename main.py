import fish
import time
import random as rn
import plugins


def main():
    colours = [96, 91, 92, 93, 94, 95, 1, 4]
    chh1 = rn.choice(colours)
    cals1 = "Build Your Betta!!"
    plugins.printdy(cals1)
    amm = input("Name your betta: ")
    agg = input("Whats your bettas age?: ")
    agg = int(agg)
    tks = input("Whats your bettas tank size?: ")
    gnder = input("Finally whats your bettas gender?: ")
    tks = int(tks)
    insta = fish.Fish(amm, agg, tks, gnder)
if __name__ == "__main__":
    main()


