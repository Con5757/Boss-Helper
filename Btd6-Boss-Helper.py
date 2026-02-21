# con made ts cus im ass at boss events but ik how to make computers do things for me

Bosses = ["vortex", "phaze", "lych", "blastapopoulos", "dreadbloon", "bloonarius"]

#maps; WATER; false, small, mid, lots
maps = {

    ### beginner

    "monkey meadow": {
        "water": False,
        "rbs": 32.745
    },
    "in the loop": {
        "water": "small",
        "rbs": 44.390
    },
    "three mines round": {
        "water": "small",
        "rbs": 48.52
    },
    "spa pits": {
        "water": "lots",
        "rbs": 57.140
    },
    "tinkerton": {
        "water": "mid",
        "rbs": 44.39
    },
    "tree stump": {
        "water": False,
        "rbs": 44.265
    },
    "town center": {
        "water": "mid",
        "rbs": 34.650
    },
    "middle of the road": {
        "water": "small",
        "rbs": 45.20
    },
    "one two tree": {
        "water": False,
        "rbs": 43.88
    },
    "scrapyard": {
        "water": False,
        "rbs": 60.730
    },
    "the cabin": {
        "water": "lots",
        "rbs": 34.645
    },
    "resort": {
        "water": "mid",
        "rbs": 54.330
    },
    "skates": {
        "water": "lots",
        "rbs": 42.980
    },
    "lotus island": {
        "water": "lots",
        "rbs": 37.195
    },
    "candy falls": {
        "water": "lots",
        "rbs": 47.915
    },
    "winter park": {
        "water": "small",
        "rbs": 41.050
    },
    "carved": {
        "water": "mid",
        "rbs": 44.670
    },
    "park path": {
        "water": "mid",
        "rbs": 40.215
    },
    "alpine run": {
        "water": False,
        "rbs": 36.550
    },
    "frozen over": {
        "water": "mid",  
        "rbs": 40.370
    },
    "cubism": {
        "water": "lots",
        "rbs": 49.215
    },
    "four circles": {
        "water": "mid",
        "rbs": 41.415
    },
    "hedge": {
        "water": False,
        "rbs": 43.775
    },
    "end of the road": {
        "water": "mid",
        "rbs": 30.045
    },
    "logs": {
        "water": "small",
        "rbs": 60.330
    },

    ### inter

    "lost crevasse": {
        "water": "mid",
        "rbs": 24.68 
    },
    "luminous cove": {
        "water": "lots",
        "rbs": 32.20
    },
    "sulfur springs": {
        "water":"mid",
        "rbs": 37.25 
    },
    "water park": {
        "water": "lots",
        "rbs": 30.52 
    },
    "polyphemus": {
        "water": "lots",
        "rbs": 21.94                                                                             
    },
    "covered garden": {
        "water":,
        "rbs":
    },
    "quarry": {
        "water":,
        "rbs":
    },
    "quiet street": {
        "water":,
        "rbs":
    },
    "bloonarius prime": {
        "water":,
        "rbs":
    },
    "balance": {
        "water":,
        "rbs":
    },
    "encrypted": {
        "water":,
        "rbs":
    },
    "bazaar": {
        "water":,
        "rbs":
    },
    "adoras temple": {
        "water":,
        "rbs":
    },
    "spring spring": {
        "water":,
        "rbs":
    },
    "kartsndarts": {
        "water":,
        "rbs":
    },
    "moon landing": {
        "water":,
        "rbs":
    },
    "haunted": {
        "water":,
        "rbs":
    },
    "downstream": {
        "water":,
        "rbs":
    },
    "firing range": {
        "water":,
        "rbs":
    },
    "cracked": {
        "water":,
        "rbs":
    },
    "steambed": {
        "water":,
        "rbs":
    },
    "chutes": {
        "water":,
        "rbs":
    },
    "rake": {
        "water":,
        "rbs":
    },
    "spice islands": {
        "water":,
        "rbs":
    },

    ### advanced

    "": {
        "water":,
        "rbs":
    },

}

boss_speedmulti = {
    "bloonarius": {
        "normal": [0.05, 0.05, 0.05, 0.06, 0.06],
        "elite": [0.05, 0.05, 0.05, 0.06, 0.06]
    },
    "lych": {
        "normal": [0.092, 0.092, 0.10, 0.108, 0.108],
        "elite": [0.10, 0.108, 0.116, 0.12, 0.124]
    },
    "vortex": {
        "normal": [0.144, 0.114, 0.156, 0.162, 0.1680],
        "elite": [0.15, 0.162, 0.18, 0.186, 0.192]
    },
    "phaze": {
        "normal": [0.0468, 0.0468, 0.0504, 0.0522, 0.0522],
        "elite": [0.0522, 0.052, 0.0558, 0.0576, 0.0596]
    },
    "dreadbloon": {
        "normal": [0.05, 0.05, 0.05, 0.06, 0.06],
        "elite": [0.052, 0.052, 0.052, 0.06, 0.06]
    },
    "blastapopoulos": {
        "normal": [0.0440, 0.0462, 0.0508, 0.0584, 0.0731],
        "elite": [0.0440, 0.0462, 0.0508, 0.0584, 0.0731]
    },
}

bloonarius_hp = {
    "normal": {1: 20000, 2: 75000, 3: 350000, 4: 750000, 5: 3000000},
    "elite":  {1: 50000, 2: 300000, 3: 2000000, 4: 8000000, 5: 40000000}
}
lych_hp = {
    "normal": {1: 14000, 2: 52500, 3: 220000, 4: 525000, 5: 2100000},
    "elite":  {1: 30000, 2: 180000, 3: 1100000, 4: 4800000, 5: 24000000}
}
vortex_hp = {
    "normal": {1: 20000, 2: 62800, 3: 294000, 4: 628000, 5: 2512500},
    "elite":  {1: 41800, 2: 251000, 3: 1675000, 4: 6700000, 5: 33500000}
}
phaze_hp = {
    "normal": {1: 11750, 2: 43750, 3: 200000, 4: 437500, 5: 1812500},
    "elite":  {1: 23750, 2: 137500, 3: 875000, 4: 3875000, 5: 19375000}
}
dreadbloon_hp = {
    "normal": {
        1: {"lead": 7500,    "regular": 3750},
        2: {"lead": 25000,   "regular": 12500},
        3: {"lead": 120000,  "regular": 60000},
        4: {"lead": 260000,  "regular": 130000},
        5: {"lead": 1000000, "regular": 500000}
    },
    "elite": {
        1: {"lead": 15000,    "regular": 7500},
        2: {"lead": 90000,    "regular": 45000},
        3: {"lead": 650000,   "regular": 325000},
        4: {"lead": 2625000,  "regular": 1312500},
        5: {"lead": 12500000, "regular": 6250000}
    }
}
blastapopoulos_hp = {
    "normal": {1: 17500, 2: 65000, 3: 300000, 4: 650000, 5: 3000000},
    "elite":  {1: 43000, 2: 270000, 3: 1700000, 4: 7000000, 5: 35000000}
}

difficulty_multipliers = {
    "easy":       0.85,
    "medium":     1.0,
    "hard":       1.08,
    "impoppable": 1.20
}
sell_multiplier = 0.70

