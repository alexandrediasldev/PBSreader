## 🟡 pokemon.txt

Information pulled from the new wiki:  
29 September 2020 - https://essentialsdocs.fandom.com/wiki/Defining_a_species 
https://essentialsdocs.fandom.com/wiki/Defining_a_species?oldid=937

### Mandatory

**[ID]**:  
This line must come first in a section, because, as mentioned above, this line defines when a new section begins. This line contains a number inside square brackets, e.g. [42].
This number must be different for each species. It must be a whole number that is 1 or higher. While you can skip numbers, minor bugs can occur if you do so, so it is recommended that you don't. The order in which species are numbered is not important; however, keeping them in order will make it easier to spot gaps or mistakes.

This ID number is the default National Pokédex number of the species. If there are no Regional Pokédex lists defined, or if viewing the default Pokédex list in the Pokédex, that list will contain all the defined Pokémon species sorted by this number.

**Name**:  
The name of the species, as seen by the player.

**InternalName**:  
This is how the scripts refer to the species. Typically this is the species name, but written in all capital letters and with no spaces or symbols. The internal name is never seen by the player.

**Type1, Type2**:  
The internal name(s) of the species' primary and secondary elemental types.
Type2 is optional, and can be omitted if it does not apply to the species.

**BaseStats:**   
Six comma-separated values, corresponding to (in order):
1. HP
2. Attack
3. Defense
4. Speed
5. Special Attack
6. Special Defense  

Each value can be 1 or higher.

**GenderRate:**  
The likelihood of a Pokémon of the species being a certain gender. Must be one of the following:
- AlwaysMale
- FemaleOneEighth
- Female25Percent
- Female50Percent
- Female75Percent
- FemaleSevenEighths
- AlwaysFemale
- Genderless

**GrowthRate:**  
The rate at which a Pokémon of the species gains levels (i.e. how much Experience is needed to level up). Must be one of the following:
- Fast
- Medium (also known as MediumFast)
- Slow
- Parabolic (also known as MediumSlow)
- Erratic
- Fluctuating

**BaseEXP:**  
The base amount of Experience gained from defeating a Pokémon of the species. It must be a whole number that is 1 or higher.
This base amount is used in a calculation to determine the actual number of Exp. points awarded for defeating a Pokémon of the species.

**EffortPoints:**   
The number of EVs gained by defeating a Pokémon of the species. Is six comma-separated numbers, corresponding to (in order):
1. HP
2. Attack
3. Defense
4. Speed
5. Special Attack
6. Special Defense
Each value can be 0 or higher. As a rule, the total of these numbers should be between 1 and 3, and higher evolutions tend to give more EVs.
   

**Rareness:**  
The catch rate of the species. It can be 0 or higher (typically the highest is 255). The higher the number, the more likely a capture (0 means it cannot be caught by anything except a Master Ball).

**Happiness:**  
The amount of happiness a newly caught Pokémon of the species will have. It can be 0 or higher, although it is typically 70. The game treats 255 as the highest attainable happiness.

**Moves:**  
The moves that all Pokémon of the species learn as they level up. There are two (comma-separated) parts to each move:
1. Level at which the move is learned (0 means the move can only be learned when a Pokémon evolves into the species).
2. The internal name of the move.

These couplets are also comma-separated in this line.

**Compatibility:**  
The egg groups that the species belongs to. Is either one or two (comma-separated) of the following words:
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

"Water1" is for sea creatures, "Water2" is for fish, and "Water3" is for shellfish. "Ditto" should contain only Ditto, as a species in that group can breed with any other breedable Pokémon. If either egg group is "Undiscovered", the species cannot breed.

**StepsToHatch:**  
The number of steps it takes to hatch an egg of the species. It can be 1 or higher. Note that this is not the number of egg cycles for the species, but the actual number of steps.

**Height:**  
The height of the species in meters, to one decimal place. Use a period for the decimal point, and do not use commas for thousands.
The Pokédex will automatically show this height in feet/inches if the game recognises that the player is in the USA. This is only cosmetic; the rest of the scripts still perform calculations using the meters value defined.

**Weight:**  
The weight of the species in kilograms, to one decimal place. Use a period for the decimal point, and do not use commas for thousands.
The Pokédex will automatically show this weight in pounds if the game recognises that the player is in the USA. This is only cosmetic; the rest of the scripts still perform calculations using the kilograms value defined.

**Color:**  
The main colour of the species. Must be one of the colours defined in the script section PBColors, which by default are:
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


**Shape:**  
The body shape of the species. The Pokédex can search for Pokémon of particular shapes. This is a number from 1 to 14 inclusive, as follows:
- 1 = Only a head
- 2 = Serpent-like
- 3 = Fish
- 4 = Head and arms
- 5 = Head and base
- 6 = Bipedal with tail
- 7 = Head and legs
- 8 = Quadruped
- 9 = Has two wings
- 10 = Tentacles/multiple legs
- 11 = Multiple fused bodies
- 12 = Humanoid
- 13 = Winged insectoid
- 14 = Insectoid

