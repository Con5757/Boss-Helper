# Notes: this isnt a readme file btw, this is just what needs to be worked on

UPDATED TO-DO LIST
✅ COMPLETED

All 25 monkey data structures (primary, military, magic, support)
Boss HP database (all 6 bosses, normal/elite, stages 1-5)
Difficulty multipliers (Easy/Medium/Hard/Impoppable)
Input validation system
Helper functions: can_pop_lead(), can_detect_camo(), get_total_cost(), filter_banned()
Dreadbloon category checker
Main menu structure
Basic HP calculation and display

🔄 IN PROGRESS (YOU'RE WORKING ON)

Map data collection:

Organizing maps by difficulty (beginner/intermediate/advanced/expert)
Red bloon time per map
Water classification (False/"small"/"mid"/"lots")


Boss speed multipliers:

Speed per boss per stage per difficulty (normal/elite)
Format: boss_speed_multipliers[boss][difficulty][stage]



📋 NEXT UP (AFTER MAPS ARE DONE)
1. IMPLEMENT BLOON SPEED SCALING

Add freeplay speed mechanics (rounds 81+)
get_bloon_speed_multiplier(round_number) function
Super Ceramic detection (round 81+)

2. FINISH MAP INFRASTRUCTURE

Combine all map dictionaries into all_maps
Create has_water(map_name) function
Create can_use_water_strategy(map_name, strategy_type) function
Create get_boss_exit_time(map_name, boss_name, stage, speed_modifier) function
Add map selection to boss_calculation() input flow

3. BUILD FILTERING SYSTEM

Filter water-only towers based on map
Filter by Phaze camo requirement
Filter by Dreadbloon 2-category + lead requirement
Filter by banned monkeys
Create get_available_monkeys() master filter function

4. BUILD RECOMMENDATION ENGINE (CORE LOGIC)
Least Cash Mode:

Calculate cheapest single-tower strategy
Calculate cheapest multi-tower combos (2-3 towers)
Include buff towers (Alchemist, Village) when cost-effective
Output total cost breakdown

Least Tiers Mode:

Count total upgrade tiers (5-0-0 = 5 tiers, 2-3-1 = 6 tiers)
Find strategy with minimum tier count
Tiebreaker: prefer cheaper if tier counts equal

Timed Mode:

Calculate DPS for each monkey crosspath
Factor in attack speed, damage, pierce, range
Include MOAB bonus damage
Find highest DPS strategy that fits budget
Check if boss can be killed before exit (use get_boss_exit_time())
Warn if insufficient DPS

Multi-Tower Strategies:

Recommend 2-3 tower combos (main DPS + support)
Include Alchemist buff calculations (+1 damage, lead popping)
Include Village MIB for Dreadbloon
Include Homeland Defense for timed strategies

5. DAMAGE CALCULATION SYSTEM

calculate_dps(monkey_name, top, middle, bottom) function
Factor in: damage × pierce / attack_speed
Add ceramic bonus damage
Add MOAB bonus damage
Add special damage types (fire DoT, explosions, etc.)
can_kill_boss(dps, boss_hp, exit_time) feasibility check

6. ECONOMY/FARMING STRATEGY (ROUNDS 1-40)

Calculate money needed by round 40 for strategy
Recommend Banana Farm placements if money short
Generate round-by-round guide:

Rounds 1-10: Start with X
Rounds 11-20: Add Y
Rounds 21-30: Upgrade to Z
Rounds 31-40: Final setup


Factor in natural income per round

7. OUTPUT IMPROVEMENTS

Display recommended strategy with costs
Show step-by-step build order
Show DPS vs boss HP comparison
Show time margin (will boss escape?)
Show total cost breakdown
Color-coded warnings (if terminal supports it)

8. QUALITY OF LIFE

Save/load functionality (pickle or JSON)
Export results to text file
Better error messages
Summary screen with all inputs + recommendations
"Try again with different settings?" loop

9. TESTING & POLISH

Test all 6 bosses × 2 difficulties × 5 stages
Test all 3 ranked modes
Test edge cases (impossible scenarios, no water, etc.)
Verify HP calculations
Verify cost calculations
Optimize performance if needed
Add code comments and documentation