primary_monkeys = {
    "dart monkey": {
        "name": "dart monkey",
        "base_cost": 200,
        "category": "primary",
        "base_stats": {
            "damage": 1,
            "attack_speed": 1.0,
            "pierce": 2,
            "range": 32,
            "camo": False,
            "lead": False,
        },
        "upgrades": {
            "top":    [140, 200, 320, 1800, 15000],
            "middle": [100, 190, 450, 7200, 45000],
            "bottom": [90, 200, 575, 2050, 21500]
        },
        "upgrade_stats": {
            "top": {
                1: {"pierce": +1},
                2: {"pierce": +2},
                3: {"damage": 2, "pierce": 19, "attack_speed": 1.15},
                4: {"damage": 2, "pierce": 61, "attack_speed": 1.0, "lead": True},
                5: {"damage": 5, "pierce": 210, "attack_speed": 1.0}
            },
            "middle": {
                1: {"attack_speed": 0.85},
                2: {"attack_speed": 0.67},
                3: {"attack_speed": 0.474, "projectiles": 3},
                4: {"attack_speed": 0.24},
                5: {}
            },
            "bottom": {
                1: {"range": +8},
                2: {"range": +8, "camo": True},
                3: {"damage": 3, "range": 60, "attack_speed": 0.95},
                4: {"damage": 6, "attack_speed": 0.475},
                5: {"damage": 8, "attack_speed": 0.2375, "pierce": 8, "range": 80, "lead": True, "camo": True}
            }
        },
        "special_properties": {
            "lead_popping": "4-x-x or 0-0-5",
            "camo_detection": "0-0-2",
            "notes": "Crossbow Master can pop any bloon type. Crits every 5 shots at tier 5."
        }
    },

    "boomerang monkey": {
        "name": "boomerang monkey",
        "base_cost": 315,
        "category": "primary",
        "base_stats": {
            "damage": 1,
            "attack_speed": 0.8,
            "pierce": 4,
            "range": 43,
            "camo": False,
            "lead": False,
        },
        "upgrades": {
            "top":    [200, 280, 600, 2000, 32500],
            "middle": [175, 250, 1250, 4200, 35000],
            "bottom": [100, 300, 1300, 2200, 50000]
        },
        "upgrade_stats": {
            "top": {
                1: {"pierce": +4},
                2: {"pierce": +5},
                3: {"pierce": 30, "bounce": True},
                4: {"pierce": 60, "attack_speed": 0.267},
                5: {"damage": 2, "moab_dot": True}
            },
            "middle": {
                1: {"attack_speed": 0.6},
                2: {"attack_speed": 0.45},
                3: {"attack_speed": 0.125, "moab_damage": +1},
                4: {"ability": "turbo_charge"},
                5: {"damage": 4, "permanent_turbo": True}
            },
            "bottom": {
                1: {"range": +14},
                2: {"lead": True, "damage": +1},
                3: {"pierce": 18, "straight_path": True},
                4: {"moab_knockback": True},
                5: {"damage": +10, "pierce": +100}
            }
        },
        "special_properties": {
            "lead_popping": "0-0-2",
            "camo_detection": None,
            "notes": "Red Hot Rangs (0-0-2) gives lead popping. MOAB Press has knockback."
        }
    },

    "bomb shooter": {
        "name": "bomb shooter",
        "base_cost": 525,
        "category": "primary",
        "base_stats": {
            "damage": 1,
            "attack_speed": 1.5,
            "pierce": 22,
            "range": 42,
            "camo": False,
            "lead": True,
            "black": False,
        },
        "upgrades": {
            "top":    [250, 650, 1100, 2800, 55000],
            "middle": [250, 400, 1000, 3450, 28000],
            "bottom": [200, 300, 700, 2500, 23000]
        },
        "upgrade_stats": {
            "top": {
                1: {"pierce": +6},
                2: {"damage": 2, "pierce": +10},
                3: {"damage": 4, "pierce": 80},
                4: {"stun": 1.4},
                5: {"damage": 24, "black": True, "stun": 2.0}
            },
            "middle": {
                1: {"attack_speed": 1.125},
                2: {"attack_speed": 0.824, "range": +4},
                3: {"moab_damage": 16},
                4: {"moab_damage": 31, "ceramic_damage": 5, "range": +5},
                5: {"moab_damage": 100}
            },
            "bottom": {
                1: {"range": +12},
                2: {"range": +2, "frags": 8},
                3: {"cluster": 8},
                4: {"damage": 2},
                5: {"damage": 5, "attack_speed": 0.9}
            }
        },
        "special_properties": {
            "lead_popping": "base",
            "camo_detection": None,
            "black_popping": "5-0-0",
            "notes": "Cannot pop Black/Zebra/DDT normally. No camo detection ever."
        }
    },

    "tack shooter": {
        "name": "tack shooter",
        "base_cost": 260,
        "category": "primary",
        "base_stats": {
            "damage": 1,
            "attack_speed": 1.12,
            "pierce": 1,
            "projectiles": 8,
            "range": 23,
            "camo": False,
            "lead": False,
        },
        "upgrades": {
            "top":    [150, 300, 600, 3500, 45500],
            "middle": [100, 225, 550, 2700, 15000],
            "bottom": [110, 110, 450, 3200, 20000]
        },
        "upgrade_stats": {
            "top": {
                1: {"attack_speed": 0.84},
                2: {"attack_speed": 0.63},
                3: {"damage": 2, "lead": True},
                4: {"damage": 5, "pierce": 30, "attack_speed": 0.315, "purple": False},
                5: {"damage": 8, "moab_damage": +4, "pierce": 45, "range": 35}
            },
            "middle": {
                1: {"range": +4},
                2: {"pierce": +3, "range": +4},
                3: {"pierce": 8, "range": +15},
                4: {"damage": 2},
                5: {"damage": 5, "lead": True}
            },
            "bottom": {
                1: {"projectiles": 10},
                2: {"projectiles": 12},
                3: {"projectiles": 16, "pierce": +1},
                4: {"attack_speed_multiplier": 3.0},
                5: {"projectiles": 32, "attack_speed": 0.6, "range": +7}
            }
        },
        "special_properties": {
            "lead_popping": "3-0-0",
            "camo_detection": None,
            "purple_immune": "4-0-0",
            "notes": "Very short range. Ring of Fire cannot pop Purple. Super Maelstrom pops lead."
        }
    },

    "glue gunner": {
        "name": "glue gunner",
        "base_cost": 225,
        "category": "primary",
        "base_stats": {
            "damage": 0,
            "attack_speed": 1.0,
            "pierce": 1,
            "range": 45,
            "camo": False,
            "lead": False,
            "slow": 0.50,
            "slow_duration": 11.0
        },
        "upgrades": {
            "top":    [200, 300, 2000, 5000, 22500],
            "middle": [100, 970, 1950, 4000, 16000],
            "bottom": [280, 400, 3600, 4000, 24000]
        },
        "upgrade_stats": {
            "top": {
                1: {"soak": "all_layers"},
                2: {"damage": 1, "dot": 2.0},
                3: {"damage": 1, "dot": 0.5, "pierce": +1, "attack_speed": 0.5},
                4: {"damage": 1, "dot": 0.1},
                5: {"damage": 8, "dot": 0.1, "ceramic_damage": 8, "moab_damage": 6}
            },
            "middle": {
                1: {"pierce": +1},
                2: {"pierce": 5},
                3: {"attack_speed_multiplier": 3.0},
                4: {"ability": "glue_strike"},
                5: {"ability": "glue_storm"}
            },
            "bottom": {
                1: {"slow_duration": 24.0},
                2: {"slow": 0.75},
                3: {"moab_slow": 0.375},
                4: {"stun_on_pop": True},
                5: {"slow": 0.95, "stun": True}
            }
        },
        "special_properties": {
            "lead_popping": None,
            "camo_detection": None,
            "notes": "Support tower. Cannot slow BADs ever. Glue Strike/Storm debuff MOAB-class."
        }
    },

    "ice monkey": {
        "name": "ice monkey",
        "base_cost": 400,
        "category": "primary",
        "base_stats": {
            "damage": 1,
            "attack_speed": 2.4,
            "pierce": 40,
            "range": 20,
            "camo": False,
            "lead": False,
            "freeze_duration": 1.5,
            "water_placement": True
        },
        "upgrades": {
            "top":    [150, 350, 1500, 2300, 28000],
            "middle": [200, 300, 2750, 4000, 16000],
            "bottom": [150, 200, 1900, 2750, 30000]
        },
        "upgrade_stats": {
            "top": {
                1: {"slow_after_thaw": 0.50},
                2: {"lead": True, "camo": True},
                3: {"shards": 3, "range": +5},
                4: {"moab_target": True, "brittle": +1},
                5: {"brittle": +4, "attack_speed": 1.2, "moab_slow": 0.25}
            },
            "middle": {
                1: {"attack_speed": 1.8, "freeze_duration": 1.75},
                2: {"pierce": 45, "freeze_duration": 2.2},
                3: {"slow_aura": 0.40, "water_freeze": True},
                4: {"range": 30, "ability": "snowstorm"},
                5: {"pierce": 300, "range": 40, "freeze_all": True}
            },
            "bottom": {
                1: {"range": +7},
                2: {"refreeze": True},
                3: {"damage": 2, "range": 46, "projectile": True},
                4: {"moab_damage": +8, "icicles": True},
                5: {"moab_damage": 50, "freeze_moab": True}
            }
        },
        "special_properties": {
            "lead_popping": "1-0-2",
            "camo_detection": "1-0-2",
            "water_placement": True,
            "notes": "Arctic Wind (0-3-0) lets land towers be placed on nearby water."
        }
    },

    "desperado": {
        "name": "desperado",
        "base_cost": 300,
        "category": "primary",
        "base_stats": {
            "damage": 1,
            "attack_speed": 0.1,
            "reload_time": 1.2,
            "pierce": 1,           # Unbuffable
            "range": 60,
            "camo": False,
            "lead": False,
        },
        "upgrades": {
            "top":    [200, 200, 1200, 5800, 16500],
            "middle": [150, 350, 3000, 6500, 42000],
            "bottom": [220, 280, 2100, 6500, 31000]
        },
        "upgrade_stats": {
            "top": {
                1: {"attack_speed_bonus": "distance_based"},
                2: {"attack_speed_bonus": "fewer_bloons"},
                3: {"damage": 2, "magazine": 6},
                4: {"damage": 6, "magazine": 12},
                5: {"fire_dot": 75, "fire_duration": 12}
            },
            "middle": {
                1: {"camo": True},
                2: {"crit_chance": 0.025, "crit_multiplier": 4},
                3: {"lead": True, "rifle": True, "rifle_damage": 10},
                4: {"ability": "marked_to_pop"},
                5: {"rifle_damage": 280, "pierce": "infinite"}
            },
            "bottom": {
                1: {"attack_speed_bonus": "fewer_towers"},
                2: {"attack_speed_bonus": "more_bloons"},
                3: {"shotgun": True, "knockback": True},
                4: {"moab_knockback": True},
                5: {"shotgun_damage": "high"}
            }
        },
        "special_properties": {
            "lead_popping": "0-3-0",
            "camo_detection": "0-1-0",
            "notes": "Pierce is unbuffable. Can generate income. Requires 3.5M pops to unlock. Added v49.0."
        }
    }
}

