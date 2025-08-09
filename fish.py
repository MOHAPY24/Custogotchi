
## Imports
import random as rn 
import time as tm
import json as js
import illnesses
import plugins




## Variables
hunger = 0
health = 0
cycles = 0
chlorine = 0
active = 0
trust = 0
ammonia = 0
nitrite = 0
nitrate = 0
pH = 0
genderr = 0
gH = 0
tanksizer = 0
lightamount = 0
kH = 0
namer = ""
temp = 0
sicknessname = ""
ager = 0
tank_clean = 0 ## ALGAE, CLOUDY WATER etc
metabolism = 0 
plantamounts = 0 ## AMOUNT OF PLANTS, WILL BE DEFINED IN CLASS
anerobicgas = 0 #AMOUNTS OF ANEROBIC GAS IF THERE IS ANY
substratedepth = 0
issick = False
aggression = 0
flaring = 0
matingmature = 0
vision = 0
fed = 0
leftoverfood = 0
boredom = 0






class Fish:
    def __init__(self, name, age,tanksize,gender):
        self.name = name
        self.age = age
        self.tanksize = tanksize
        self.gender = gender
        self.setup(gender,age,name,tanksize)
        global hunger 
        global leftoverfood
        global health 
        global active 
        global chlorine
        global trust
        global ammonia 
        global issick
        global sicknessname
        global boredom
        global nitrite 
        global nitrate
        global pH 
        global genderr
        global tanksizer
        global fed
        global gH
        global kH
        global temp
        global lightamount
        global tank_clean
        global metabolism
        global plantamounts
        global anerobicgas
        global aggression
        global matingmature
        global flaring
        global substratedepth
        global vision
        global ager
        global namer
        global hunger 
        global health 
        global active 
        global trust 
        global ammonia 
        global issick
        global sicknessname
        global nitrite 
        global nitrate
        global pH 
        global genderr
        global tanksizer
        global fed
        global gH
        global kH
        global temp
        fed=0
        global lightamount
        global tank_clean
        global metabolism
        global plantamounts
        global anerobicgas
        global aggression
        global matingmature
        global flaring
        global substratedepth
        global vision
        global ager
        global namer
        global tanker
        pass
        
    
    def setup(self, gender, age, name, tanksize):
        global hunger 
        hunger = 0
        global health 
        health = 100
        global active 
        active = 100
        global trust 
        trust = 0
        global ammonia 
        global issick
        global sicknessname
        global chlorine 
        chlorine = 0
        ammonia = 0
        global nitrite 
        nitrite = 0
        global nitrate
        global leftoverfood
        leftoverfood = 0
        nitrate = 15
        global pH 
        global boredom 
        boredom = 0
        pH = 7.1
        global genderr
        global tanksizer
        global fed
        fed = 60
        global gH
        global kH
        global temp
        global lightamount
        global tank_clean
        global metabolism
        global plantamounts
        global anerobicgas
        global aggression
        global matingmature
        global flaring
        global substratedepth
        global vision
        global ager
        global namer
        vision = 100
        if gender == "F" or gender == "Female" or gender == "female" or gender == "f":
            genderr = 0
        if gender == "M" or gender == "Male" or gender == "male" or gender == "m":
            genderr = 1
        gH = 50
        tanksizer = tanksize
        kH = 40
        temp = 25
        lightamount = 9
        tank_clean = 20
        metabolism = 100
        substratedepth = 2
        anerobicgas = substratedepth / tanksizer / tank_clean
        aggression = 20
        matingmature = age * 10
        if aggression > 50:
            flaring = 1
        else:
            flaring = 0
        global ager
        ager = age
        namer = name
        self.update() 

    def feed(self):
        global aggression
        global hunger
        global fed
        global active
        randomnum = rn.randint(1, 25)
        hunger -= randomnum
        fed += randomnum
        active += 10
        randomagres = rn.randint(1, 25)
        aggression - randomagres
        plugins.printdy(f"{namer} has been fed, -{randomnum} hunger, +{randomnum} food, -{randomagres} aggresion!")

    def play(self):
        ls = ["Mirror", "Laser", "TicTacToe"]
        global hunger
        global issick
        global sicknessname

        choice = rn.choices(ls)
        if choice == ['Mirror']:
            global aggression
            aggression += 50
            if aggression > 100:
                hunger += 10
                aggression = 100
            global active 
            active - 5  
            plugins.printdy(f"{namer} has played with a Mirror! {aggression} aggression, {namer} has flared!")

        if choice == ['Laser']:
            rsd = rn.randint(1, 1000)
            if rsd == 500:
                aggression = 0
                global health
                health = 20
                global vision
                hunger += 10
                vision = 0
                plugins.printdy(f"The laser hit {namer}'s eyes! They are now blind and there current health is {health}!")

            else:
                aggression += 15
                vision -= 1
                active -= 10
                hunger += 10
                plugins.printdy(f"{namer} has played with a laser! activity level is now {active}.")

        if choice == ['TicTacToe']:
            aggression - 10
            active -= 5
            hunger += 5
            plugins.printdy(f"{namer} has played tictactoe! its activity level is {active}")

    def Treat(self):
        if issick == True:
            if sicknessname == "ick":
                plugins.printdy(f"Oh no! {namer} has ick! how would you like to treat him?")
                plugins.printdy("1: IchX \n 2: High temp and salt bath \n 3: Ignore ")
                chcc = input(": ")
                if chcc == "1" or chcc == "ichx" or chcc == "IchX" or chcc == "Ichx":
                    if health < 100:
                        while health < 100:
                            health += 10
                            if health > 100:
                                health = 100
                        if health == 100:
                            issick = False
                            illnesses.ick.treated(Fish)

    def waterchange(self):
        global pH
        global kH
        global gH
        global ammonia
        global nitrite
        global nitrate
        global leftoverfood
        global anerobicgas
        global chlorine
        pH - 2.4
        ammonia - 15
        nitrite - 15
        nitrate - 5
        kH = 40
        gH = 150
        anerobicgas - 10
        leftoverfood - 15
        chlorine = 0
        plugins.printdy(f"Did a water change! {chlorine} chlorine, {pH} pH, {gH} gH, {kH} kH, {ammonia} ammonia, {nitrite} nitrite, {nitrate} nitrate, {anerobicgas} anerobic gas, {leftoverfood} leftover food ")

                        
                    

    
    def update(self):
        tm.sleep(1)
        plugins.cleancnsl()
        global aggression
        global ager
        global fed
        global hunger
        global health
        global boredom
        global active
        global metabolism
        global leftoverfood
        global ammonia
        global nitrate
        global nitrite
        global pH
        global kH
        global gH
        global cycles
        leftoverfood = fed / 5
        if leftoverfood > 30:
            ammonia += 1.2 #ppm
            health - ammonia 
        if leftoverfood > 60:
            ammonia += 2.5 
            health - ammonia
        if nitrite > 0:
            health - nitrite
        if nitrate > 26:
            health - 15
        if pH > 7.9:
            health - 20
            plugins.printdy("your pH is too high! do a water change")
        if gH > 500:
            health - 5
            plugins.printdy("Your gH is too high! do a water change")
        if kH > 60:
            aggression += 10
            plugins.printdy(f"Your kH is irrating {namer}, do a water change or ignore ")
        cycles = 0
        fed = fed - hunger
        cycles += 1
        if cycles == 6 or cycles > 6:
            if ammonia > 0:
                nitrite = ammonia -1
                ammonia = 0
                plugins.printdy("uh oh your ammonia has turned into nitrite! do a water change")
            if nitrite > 0:
                nitrate = nitrite - 2
                nitrite = 0
                plugins.printdy("uh oh your nitrite has turned into nitrate! do a water change")
            cycles = 0
            ager += 1
            plugins.printdy(f"{namer} is now {ager}!")
        if tanksizer < 4.9:
            health = 0
            plugins.printdy("DONT KEEP BETTAS IN LOWER THAN 5 GALLONS!! :(")
            quit("bad fishkeeper :(")
        if ager == 5 or ager > 5:
            plugins.printdy(f"{namer} is getting old :(")
        if hunger > 70:
            plugins.printdy(f"{namer} is hungry! Please feed it")
        if hunger > 120:
            plugins.cleancnsl()
            plugins.printdy(f"{namer} has died of starvation :(")
            quit("Dead :(")
        if ager > 7:
            plugins.printdy(f"{namer} has died of old age :(")
            quit("Dead :(")
        if active > 75 and active < 90:
            boredom += active / 2
            plugins.printdy(f"{namer} is very bored! play with him!")
        if health < 50:
            plugins.printdy(f"{namer} is hurt or sick! Treat him.")
        if health < 0 or health == 0:
            plugins.cleancnsl()
            plugins.printdy(f"{namer} has died due to low health :(")
            quit("Dead :(")
        hunger += 1
        aggression -= 2
        active -= 2
        global matingmature
        global anerobicgas
        if fed > 140:
            health - 20
            plugins.printdy(f"{namer} is bloated! please stop feeding them and play with them more!")
        if fed > 180:
            health = 0
            plugins.cleancnsl()
            plugins.printdy(f"{namer} has died of overfeeding :(")
            quit("Dead :(")
        if aggression > 100:
            hunger += 10
            aggression = 100
        anerobicgas = substratedepth / tanksizer / tank_clean
        matingmature = ager * 10
        global flaring
        if aggression > 50:
            flaring = 1
        else:
            flaring = 0
        metabolism += 2
        colours = [96, 91, 92, 93, 94, 95, 1, 4]
        chh = rn.choice(colours)
        colours = [96, 91, 92, 93, 94, 95, 1, 4]
        chh2 = rn.choice(colours)
        clr = "CUSTOGOTCHI V1 BETA"
        plugins.printdy(clr)
        cls2 = " 1: Play \n 2: Feed \n 3: Water Change"
        plugins.printdy(cls2)
        option = input("Your Option: ")
        if option in "play" or option in "Play" or option in "1":
            self.play()
            tm.sleep(1)
           
            self.update()
        if option in "feed" or option in "Feed" or option in "2":
            self.feed()
            tm.sleep(1)
            
            self.update()
        
        if option in "3" or option in "water change" or option in "Water Change" or option in "Water change":
            self.waterchange()
            tm.sleep(1)
            self.update()
        
        


