## pokemon.txt

Information pulled from the old wiki on the way back machine:  
September 28th 2015 - http://pokemonessentials.wikia.com/wiki/Defining_a_species  
https://web.archive.org/web/20150928234522/http://pokemonessentials.wikia.com/wiki/Defining_a_species


### Mandatory

**[IDnumber]**:  
National Dex number of the species, comes first in a section

**Name**:  
The actual name of this species. This is only used when displaying the species' name on the screen.

**InternalName**:  
This is the name the scripts refer to and use. Typically written only in capital letters with no spaces or symbols. It is never shown to the player.

**Type1, Type2**:  
The primary and secondary elemental types of this species.
Type2 is optional.

**BaseStats:**   
Six comma-separated values, corresponding to:
1. HP
2. Attack
3. Defense
4. Speed
5. Special Attack
6. Special Defense  

Each value can be between 0 and 255.

**GenderRate:**  
The likelihood of a Pokémon of this species being a certain gender. Must be one of:
- AlwaysMale
- FemaleOneEighth
- Female25Percent
- Female50Percent
- Female75Percent
- FemaleSevenEighths
- AlwaysFemale
- Genderless

**GrowthRate:**  
The rate at which a Pokémon of this species gains levels (i.e. how much Experience is needed to level up). One of:
- Fast
- Medium or MediumFast
- Slow
- Parabolic or MediumSlow
- Erratic
- Fluctuating

**BaseEXP:**  
The base amount of Experience gained from defeating a Pokémon of this species. Is a number between 0 and 65535.
This base amount is then modified depending on the level and ownership of the defeated Pokémon, along with several other factors. See the article Ending a battle for more information.

**EffortPoints:**   
The number of EVs gained by defeating a Pokémon of this species. Is six comma-separated numbers, corresponding to:
1. HP
2. Attack
3. Defense
4. Speed
5. Special Attack
6. Special Defense
As a rule, the total of these numbers should be between 1 and 3, and higher evolutions tend to give more EVs.

**Rareness:**  
The catch rate of this species. Is a number between 0 and 255. The higher the number, the more likely a capture (0 means it cannot be caught by anything except a Master Ball).

**Happiness:**  
The amount of happiness a newly caught Pokémon of this species will have. Is a number between 0 and 255, although is typically 70.

**Moves:**  
The moves this species learns as it levels up. There are two (comma-separated) parts to each move:
1. Level at which the move is learned.
2. The move's internal name.
These couplets are also comma-separated in this line.

**Compatibility:**  
The egg groups this species belongs to. Is either one word or two comma-separated words, depending on how many egg groups this species belongs to. If either egg group is "Undiscovered", this species cannot breed.
- Monster
- Water1
- Bug
- Flying
- Field
- Fairy
- Grass
- Humanlike
- Water3
- Mineral
- Amorphous
- Water2
- Ditto
- Dragon
- Undiscovered  

"Water1" is for sea creatures, "Water2" is for fish, and "Water3" is for shellfish. "Ditto" should contain only Ditto, as a species in this group can breed with any other breedable Pokémon.

**StepsToHatch:**  
The number of steps it takes to hatch an egg of this species. Is typically a multiple of 255, and is typically 5355.

**Height:**  
The height of the species in meters, to one decimal place. Use a period for the decimal point, and do not use commas for thousands.
The Pokédex will automatically show this height in feet/inches, if the game recognises that the player is in the USA. This is only cosmetic; the rest of the scripts still calculate using the metres value defined.

**Weight:**  
The weight of the species in kilograms, to one decimal place. Use a period for the decimal point, and do not use commas for thousands.
The Pokédex will automatically show this weight in pounds, if the game recognises that the player is in the USA. This is only cosmetic; the rest of the scripts still calculate using the kilograms value defined.

**Color:**  
The main colour of this species. Must be one of:
- Black
- Blue
- Brown
- Gray
- Green
- Pink
- Purple
- Red
- White
- Yellow

**Kind:**  
The species' kind (e.g. Bulbasaur is the Seed Pokémon). The word "Pokémon" is automatically added to the end, so only "Seed" needs to be here.

**Pokedex:**  
The Pokédex entry.

### Optional
**Abilities:**  
The abilities this species can have (either 1 or 2 of them). Is the internal names of those abilities. If there are two abilities, separate them with a comma.

**HiddenAbility:**    
Up to 4 additional abilities this species can have. Is the internal names of those abilities, separated by commas. Pokémon cannot have any hidden ability naturally, and must be specially given one.