military_monkeys = {
    "sniper monkey": {
        "name": "sniper monkey",
        "base_cost": 350,
        "category": "military",
        "base_stats": {
            "damage": 2,
            "attack_speed": 1.64,
            "pierce": 1,
            "range": "infinite",
            "camo": False,
            "lead": False,
        },
        "upgrades": {
            "top":    [350, 1300, 2500, 6000, 32000],
            "middle": [250, 450, 2400, 7600, 14500],
            "bottom": [450, 450, 2900, 4100, 14700]
        },
        "upgrade_stats": {
            "top": {
                1: {"damage": 4, "lead": True},
                2: {"damage": 7},
                3: {"damage": 20, "ceramic_damage": +15},
                4: {"damage": 30, "moab_stun": True},
                5: {"damage": 140, "moab_vulnerable": +5}
            },
            "middle": {
                1: {"camo": True, "camo_damage": +2},
                2: {"shrapnel": 5},
                3: {"bounce": 3},
                4: {"lead": True, "pierce": 5, "ability": "supply_drop"},
                5: {"attack_speed": 0.4, "ability": "elite_sniper"}
            },
            "bottom": {
                1: {"attack_speed": 1.15},
                2: {"attack_speed": 0.80},
                3: {"attack_speed": 0.267},
                4: {"attack_speed": 0.133, "moab_damage": +2},
                5: {"attack_speed": 0.066, "moab_damage": +4}
            }
        },
        "special_properties": {
            "lead_popping": "1-0-0 or 0-4-0",
            "camo_detection": "0-1-0",
            "notes": "Infinite range but blocked by Line of Sight. Elite Sniper buffs all snipers on screen."
        }
    },

    "monkey sub": {
        "name": "monkey sub",
        "base_cost": 325,
        "category": "military",
        "base_stats": {
            "damage": 1,
            "attack_speed": 0.75,
            "pierce": 2,
            "range": 42,
            "camo": False,
            "lead": False,
            "water_only": True
        },
        "upgrades": {
            "top":    [130, 500, 700, 2300, 31000],
            "middle": [450, 300, 1350, 13000, 32000],
            "bottom": [450, 1000, 1100, 3000, 25000]
        },
        "upgrade_stats": {
            "top": {
                1: {"range": +10},
                2: {"range": "infinite_via_towers"},
                3: {"camo_decamo": True},
                4: {"damage": 2, "cooldown_reduction": 0.15},
                5: {"damage": 5, "cooldown_reduction": 0.20, "hero_xp": 1.5}
            },
            "middle": {
                1: {"pierce": 5},
                2: {"lead": True},
                3: {"moab_damage": 6, "ceramic_damage": 6, "range": +8},
                4: {"ability": "first_strike"},
                5: {"ability": "pre_emptive_strike", "moab_damage": 750}
            },
            "bottom": {
                1: {"attack_speed": 0.375},
                2: {"split_darts": 3},
                3: {"attack_speed": 0.25},
                4: {"damage": 2, "moab_damage": 4},
                5: {"damage_multiplier": 2, "pierce": +4}
            }
        },
        "special_properties": {
            "lead_popping": "0-2-0",
            "camo_detection": "submerge or advanced_intel",
            "water_only": True,
            "notes": "Water only. Energizer reduces ALL tower cooldowns and boosts hero XP. Sub Commander buffs all nearby subs."
        }
    },

    "monkey buccaneer": {
        "name": "monkey buccaneer",
        "base_cost": 400,
        "category": "military",
        "base_stats": {
            "damage": 1,
            "attack_speed": 1.0,
            "pierce": 2,
            "range": 60,
            "camo": False,
            "lead": False,
            "water_only": True
        },
        "upgrades": {
            "top":    [275, 425, 3050, 8000, 24500],
            "middle": [550, 500, 900, 4900, 26000],
            "bottom": [200, 350, 2400, 5500, 23000]
        },
        "upgrade_stats": {
            "top": {
                1: {"attack_speed": 0.75},
                2: {"projectiles": +1},
                3: {"attack_speed": 0.15},
                4: {"planes": 3, "moab_missiles": True},
                5: {"buff_water_towers": 0.85, "land_placement": True}
            },
            "middle": {
                1: {"grapes": 5},
                2: {"lead": True, "fire_dot": True},
                3: {"cannon": True, "damage": 2},
                4: {"ability": "moab_takedown"},
                5: {"hooks": 6, "ability": "pirate_lord"}
            },
            "bottom": {
                1: {"range": +11, "pierce": +2},
                2: {"camo": True},
                3: {"income": 200},
                4: {"income": 500, "attack_speed": 0.5},
                5: {"income": 800, "buff_merchantmen": True}
            }
        },
        "special_properties": {
            "lead_popping": "0-2-0",
            "camo_detection": "0-0-2",
            "water_only": True,
            "notes": "Water only. Merchantman generates income. Pirate Lord instakills MOABs. Hot Shot loses purple."
        }
    },

    "monkey ace": {
        "name": "monkey ace",
        "base_cost": 800,
        "category": "military",
        "base_stats": {
            "damage": 1,
            "attack_speed": 1.68,
            "pierce": 5,
            "projectiles": 8,
            "range": "map_wide",
            "camo": False,
            "lead": False,
        },
        "upgrades": {
            "top":    [650, 650, 1000, 3000, 41000],
            "middle": [200, 350, 900, 18000, 30000],
            "bottom": [500, 300, 2800, 23400, 85000]
        },
        "upgrade_stats": {
            "top": {
                1: {"attack_speed": 1.26},
                2: {"projectiles": 12},
                3: {"moab_missiles": 18},
                4: {"projectiles": 16, "attack_speed": 0.63},
                5: {"projectiles": 32, "damage": 3, "ceramic_damage": +2, "lead": True, "black": True}
            },
            "middle": {
                1: {"pineapples": True},
                2: {"camo": True, "camo_damage": 2},
                3: {"bombs": 4, "damage": 3},
                4: {"ability": "ground_zero", "bomb_damage": 15},
                5: {"ability": "tsar_bomba", "bomb_damage": 20}
            },
            "bottom": {
                1: {"pierce": 8},
                2: {"flight_path": "centered"},
                3: {"seeking": True},
                4: {"rapid_darts": 8, "rapid_bombs": 3},
                5: {"attack_speed": 0.66, "all_bloons": True}
            }
        },
        "special_properties": {
            "lead_popping": "5-0-0",
            "camo_detection": "0-2-0",
            "notes": "Flies in patterns around runway. Sky Shredder and Flying Fortress pop all bloon types."
        }
    },

    "heli pilot": {
        "name": "heli pilot",
        "base_cost": 1600,
        "category": "military",
        "base_stats": {
            "damage": 1,
            "attack_speed": 0.57,
            "pierce": 3,
            "projectiles": 2,
            "range": 42,
            "camo": False,
            "lead": False,
        },
        "upgrades": {
            "top":    [800, 500, 1750, 19600, 45000],
            "middle": [300, 600, 3500, 10500, 30000],
            "bottom": [250, 350, 3000, 8500, 35000]
        },
        "upgrade_stats": {
            "top": {
                1: {"projectiles": 4},
                2: {"pursuit": True},
                3: {"rotors": True, "rotor_damage": 2, "lead": True},
                4: {"missiles": 4, "machine_gun": True},
                5: {"laser": True, "laser_damage": 6, "missile_damage": 17}
            },
            "middle": {
                1: {"speed": +75},
                2: {"camo": True},
                3: {"downdraft": True},
                4: {"ability": "support_chinook", "damage": 2},
                5: {"ability": "special_poperations"}
            },
            "bottom": {
                1: {"dart_speed": +30},
                2: {"attack_speed": 0.456},
                3: {"moab_shove": True, "lead": True},
                4: {"mini_comanches": 3},
                5: {"mini_comanches": 3, "permanent": True}
            }
        },
        "special_properties": {
            "lead_popping": "1-0-3",
            "camo_detection": "0-2-0",
            "notes": "Mobile tower. Hard/Impoppable costs incomplete from wiki. Apache Prime is highest DPS. Support Chinook can redeploy towers."
        }
    },

    "mortar monkey": {
        "name": "mortar monkey",
        "base_cost": 600,
        "category": "military",
        "base_stats": {
            "damage": 2,
            "attack_speed": 2.0,
            "pierce": 25,
            "range": "map_wide",
            "camo": False,
            "lead": True,
            "black": False,
        },
        "upgrades": {
            "top":    [500, 500, 900, 6500, 36000],
            "middle": [300, 500, 900, 5500, 32000],
            "bottom": [200, 500, 900, 10500, 40000]
        },
        "upgrade_stats": {
            "top": {
                1: {"pierce": 45, "blast_radius": 28},
                2: {"damage": 3},
                3: {"shockwave": True, "blast_radius": 38},
                4: {"damage": 10, "pierce": 85, "blast_radius": 58},
                5: {"damage": 25, "ceramic_damage": +30, "moab_damage": +30, "pierce": 200}
            },
            "middle": {
                1: {"attack_speed": 1.5},
                2: {"attack_speed": 1.08},
                3: {"black": True, "ceramic_damage": +3, "attack_speed": 0.81},
                4: {"attack_speed": 0.27, "ability": "bombardment"},
                5: {"ability": "pop_and_awe", "stun_all": True}
            },
            "bottom": {
                1: {"accuracy": +10},
                2: {"dot": 1.25},
                3: {"camo": True, "decamo": True},
                4: {"strip_properties": True, "moab_burn": 25},
                5: {"burn_damage": 100, "moab_burn": 100}
            }
        },
        "special_properties": {
            "lead_popping": "base",
            "camo_detection": "0-0-3",
            "black_popping": "0-3-0",
            "notes": "Map-wide range. Inaccurate by default. Cannot pop Black/Zebra without Heavy Shells. Pop and Awe stuns all bloons repeatedly."
        }
    },

    "dartling gunner": {
        "name": "dartling gunner",
        "base_cost": 850,
        "category": "military",
        "base_stats": {
            "damage": 1,
            "attack_speed": 0.2,
            "pierce": 1,
            "range": "aimed",
            "camo": False,
            "lead": False,
        },
        "upgrades": {
            "top":    [300, 900, 3750, 11000, 80000],
            "middle": [250, 950, 4800, 5550, 60000],
            "bottom": [150, 1200, 3400, 12000, 58000]
        },
        "upgrade_stats": {
            "top": {
                1: {"accuracy": +60},
                2: {"dot": 1.0, "shock": True},
                3: {"damage": 2, "pierce": 6, "lead": True, "purple": False},
                4: {"beam": True, "damage": "endpoint_focused"},
                5: {"pierce": 1000, "damage": "extreme"}
            },
            "middle": {
                1: {"camo": True},
                2: {"attack_speed": 0.132},
                3: {"rockets": True, "all_bloons": True},
                4: {"ability": "rocket_storm"},
                5: {"moab_damage": 550, "attack_speed": 0.6}
            },
            "bottom": {
                1: {"rotation_speed": 2},
                2: {"pierce": +2, "lead": True},
                3: {"damage": 4, "pierce": 4, "knockback": True},
                4: {"barrels": 4, "attack_speed_multiplier": 4},
                5: {"barrels": 6, "damage": 8, "pierce": 6}
            }
        },
        "special_properties": {
            "lead_popping": "1-0-3",
            "camo_detection": "0-1-0",
            "purple_immune": "1-0-3",
            "notes": "Player aimed tower. M.A.D is strongest anti-MOAB tower. Requires 3M pops to unlock."
        }
    }
}

