# Notes: this isnt a readme file btw, this is just what needs to be worked on

Monkey Data (Costs + Stats)

 Ice Monkey
 Glue Gunner
 Sniper Monkey
 Monkey Sub
 Monkey Buccaneer
 Monkey Ace
 Heli Pilot
 Mortar Monkey
 Dartling Gunner
 Wizard Monkey
 Super Monkey
 Ninja Monkey
 Alchemist
 Druid
 Mermonkey
 Banana Farm
 Spike Factory
 Monkey Village
 Engineer Monkey
 Beast Handler

Monkey Stats Needed (for each monkey)

 Base damage
 Base attack speed
 Base pierce
 Base range
 How each upgrade modifies these stats
 Special abilities (buffs, debuffs, etc.)

Map Data

 List all available maps
 Time for each boss to reach end on each map (by boss + map combination)
 Water availability per map

2. CALCULATION LOGIC
Filtering System

 Filter monkeys by boss requirements (Phaze = camo, Dreadbloon = 2 categories + lead)
 Filter out banned monkeys
 Filter by map (water monkeys only on water maps)

Recommendation Engine

 Least Cash Mode: Calculate cheapest effective strategy
 Least Tiers Mode: Calculate strategy with fewest total upgrade tiers
 Timed Mode: Calculate highest DPS strategy
 Support multiple towers in recommendation (not just one)
 Include buff towers (Alchemist, Village) in calculations

Damage Calculations

 Create function to calculate DPS for any monkey crosspath
 Factor in pierce (how many bloons hit per shot)
 Factor in special damage bonuses (vs Ceramics, MOABs, etc.)
 Calculate if strategy can deal enough damage in time
 Warn if boss will escape before being killed

Economy/Farming Strategy

 Generate farming instructions for rounds 1-40
 Calculate money needed by round 40
 Recommend farming towers (Banana Farm, etc.)

3. FEATURES TO ADD
Menu System

 Main menu with options
 "Continue from saved data" - save/load previous inputs
 Better error handling and input validation

Boss Mechanics

 Display Dreadbloon immunity rotation info
 Display Phaze camo requirement
 Display any other special boss mechanics
 Factor in speed modifier (affects time boss takes to exit)

Output Improvements

 Show recommended tower placements/strategy
 Show step-by-step guide (rounds 1-10, 11-20, etc.)
 Show total cost breakdown
 Show if strategy is possible or not
 Show margin of error (overkill vs underkill)

Quality of Life

 Ask if there's water on the map
 Color-coded terminal output (if possible)
 Summary screen at end with all inputs + recommendations
 Option to export/save results to file

4. CODE ORGANIZATION

 Organize all monkey data into clean dictionary structure
 Create helper functions for common calculations
 Add comments and documentation
 Test all edge cases
 Optimize performance (if needed for large calculations)

5. TESTING & DEBUGGING

 Test each boss with different configurations
 Test all ranked modes
 Test with various banned monkey combinations
 Verify all HP calculations are correct
 Verify all cost calculations are correct
 Test impossible scenarios (not enough DPS, etc.)