**Kind:**  
The species' kind, which is displayed in the Pokédex. For example, Bulbasaur is the Seed Pokémon. The word "Pokémon" is automatically added to the end, so only "Seed" needs to be here.

**Pokedex:**  
The Pokédex entry.

### Optional
**Abilities:**  
The internal name(s) of one or two abilities that the species can have. If there are two abilities, separate them with a comma.

**HiddenAbility:**    
The internal names of up to four additional abilities that the species can have. If there are multiple abilities here, they are separated by commas.
Pokémon cannot have any hidden ability naturally, and must be specially given one.

**EggMoves:**  
A comma-separated list of the internal names of moves that a Pokémon of the species can only learn as an egg (obtained through breeding). Only species that can be in eggs should have this line (typically only unevolved species).

**Habitat:**  
The kind of location that the species can typically be found in. Must be one of the habitats defined in the script section PBHabitats, which by default are:
- None
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

This information is unused in Pokémon Essentials.

**RegionalNumbers:**  
One or more comma-separated numbers. Each number is the Pokédex number of the species in the corresponding Regional Pokédex. A number of 0 means that the species does not appear in that Regional Pokédex.

**WildItemCommon
WildItemUncommon
WildItemRare:**  
The internal names of items that a wild Pokémon of the species may be found holding. Each line can only list one item.
The chances of holding the item are 50%, 5% and 1% respectively. If all three are the same item, then the chance of holding it is 100% instead.

**🟢 BattlerPlayerX
BattlerPlayerY:**  
Affects the positioning of the back sprite of the species in battle. A higher number means the back sprite is placed further right/lower down the screen. Can be positive or negative, and is 0 by default.

**🟢 BattlerEnemyX
BattlerEnemyY:**  
Affects the positioning of the front sprite of the species in battle. A higher number means the front sprite is placed further right/lower down the screen. Can be positive or negative, and is 0 by default.

**BattlerAltitude:**  
Affects the positioning of the front sprite of the species in battle relative to its base. A higher number means the front sprite is placed further up the screen. Can only be positive or 0, and is 0 by default.
This properly is typically unused as BattlerEnemyY can do the same thing.

**🟢 BattlerShadowX:**  
Affects the horizontal positioning of the shadow beneath the front sprite of the species in battle. A higher number means the shadow is placed further right on the screen. Can be positive or negative, and is 0 by default.

**🟢 BattlerShadowSize:**  
A number that determines which shadow graphic to place underneath the front sprite of the species in battle. It can be 0 or higher. By default, there are three possible shadow graphics, ranging from 1 (smallest) to 3 (largest).

**Evolutions:**  
The evolution paths the species can take. For each possible evolution of the species, there are three parts:
1. The internal name of the evolved species.
2. The evolution method. Must be one of the methods defined in the script section Pokemon_Evolution. A full list is on the page Evolution, but examples are:
- Happiness
- Level
- Trade
- Item
- Beauty
- HasMove
- LevelFemale
- Location

3. A parameter used by the evolution method. Depending on the method, this could be blank or a number or the internal name of a move/item/ability/species/type/etc.


**FormNames:**  
The name of this form of the species (form 0), if it has one.
If this is blank, then its form name as shown in the Pokédex's Forms page will be "Male"/"Female" if the species is gendered. If the species is genderless, its form name will be "Genderless" (if this is the only form for the species) or "One Form" (if the species also has other forms).

**Incense:**  
The internal name of an item that needs to be held by a parent when breeding in order for the egg to be this species. If neither parent is holding the required item, the egg will be the next evolved species instead.
The only species that should have this line are ones which cannot breed, but evolve into a species which can. That is, the species should be a "baby" species. Not all baby species need this line. Note that Essentials does not have any formal definition of what a "baby" species is.

### Example:
```
[1]
Name = Bulbasaur
Type1 = GRASS
Type2 = POISON
BaseStats = 45,49,49,45,65,65
GenderRate = FemaleOneEighth
BaseEXP = 64
Moves = 1,TACKLE,3,GROWL,7,LEECHSEED,9,VINEWHIP,13,POISONPOWDER,13,SLEEPPOWDER,15,TAKEDOWN,19,RAZORLEAF,21,SWEETSCENT,25,GROWTH,27,DOUBLEEDGE,31,WORRYSEED,33,SYNTHESIS,37,SEEDBOMB
Height = 0.7
Pokedex = Bulbasaur can be seen napping in bright sunlight. There is a seed on its back. By soaking up the sun's rays, the seed grows progressively larger.
Evolutions = IVYSAUR,Level,16
```


