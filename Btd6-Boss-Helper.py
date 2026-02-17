# make a bot that asks for the banned monkeys
# asks for which boss
# asks for stage
# asks if there is water on the map
# asks the speed of the boss in %
# asks for health in percentage

# spits out answer 

import math
import time

Bosses = ["vortex",
"phaze", 
"lych", 
"blastapopoulos", 
"dreadbloon", 
"bloonarius"
]

# Bloonarius HP
bloonarius_hp = {
    "normal": {
        1: 20000,
        2: 75000,
        3: 350000,
        4: 750000,
        5: 3000000
    },
    "elite": {
        1: 50000,
        2: 300000,
        3: 2000000,
        4: 8000000,
        5: 40000000
    }
}

# Lych HP
lych_hp = {
    "normal": {
        1: 14000,
        2: 52500,
        3: 220000,
        4: 525000,
        5: 2100000
    },
    "elite": {
        1: 30000,
        2: 180000,
        3: 1100000,
        4: 4800000,
        5: 24000000
    }
}

# Vortex HP
vortex_hp = {
    "normal": {
        1: 20000,
        2: 62800,
        3: 294000,
        4: 628000,
        5: 2512500
    },
    "elite": {
        1: 41800,
        2: 251000,
        3: 1675000,
        4: 6700000,
        5: 33500000
    }
}

# Phaze HP (shield + health combined)
phaze_hp = {
    "normal": {
        1: 11750,
        2: 43750,
        3: 200000,
        4: 437500,
        5: 1812500
    },
    "elite": {
        1: 23750,
        2: 137500,
        3: 875000,
        4: 3875000,
        5: 19375000
    }
}

# Dreadbloon HP (kept separate: lead HP + regular HP)
dreadbloon_hp = {
    "normal": {
        1: {"lead": 7500, "regular": 3750},
        2: {"lead": 25000, "regular": 12500},
        3: {"lead": 120000, "regular": 60000},
        4: {"lead": 260000, "regular": 130000},
        5: {"lead": 1000000, "regular": 500000}
    },
    "elite": {
        1: {"lead": 15000, "regular": 7500},
        2: {"lead": 90000, "regular": 45000},
        3: {"lead": 650000, "regular": 325000},
        4: {"lead": 2625000, "regular": 1312500},
        5: {"lead": 12500000, "regular": 6250000}
    }
}

# Blastapopoulos HP
blastapopoulos_hp = {
    "normal": {
        1: 17500,
        2: 65000,
        3: 300000,
        4: 650000,
        5: 3000000
    },
    "elite": {
        1: 43000,
        2: 270000,
        3: 1700000,
        4: 7000000,
        5: 35000000
    }
}

monkeys = [
"dart monkey",
"boomerang monkey",
"bomb shooter",
"tack shooter",
"ice monkey",
"glue gunner",
"desperado",
"sniper monkey",
"monkey sub",
"monkey buccaneer",
"monkey ace",
"heli pilot",
"mortar monkey",
"dartling gunner",
"wizard monkey",
"super monkey",
"ninja monkey",
"alchemist",
"druid",
"mermonkey",
"banana farm",
"spike factory",
"monkey village",
"engineer monkey",
"beast handler"
]

ranked_modes = ["least cash", "least tiers", "timed"]
difficulty_modes = ["normal", "elite"]

while True:
    boss = input("Boss: ").lower()
    if boss in Bosses:
        break
    else: 
        print("thats not a boss goober")

while True:
    stage = input("Stage (1-5): ")
    if stage.isdigit():
        stage = int(stage)
        if 1 <= stage <= 5:
            break
        else:
            print("Stage must be between 1 and 5")
    else:
        print("Please enter a valid number")

while True:
    difficulty = input("Difficulty (normal or elite): ").lower()
    if difficulty in difficulty_modes:
        break
    else:
        print("Invalid difficulty. Choose: normal or elite")

while True:
    ranked_mode = input("Ranked mode (least cash, least tiers, timed): ").lower()
    if ranked_mode in ranked_modes:
        break
    else:
        print("Invalid mode. Choose: least cash, least tiers, or timed")

print("If no modifier is mentioned, enter 100")
time.sleep(0.5)

while True:
    Speed = input("Speed modifier in %: ")
    FixedSpeed = Speed.replace('%', '').strip() 
    
    if FixedSpeed.isdigit():
        Speed = int(FixedSpeed)
        break
    else:
        print("Please enter a valid number")

while True:
    Health = input("Health modifier in %: ")
    FixedHealth = Health.replace('%', '').strip()
    
    if FixedHealth.isdigit():
        Health = int(FixedHealth)
        break
    else:
        print("Please enter a valid number")

print("Space each one out")
Bannedmonkeys = input("banned monkeys: ")