**EggMoves:**  
Moves that a Pokémon of this species can only learn as an egg (obtained through breeding). Only species that can be in eggs should have this line (typically only unevolved species). Is a comma-separated list of the internal names of all egg moves. See the article Breeding for more information on how a Pokémon can learn egg moves.

**Habitat:**  
The location this species can typically be found in. Is one of:
- Cave
- Forest
- Grassland
- Mountain
- Rare
- RoughTerrain
- Sea
- Urban
- WatersEdge

"Rare" can be taken to mean "unknown" here.

**RegionalNumbers:**  
Used to define Regional Pokédexes. This is the Regional Dex number of this species in each region (0 if this species is not in that Regional Dex). For multiple Regional Dexes, separate each number with a comma (e.g. 25,22,156,104 for four Regional Dexes).

**WildItemCommon,WildItemUncommon,WildItemRare:**  
The item that a wild Pokémon of this species may be holding. Is the internal name of that item.
The chances of holding the item are 50%, 5% and 1% respectively. If all three are the same item, then the chance of holding it is 100% instead.

**BattlerPlayerY:**  
How far down the screen the back sprite is in battle. A higher number means the back sprite is placed lower down the screen. Can be positive or negative, and is 0 by default.

**BattlerEnemyY:**  
How far down the screen the enemy (front) sprite is in battle. A higher number means the front sprite is placed lower down the screen. Can be positive or negative, and is 0 by default.

**BattlerAltitude:**  
How far up the screen the enemy (front) sprite is in battle. A higher number means the front sprite is placed lower down the screen. Can only be positive or 0, and is 0 by default.
This is the exact opposite of BattlerEnemyY. If this value is greater than 0, the Pokémon's shadow is shown in battle.

**Evolutions:**  
The evolution paths this species can take. For each possible evolution of this species, there are three parts:
1. The evolved species.
2. The evolution method. One of:
- Level - (level)
- LevelMale - (level)
- LevelFemale - (level)
- AttackGreater - (level)
- AtkDefEqual - (level)
- DefenseGreater - (level)
- Silcoon - (level)
- Cascoon - (level)
- Ninjask - (level)
- Shedinja - (level)
- ItemMale - (item's internal name)
- ItemFemale - (item's internal name)
- DayHoldItem - (item's internal name)
- NightHoldItem - (item's internal name)
- Happiness - (-)
- HappinessDay - (-)
- HappinessNight - (-)
- HasMove - (move's internal name)
- HasInParty - (species' internal name)
- Beauty - (minimum beauty)
- Location - (map ID)
- Trade - (-)
- TradeItem - (item's internal name)
- TradeSpecies - (species' internal name)
- Custom 1-7 - (number between 0-65535)

3. The value/name as mentioned above.

**FormNames:**  
The names of each form of this species, separated by commas. These names also determine how many forms this species has. Currently used only in the Pokédex's Forms page.
If the first name is blank, then its form name as shown in the Pokédex will be "Male"/"Female" if the species is gendered, or "One form" if genderless.

### Example:
```
[1]
Name=Bulbasaur
InternalName=BULBASAUR
Type2=POISON
BaseStats=45,49,49,45,65,65
GenderRate=FemaleOneEighth
GrowthRate=Parabolic
BaseEXP=64
EffortPoints=0,0,0,0,1,0
Rareness=45
Happiness=70
Abilities=OVERGROW
HiddenAbility=CHLOROPHYLL
Moves=1,TACKLE,3,GROWL,7,LEECHSEED,9,VINEWHIP,13,POISONPOWDER,13,SLEEPPOWDER,15,TAKEDOWN,19,RAZORLEAF,21,SWEETSCENT,25,GROWTH,27,DOUBLEEDGE,31,WORRYSEED,33,SYNTHESIS,37,SEEDBOMB
EggMoves=AMNESIA,CHARM,CURSE,ENDURE,GIGADRAIN,GRASSWHISTLE,INGRAIN,LEAFSTORM,MAGICALLEAF,NATUREPOWER,PETALDANCE,POWERWHIP,SKULLBASH,SLUDGE
Compatibility=1,7
StepsToHatch=5355
Height=0.7
Weight=6.9
Color=Green
Habitat=Grassland
RegionalNumbers=1,231
Kind=Seed
Pokedex=Bulbasaur can be seen napping in bright sunlight. There is a seed on its back. By soaking up the sun's rays, the seed grows progressively larger.
BattlerPlayerY=0
BattlerEnemyY=25
BattlerAltitude=0
Evolutions=IVYSAUR,Level,16
```