magic_monkeys = {
    "wizard monkey": {
        "name": "wizard monkey",
        "base_cost": 250,
        "category": "magic",
        "base_stats": {
            "damage": 1,
            "attack_speed": 1.1,
            "pierce": 3,
            "range": 40,
            "camo": False,
            "lead": False,
            "purple": False,
        },
        "upgrades": {
            "top":    [175, 450, 1450, 10000, 32000],
            "middle": [300, 800, 3300, 6000, 50000],
            "bottom": [300, 300, 1500, 2800, 26500]
        },
        "upgrade_stats": {
            "top": {
                1: {"seeking": True},
                2: {"damage": 2},
                3: {"damage": 3, "pierce": +4, "attack_speed": 0.55, "range": +20},
                4: {"damage": 6, "moab_damage": 16, "lead": True},
                5: {"damage": 8, "moab_damage": 27}
            },
            "middle": {
                1: {"fireball": True, "lead": True},
                2: {"wall_of_fire": True},
                3: {"dragon_breath": True, "damage": 2},
                4: {"ability": "summon_phoenix"},
                5: {"ability": "wizard_lord_phoenix", "permanent_phoenix": True}
            },
            "bottom": {
                1: {"pierce": +5},
                2: {"camo": True, "range": +10},
                3: {"decamo": True, "range": +10},
                4: {"undead": True},
                5: {"undead_moab": True, "range": 80}
            }
        },
        "special_properties": {
            "lead_popping": "0-1-0 or 1-0-4",
            "camo_detection": "0-0-2",
            "purple_immune": "base",
            "notes": "Cannot pop purple at base or with fire upgrades. Archmage inherits Dragon's Breath and Shimmer."
        }
    },

    "super monkey": {
        "name": "super monkey",
        "base_cost": 2500,
        "category": "magic",
        "base_stats": {
            "damage": 1,
            "attack_speed": 0.045,
            "pierce": 1,
            "range": 48,
            "camo": False,
            "lead": False,
            "purple": True,
        },
        "upgrades": {
            "top":    [2000, 2500, 20000, 100000, 500000],
            "middle": [1500, 1900, 7500, 25000, 70000],
            "bottom": [3000, 1200, 5600, 55555, 165650]
        },
        "upgrade_stats": {
            "top": {
                1: {"pierce": +1, "lead": False, "purple": False},
                2: {"attack_speed": 0.03, "lead": True},
                3: {"beams": 3, "pierce": 6},
                4: {"sacrifice": True},
                5: {"sacrifice": True, "ultimate": True}
            },
            "middle": {
                1: {"range": +10, "pierce": +1},
                2: {"range": +12, "pierce": +2},
                3: {"dual_guns": True, "crit": 10},
                4: {"ability": "annihilation", "damage": 2600},
                5: {"ability": "annihilation", "damage": 10400, "all_bloons": True}
            },
            "bottom": {
                1: {"knockback": True},
                2: {"camo": True, "camo_damage": +1},
                3: {"moab_damage": +2, "pierce": +3},
                4: {"damage": +1, "attack_speed": 0.5, "all_bloons": True},
                5: {"black_hole": True, "damage": +8, "moab_damage": +16}
            }
        },
        "special_properties": {
            "lead_popping": "1-0-2",
            "camo_detection": "0-0-2",
            "purple_immune": "1-0-0",
            "notes": "Fastest attacking base tower. Laser Blasts loses lead AND purple. Most expensive base tower."
        }
    },

    "ninja monkey": {
        "name": "ninja monkey",
        "base_cost": 400,
        "category": "magic",
        "base_stats": {
            "damage": 1,
            "attack_speed": 0.62,
            "pierce": 2,
            "range": 40,
            "camo": True,
            "lead": False,
        },
        "upgrades": {
            "top":    [350, 350, 900, 2750, 35000],
            "middle": [250, 400, 1200, 5200, 22000],
            "bottom": [300, 450, 2250, 5000, 40000]
        },
        "upgrade_stats": {
            "top": {
                1: {"attack_speed": 0.434},
                2: {"pierce": +2},
                3: {"projectiles": 2},
                4: {"projectiles": 5},
                5: {"projectiles": 8, "damage": 2, "attack_speed": 0.192, "range": +10}
            },
            "middle": {
                1: {"blowback": 0.15},
                2: {"decamo": True},
                3: {"buff_ninjas": True},
                4: {"ability": "bloon_sabotage"},
                5: {"ability": "grand_saboteur", "moab_health": 0.75}
            },
            "bottom": {
                1: {"seeking": True, "range": +7},
                2: {"caltrops": True},
                3: {"flash_bomb": True, "lead": True, "black": True},
                4: {"sticky_bomb": True, "moab_damage": 450},
                5: {"sticky_bomb_damage": 3000, "moab_stun": True}
            }
        },
        "special_properties": {
            "lead_popping": "0-0-3",
            "camo_detection": "base",
            "notes": "One of only 2 base camo detectors. Shinobi Tactics stacks up to 20x. Grand Saboteur reduces incoming MOAB HP by 25%."
        }
    },

    "alchemist": {
        "name": "alchemist",
        "base_cost": 550,
        "category": "magic",
        "base_stats": {
            "damage": 1,
            "attack_speed": 2.0,
            "pierce": 15,
            "range": 42,
            "camo": False,
            "lead": True,
            "purple": True,
            "black": True,
            "white": True,
        },
        "upgrades": {
            "top":    [250, 350, 1250, 3000, 60000],
            "middle": [250, 475, 3000, 4500, 45000],
            "bottom": [650, 450, 1000, 2750, 40000]
        },
        "upgrade_stats": {
            "top": {
                1: {"splash": +5},
                2: {"buff_lead": True, "buff_ceramic": +1},
                3: {"buff_damage": +1, "buff_speed": 0.10, "buff_pierce": +2},
                4: {"buff_damage": +1, "buff_speed": 0.176, "buff_pierce": +3},
                5: {"permanent_buff": True}
            },
            "middle": {
                1: {"dot": 1.5},
                2: {"moab_damage": 5, "strip_fortified": True},
                3: {"moab_explosion": 0.10},
                4: {"ability": "transforming_tonic"},
                5: {"ability": "total_transformation", "transforms": 5}
            },
            "bottom": {
                1: {"attack_speed": 1.6},
                2: {"acid_pool": True},
                3: {"lead_instakill": True, "lead_cash": 50},
                4: {"goldify": True, "income": +100},
                5: {"shrink": True, "converts_to_red": True}
            }
        },
        "special_properties": {
            "lead_popping": "base",
            "camo_detection": None,
            "notes": "Pops any non-camo bloon type at base (Acid type). Permanent Brew is one of the best buffs in game."
        }
    },

    "druid": {
        "name": "druid",
        "base_cost": 400,
        "category": "magic",
        "base_stats": {
            "damage": 1,
            "attack_speed": 1.0,
            "pierce": 1,
            "projectiles": 5,
            "range": 35,
            "camo": False,
            "lead": False,
        },
        "upgrades": {
            "top":    [350, 850, 1700, 4500, 60000],
            "middle": [250, 350, 1050, 4900, 35000],
            "bottom": [100, 300, 600, 2500, 45000]
        },
        "upgrade_stats": {
            "top": {
                1: {"pierce": +1, "lead": True, "all_bloons": True},
                2: {"lightning": True, "lightning_damage": 2, "lightning_pierce": 31},
                3: {"tornado": True, "blowback": 24},
                4: {"ball_lightning": True},
                5: {"supertornado": True, "camo": True, "moab_blowback": True}
            },
            "middle": {
                1: {"projectiles": 8},
                2: {"strip_regrow": True},
                3: {"vine": True, "instakill_non_moab": True},
                4: {"ability": "jungles_bounty", "income": 320},
                5: {"vines_on_track": True, "income": 1000}
            },
            "bottom": {
                1: {"range": +10},
                2: {"attack_speed_on_lives_lost": True},
                3: {"attack_speed_on_damage": True},
                4: {"buff_druids": True},
                5: {"damage": 4, "damage_scales_with_rbe": True}
            }
        },
        "special_properties": {
            "lead_popping": "1-0-0",
            "camo_detection": "5-0-0",
            "notes": "No camo until tier 5 top. Poplust stacks up to 5x. Spirit of the Forest generates $1000/round. Avatar of Wrath scales with bloons on screen."
        }
    },

    "mermonkey": {
        "name": "mermonkey",
        "base_cost": 275,
        "category": "magic",
        "base_stats": {
            "damage": 2,
            "attack_speed": 1.2,
            "pierce": 2,
            "range": 28,
            "camo": False,
            "lead": False,
            "water_bonus_range": 35,
            "water_placement": True
        },
        "upgrades": {
            "top":    [150, 250, 1600, 4200, 23000],
            "middle": [200, 300, 2300, 8000, 52000],
            "bottom": [200, 280, 2000, 7600, 25000]
        },
        "upgrade_stats": {
            "top": {
                1: {"attack_speed": 1.02},
                2: {"attack_speed": 0.816},
                3: {"tentacles": 8, "tentacle_damage": 10, "pierce_buff": 0.10},
                4: {"tentacle_damage": 18, "slow": True, "pierce_buff": 0.20},
                5: {"tentacle_damage": 50, "pierce_buff": 0.40, "water_land": True}
            },
            "middle": {
                1: {"pierce": +4},
                2: {"freeze": 0.5, "lead": True},
                3: {"damage_scales_distance": True, "lead": True},
                4: {"ability": "ice_jet", "moab_slow": True},
                5: {"tridents": 3, "freeze_all": True}
            },
            "bottom": {
                1: {"camo": True, "seeking": True},
                2: {"range_buff_per_mermonkey": 0.10},
                3: {"spiral": True, "decamo": True, "dot_detonate": True},
                4: {"spiral_moab": True},
                5: {"spiral_bfb": True, "hero_buff": True, "magic_pierce": +3}
            }
        },
        "special_properties": {
            "lead_popping": "0-2-0",
            "camo_detection": "0-0-1",
            "water_placement": True,
            "notes": "Can be placed on land or water. Range +25% on water. Total cost table incomplete. Requires 3M pops to unlock."
        }
    }
}

