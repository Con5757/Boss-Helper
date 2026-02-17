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
boss_difficulty_modes = ["normal", "elite"]
game_difficulty_modes = ["easy", "medium", "hard", "impoppable"]

# Cost multipliers by difficulty
difficulty_multipliers = {
    "easy": 0.85,
    "medium": 1.0,
    "hard": 1.08,
    "impoppable": 1.20
}

# Monkey data
dart_monkey = {
    "base_cost": 215,
    "category": "primary",
    "upgrades": {
        "top": [140, 200, 320, 1800, 15000],
        "middle": [100, 190, 450, 7200, 45000],
        "bottom": [90, 200, 575, 2050, 21500]
    },
    "special_properties": {
        "lead_popping": None,
        "camo_detection": "0-0-2"
    }
}

boomerang_monkey = {
    "base_cost": 315,
    "category": "primary",
    "upgrades": {
        "top": [200, 280, 600, 2000, 32500],
        "middle": [175, 250, 1250, 4200, 35000],
        "bottom": [100, 300, 1300, 2200, 50000]
    },
    "special_properties": {
        "lead_popping": "0-0-2",
        "camo_detection": None
    }
}

bomb_shooter = {
    "base_cost": 525,
    "category": "primary",
    "upgrades": {
        "top": [250, 650, 1100, 2800, 55000],
        "middle": [250, 400, 1000, 3450, 28000],
        "bottom": [200, 300, 700, 2500, 23000]
    },
    "special_properties": {
        "lead_popping": "base",
        "camo_detection": None,
        "can_pop_black": "tier_5_top",
        "notes": "Cannot pop Black/Zebra normally"
    }
}

tack_shooter = {
    "base_cost": 280,
    "category": "primary",
    "upgrades": {
        "top": [150, 300, 600, 3500, 45500],
        "middle": [100, 225, 550, 2700, 15000],
        "bottom": [100, 100, 450, 3200, 20000]
    },
    "special_properties": {
        "lead_popping": "3-0-0",
        "camo_detection": None,
        "notes": "Ring of Fire cannot pop Purple"
    }
}

def boss_calculation():
    """Main boss calculation function"""
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
        boss_difficulty = input("Boss difficulty (normal or elite): ").lower()
        if boss_difficulty in boss_difficulty_modes:
            break
        else:
            print("Invalid difficulty. Choose: normal or elite")

    while True:
        game_difficulty = input("Game difficulty (easy, medium, hard, impoppable): ").lower()
        if game_difficulty in game_difficulty_modes:
            break
        else:
            print("Invalid difficulty. Choose: easy, medium, hard, or impoppable")

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

    # Get the boss's HP based on boss, difficulty, and stage
    if boss == "bloonarius":
        base_hp = bloonarius_hp[boss_difficulty][stage]
    elif boss == "lych":
        base_hp = lych_hp[boss_difficulty][stage]
    elif boss == "vortex":
        base_hp = vortex_hp[boss_difficulty][stage]
    elif boss == "phaze":
        base_hp = phaze_hp[boss_difficulty][stage]
    elif boss == "dreadbloon":
        base_hp = dreadbloon_hp[boss_difficulty][stage]
    elif boss == "blastapopoulos":
        base_hp = blastapopoulos_hp[boss_difficulty][stage]

    # Apply health modifier
    if boss == "dreadbloon":
        modified_lead_hp = int(base_hp["lead"] * (Health / 100))
        modified_regular_hp = int(base_hp["regular"] * (Health / 100))
        total_hp = modified_lead_hp + modified_regular_hp
        print(f"\n{boss} ({boss_difficulty}) Stage {stage}:")
        print(f"Lead HP: {modified_lead_hp:,} (needs lead popping)")
        print(f"Regular HP: {modified_regular_hp:,}")
        print(f"Total HP to destroy: {total_hp:,}")
    else:
        modified_hp = int(base_hp * (Health / 100))
        print(f"\n{boss} ({boss_difficulty}) Stage {stage} HP: {modified_hp:,}")

    print("\n[Strategy calculation coming soon...]")

def main_menu():
    """Main menu system"""
    while True:
        print("\n" + "="*40)
        print("Boss calc")
        print("="*40)
        print("1. Start new boss fight")
        print("2. Calculate mid boss")
        print("3. Quit")
        print("="*40)
        
        choice = input("\nChoose an option (1-3): ").strip()
        
        if choice == "1":
            print("\nStarting new calculation...\n")
            boss_calculation()
        elif choice == "2":
            print("\n[Continue feature coming soon...]")
            print("For now, starting new calculation...\n")
            boss_calculation()
        elif choice == "3":
            print("\nbuh bye!!!")
            exit()
        else:
            print("\nInvalid choice. Please enter 1, 2, or 3.")

# Start the program
if __name__ == "__main__":
    main_menu()