support_monkeys = {

    "banana farm": {
        "name": "banana farm",
        "base_cost": 1250,
        "category": "support",
        "base_stats": {
            "damage": 0,
            "attack_speed": None,
            "pierce": None,
            "range": None,
            "camo": False,
            "lead": False,
            "income_per_round": 80,
        },
        "upgrades": {
            "top":    [500, 600, 3000, 19000, 115000],
            "middle": [300, 800, 3650, 7200, 100000],
            "bottom": [250, 400, 2700, 15000, 70000]
        },
        "upgrade_stats": {
            "top": {
                1: {"bananas": 6, "income": 120},
                2: {"bananas": 8, "income": 160},
                3: {"bananas": 16, "income": 320},
                4: {"crates": 5, "income": 1500},
                5: {"crates": 5, "income": 6000, "buff_brf": 1.25}
            },
            "middle": {
                1: {"banana_duration": 30},
                2: {"income_multiplier": 1.25},
                3: {"bank": True, "income": 225, "bank_limit": 7000, "interest": 0.15},
                4: {"bank_limit": 10000, "ability": "imf_loan", "loan": 9000},
                5: {"ability": "monkey_nomics", "loan_no_penalty": True}
            },
            "bottom": {
                1: {"autocollect": 0.50},
                2: {"autocollect": 0.85, "sell_bonus": 0.10},
                3: {"auto_income": True, "income": 320},
                4: {"income": 1120, "buff_merchantmen": 0.10},
                5: {"income": 5120, "lives_per_round": 15, "autocollect_radius": 75}
            }
        },
        "special_properties": {
            "lead_popping": None,
            "camo_detection": None,
            "notes": "Pure income tower. Bank stores up to $7000 with 15% interest. Banana Central buffs all BRFs by 25%. Central Market buffs Merchantmen up to 10x."
        }
    },

    "spike factory": {
        "name": "spike factory",
        "base_cost": 1000,
        "category": "support",
        "base_stats": {
            "damage": 1,
            "attack_speed": 1.75,
            "pierce": 5,
            "range": 40,
            "camo": True,
            "lead": False,
            "spike_duration": 50,
            "spike_rounds": 1
        },
        "upgrades": {
            "top":    [800, 600, 2300, 9500, 125000],
            "middle": [600, 800, 2500, 7000, 41000],
            "bottom": [150, 400, 1300, 3600, 30000]
        },
        "upgrade_stats": {
            "top": {
                1: {"pierce": 10},
                2: {"lead": True},
                3: {"damage": 2, "ceramic_damage": +3, "fortified_damage": +1},
                4: {"ceramic_damage": +6, "pierce": 18, "explosion_damage": 10},
                5: {"damage": 50, "pierce": 50, "attack_speed": 3.5, "explosion_damage": 1000}
            },
            "middle": {
                1: {"attack_speed": 1.4},
                2: {"attack_speed": 1.05},
                3: {"moab_damage": +7},
                4: {"ability": "spike_storm", "storm_piles": 200},
                5: {"auto_storm": 15, "storm_piles": 200}
            },
            "bottom": {
                1: {"range": +8, "spike_duration": 100},
                2: {"targeting": True, "round_start_burst": 3},
                3: {"spike_duration": 140, "spike_rounds": 2},
                4: {"damage": 3, "spike_rounds": 3},
                5: {"damage": 10, "pierce": 50, "spike_rounds": 4, "spike_duration": 300, "attack_speed": 6.06}
            }
        },
        "special_properties": {
            "lead_popping": "1-0-2",
            "camo_detection": "base",
            "notes": "One of only 2 base camo detectors. Spikes expire end of round by default. Perma-Spike lasts 4 rounds. Carpet of Spikes auto-storms every 15s."
        }
    },

    "monkey village": {
        "name": "monkey village",
        "base_cost": 1200,
        "category": "support",
        "base_stats": {
            "damage": 0,
            "attack_speed": None,
            "pierce": None,
            "range": 40,
            "camo": False,
            "lead": False,
            "range_buff": 0.10
        },
        "upgrades": {
            "top":    [400, 1500, 800, 2500, 25000],
            "middle": [250, 1700, 5000, 23500, 45000],
            "bottom": [500, 500, 1500, 7200, 15000]  # Monkeyopolis cost varies
        },
        "upgrade_stats": {
            "top": {
                1: {"radius": +8},
                2: {"attack_speed_buff": 0.85},
                3: {"primary_range": 0.10, "primary_pierce": 0.15, "primary_proj_speed": 0.25},
                4: {"primary_free_t1": True, "ability_cooldown": 0.80},
                5: {"primary_free_t1_t2": True, "primary_pierce": 0.40, "ballista": True}
            },
            "middle": {
                1: {"block_regrow": True},
                2: {"camo_buff": True},
                3: {"all_bloons_buff": True},
                4: {"ability": "call_to_arms", "attack_speed": 1.5, "pierce": 1.5},
                5: {"ability": "homeland_defense", "attack_speed": 2.0, "pierce": 2.0, "global": True}
            },
            "bottom": {
                1: {"discount": 0.10},
                2: {"discount": 0.15},
                3: {"income": 400},
                4: {"income": 1600, "range": +10},
                5: {"income": 1600, "absorbs_farms": True, "eco_bonus": 0.20}
            }
        },
        "special_properties": {
            "lead_popping": None,
            "camo_detection": None,
            "mib": "0-3-0",
            "notes": "MIB (0-3-0) is critical for Dreadbloon. Homeland Defense doubles all tower attack speed and pierce globally. Radar Scanner gives all nearby towers camo detection."
        }
    },

    "engineer monkey": {
        "name": "engineer monkey",
        "base_cost": 350,
        "category": "support",
        "base_stats": {
            "damage": 1,
            "attack_speed": 0.70,
            "pierce": 3,
            "range": 40,
            "camo": False,
            "lead": False,
        },
        "upgrades": {
            "top":    [500, 400, 575, 2500, 32000],
            "middle": [250, 350, 900, 13500, 72000],
            "bottom": [450, 220, 450, 3600, 45000]
        },
        "upgrade_stats": {
            "top": {
                1: {"sentry": True, "sentry_duration": 25},
                2: {"production_speed": 0.60},
                3: {"attack_speed": 0.5},
                4: {"specialized_sentries": 4},
                5: {"plasma_sentries": True}
            },
            "middle": {
                1: {"range": +20},
                2: {"moab_damage": +1, "fortified_damage": +1},
                3: {"lead": True, "decamo": True},
                4: {"ability": "overclock"},
                5: {"ability": "ultraboost", "permanent_overclock": 0.10}
            },
            "bottom": {
                1: {"pierce": 8},
                2: {"pin": True},
                3: {"attack_speed": 0.5},
                4: {"bloon_trap": True, "trap_rbe": 500},
                5: {"bloon_trap": True, "trap_rbe": 10000, "traps_moab": True}
            }
        },
        "special_properties": {
            "lead_popping": "0-3-0",
            "camo_detection": None,
            "notes": "Overclock is one of the best support upgrades. Ultraboost permanently stacks. XXXL Trap can trap MOABs."
        }
    },

    "beast handler": {
        "name": "beast handler",
        "base_cost": 250,
        "category": "support",
        "base_stats": {
            "damage": 1,
            "attack_speed": 1.4,
            "pierce": 4,
            "range": 20,
            "beast_range": 50,
            "camo": False,
            "lead": False,
        },
        "upgrades": {
            "top":    [160, 875, 2950, 12500, 45000],
            "middle": [195, 945, 2600, 9500, 70000],
            "bottom": [180, 915, 3000, 8000, 30000]
        },
        "upgrade_stats": {
            "top": {
                1: {"beast": "piranha", "water_required": True},
                2: {"beast": "barracuda", "damage": 2, "pierce": 4},
                3: {"beast": "great_white", "lead": True, "moab_drag": True},
                4: {"beast": "orca", "instakill_bfb": True},
                5: {"beast": "megalodon", "instakill_bad": True, "requires_4x_orca_handlers": True}
            },
            "middle": {
                1: {"beast": "microraptor"},
                2: {"beast": "adasaurus", "lead": True},
                3: {"beast": "velociraptor", "stun_damage": True},
                4: {"beast": "t_rex", "ability": "stomp"},
                5: {"beast": "giganotosaurus", "global_stomp": True, "requires_4x_trex_handlers": True}
            },
            "bottom": {
                1: {"beast": "gyrfalcon", "track_required": True},
                2: {"beast": "horned_owl", "camo": True},
                3: {"beast": "golden_eagle", "moab_carry": True},
                4: {"beast": "giant_condor", "bfb_carry": True},
                5: {"beast": "pouakai", "zomg_carry": True, "requires_4x_condor_handlers": True}
            }
        },
        "special_properties": {
            "lead_popping": "0-2-0",
            "camo_detection": "0-0-2",
            "water_only_top": True,
            "track_required_bottom": True,
            "incomplete": True,
            "notes": "INCOMPLETE DATA - use rarely. Complex merging system. Tier 5 requires 4 merged Tier 4 handlers. Smallest base range (20). Cannot be moved by Support Chinook."
        }
    }
}

all_monkeys = {}
all_monkeys.update(primary_monkeys)
all_monkeys.update(military_monkeys)
all_monkeys.update(magic_monkeys)
all_monkeys.update(support_monkeys)

ranked_modes          = ["least cash", "least tiers", "timed"]
boss_difficulty_modes = ["normal", "elite"]
game_difficulty_modes = ["easy", "medium", "hard", "impoppable"]

def has_water(map_name): 
    map_data = maps.get(map_name.lower())
    if map_data:
        return map_data.get("water", False)
    return False

def can_use_water_strategy(map_name, strategy_type="basic"):
    """
    Check if map supports a water strategy.
    strategy_type options:
    - "basic": Just needs any water (Sub, Buccaneer)
    - "favored_trades": Needs mid/lots (5+ boats for Favored Trades buff)
    - "max_trades": Needs lots (10+ boats for max Favored Trades/Trade Empire)
    """
    water = has_water(map_name)
    
    if strategy_type == "basic":
        return water in ["small", "mid", "lots"]
    elif strategy_type == "favored_trades":
        return water in ["mid", "lots"]
    elif strategy_type == "max_trades":
        return water == "lots"
    
    return False

def get_upgrade_cost(monkey, path, tier, game_difficulty):
    """Get the cost of a specific upgrade adjusted for difficulty."""
    base_cost = monkey["upgrades"][path][tier - 1]
    return int(base_cost * difficulty_multipliers[game_difficulty])

def get_total_cost(monkey, top, middle, bottom, game_difficulty):
    """Get total cost of a monkey with a specific crosspath."""
    total = int(monkey["base_cost"] * difficulty_multipliers[game_difficulty])
    paths = {"top": top, "middle": middle, "bottom": bottom}
    for path, tiers in paths.items():
        for tier in range(1, tiers + 1):
            total += get_upgrade_cost(monkey, path, tier, game_difficulty)
    return total

def can_pop_lead(monkey_name):
    """Check if a monkey can pop lead at base or via upgrades."""
    m = all_monkeys.get(monkey_name)
    if not m:
        return False
    lead = m["special_properties"].get("lead_popping")
    if lead == "base":
        return True
    if lead and lead != None:
        return True
    return m["base_stats"].get("lead", False)

def can_detect_camo(monkey_name):
    """Check if a monkey can detect camo at base or via upgrades."""
    m = all_monkeys.get(monkey_name)
    if not m:
        return False
    camo = m["special_properties"].get("camo_detection")
    if camo == "base":
        return True
    if camo and camo != None:
        return True
    return m["base_stats"].get("camo", False)

def get_category(monkey_name):
    """Get the category of a monkey."""
    m = all_monkeys.get(monkey_name)
    if m:
        return m["category"]
    return None

def get_boss_hp(boss, boss_difficulty, stage, health_modifier):
    """Get the modified HP of a boss."""
    hp_tables = {
        "bloonarius":    bloonarius_hp,
        "lych":          lych_hp,
        "vortex":        vortex_hp,
        "phaze":         phaze_hp,
        "dreadbloon":    dreadbloon_hp,
        "blastapopoulos": blastapopoulos_hp
    }
    base_hp = hp_tables[boss][boss_difficulty][stage]
    if boss == "dreadbloon":
        return {
            "lead":    int(base_hp["lead"] * (health_modifier / 100)),
            "regular": int(base_hp["regular"] * (health_modifier / 100))
        }
    return int(base_hp * (health_modifier / 100))

def filter_banned(banned_list):
    """Return all monkeys minus banned ones."""
    return {name: data for name, data in all_monkeys.items()
            if name not in banned_list}

def get_boss_exit_time(map_name, boss_name, stage, boss_difficulty, speed_modifier=100):
    """
    Calculate how long it takes a boss to reach the exit.
    
    Args:
        map_name: Name of the map (e.g., "logs")
        boss_name: Name of the boss (e.g., "bloonarius")
        stage: Boss stage (1-5)
        boss_difficulty: "normal" or "elite"
        speed_modifier: Event speed modifier in % (default 100)
    
    Returns:
        Time in seconds for boss to exit, or None if data missing
    """
    # Get map data
    map_data = maps.get(map_name.lower())
    if not map_data:
        print(f"Warning: Map '{map_name}' not found in database")
        return None
    
    red_time = map_data.get("rbs")
    if not red_time:
        print(f"Warning: No red bloon time data for '{map_name}'")
        return None
    
    # Get boss speed multiplier for this stage
    boss_speeds = boss_speedmulti.get(boss_name.lower())
    if not boss_speeds:
        print(f"Warning: Boss '{boss_name}' not found in speed database")
        return None
    
    difficulty_speeds = boss_speeds.get(boss_difficulty.lower())
    if not difficulty_speeds:
        print(f"Warning: No speed data for {boss_difficulty} {boss_name}")
        return None
    
    # Stages are 1-indexed but list is 0-indexed
    if stage < 1 or stage > 5:
        print(f"Warning: Stage must be 1-5, got {stage}")
        return None
    
    boss_speed_percent = difficulty_speeds[stage - 1]
    
    # Calculate boss exit time
    # Boss time = red time / boss speed multiplier
    # Then apply event speed modifier
    base_boss_time = red_time / boss_speed_percent
    actual_time = base_boss_time / (speed_modifier / 100)
    
    return actual_time

def get_dreadbloon_requirements(available_monkeys):
    """
    Dreadbloon needs at least 2 different categories of monkeys
    and lead-popping ability for the lead phase.
    Immune phases: primary (100-75%), military (75-50%), magic (50-25%), support (25-0%).
    """
    categories_available = set()
    lead_options = []
    for name, data in available_monkeys.items():
        categories_available.add(data["category"])
        if can_pop_lead(name):
            lead_options.append(name)
    return {
        "categories_available": categories_available,
        "lead_options": lead_options,
        "meets_minimum": len(categories_available) >= 2 and len(lead_options) > 0
    }

def boss_calculation():
    """Main boss calculation - collects all inputs and displays HP."""

    # --- Boss selection ---
    while True:
        boss = input("Boss: ").lower().strip()
        if boss in Bosses:
            break
        print(f"Invalid boss. Choose from: {', '.join(Bosses)}")

    # --- Stage ---
    while True:
        stage = input("Stage (1-5): ").strip()
        if stage.isdigit() and 1 <= int(stage) <= 5:
            stage = int(stage)
            break
        print("Stage must be a number between 1 and 5.")

    # --- Boss difficulty ---
    while True:
        boss_difficulty = input("Boss difficulty (normal / elite): ").lower().strip()
        if boss_difficulty in boss_difficulty_modes:
            break
        print("Choose: normal or elite")

    # --- Game difficulty ---
    while True:
        game_difficulty = input("Game difficulty (easy / medium / hard / impoppable): ").lower().strip()
        if game_difficulty in game_difficulty_modes:
            break
        print("Choose: easy, medium, hard, or impoppable")

    # --- Ranked mode ---
    while True:
        ranked_mode = input("Ranked mode (least cash / least tiers / timed): ").lower().strip()
        if ranked_mode in ranked_modes:
            break
        print("Choose: least cash, least tiers, or timed")

    # --- Modifiers ---
    print("\nIf no modifier is mentioned, enter 100")

    while True:
        speed_raw = input("Speed modifier in %: ").replace('%', '').strip()
        if speed_raw.isdigit():
            speed_modifier = int(speed_raw)
            break
        print("Please enter a valid number.")

    while True:
        health_raw = input("Health modifier in %: ").replace('%', '').strip()
        if health_raw.isdigit():
            health_modifier = int(health_raw)
            break
        print("Please enter a valid number.")

    # --- Banned monkeys ---
    print("\nEnter banned monkeys separated by spaces (or press Enter for none):")
    banned_input = input("Banned monkeys: ").lower().strip()
    banned_monkeys = banned_input.split() if banned_input else []

    # Validate banned monkeys
    valid_banned = []
    for name in banned_monkeys:
        if name in all_monkeys:
            valid_banned.append(name)
        else:
            print(f"  Warning: '{name}' not recognised, skipping.")
    banned_monkeys = valid_banned

    # map selection
    while True:
        map_name = input("\nMap name: ").lower().strip()
        if map_name in maps:
            break
        else:
            print(f"map not in list")

    # ---- Compute HP ----
    hp_data = get_boss_hp(boss, boss_difficulty, stage, health_modifier)

    print("\n" + "=" * 50)
    print(f"  {boss.upper()} | {boss_difficulty.upper()} | Stage {stage}")
    print("=" * 50)

    if boss == "dreadbloon":
        total_hp = hp_data["lead"] + hp_data["regular"]
        print(f"  Lead HP:    {hp_data['lead']:>15,}  (needs lead popping)")
        print(f"  Regular HP: {hp_data['regular']:>15,}")
        print(f"  Total HP:   {total_hp:>15,}")
        print(f"\n  Immunity rotation (every 25% HP):")
        print(f"    100-75%: Primary immune")
        print(f"     75-50%: Military immune")
        print(f"     50-25%: Magic immune")
        print(f"     25-0%:  Support immune")
        dread_req = get_dreadbloon_requirements(filter_banned(banned_monkeys))
        print(f"\n  Categories available: {', '.join(sorted(dread_req['categories_available']))}")
        if not dread_req["meets_minimum"]:
            print("  WARNING: Not enough categories or no lead popping available!")
    else:
        print(f"  HP: {hp_data:,}")

    if boss == "phaze":
        print(f"\n  Note: Phaze requires camo detection!")

    print(f"\n  Speed modifier:  {speed_modifier}%")
    print(f"  Health modifier: {health_modifier}%")
    print(f"  Game difficulty: {game_difficulty}")
    print(f"  Ranked mode:     {ranked_mode}")
    if banned_monkeys:
        print(f"  Banned:          {', '.join(banned_monkeys)}")
    print("=" * 50)

    print("\n[Strategy recommendation engine coming soon!]")

# ============================================================
# MAIN MENU
# ============================================================

def main_menu():
    """Main menu."""
    while True:
        print("\n" + "=" * 40)
        print("    BTD6 BOSS EVENT CALCULATOR")
        print("=" * 40)
        print("1. Start new boss calculation")
        print("2. Continue from saved data")
        print("3. Quit")
        print("=" * 40)

        choice = input("\nChoose an option (1-3): ").strip()

        if choice == "1":
            print()
            boss_calculation()
        elif choice == "2":
            print("\n[Save/load coming soon! Starting new calculation...]\n")
            boss_calculation()
        elif choice == "3":
            print("\nGoodbye!")
            break
        else:
            print("Invalid choice. Enter 1, 2, or 3.")

# ============================================================
# ENTRY POINT
# ============================================================

if __name__ == "__main__":
    main_menu()
