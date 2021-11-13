## 🟡 pokemon.txt

Information pulled from the new wiki:  
8 May 2021 - https://essentialsdocs.fandom.com/wiki/Defining_a_species 
https://essentialsdocs.fandom.com/wiki/Defining_a_species?oldid=1027

### Mandatory

**[ID number]**:  
This line must come first in a section, because, as mentioned above, this line defines when a new section begins. This line contains a number inside square brackets, e.g. [42].
This number must be different for each species. It must be a whole number greater than 0. You cannot skip numbers. The ID number is used as the National Pokédex number, and also affects the order in which species are listed in some Debug mode features.

**Name**:  
The name of the species, as seen by the player.

**InternalName**:  
This must be different for each species. Also known as the ID, this is how the scripts refer to the species. Typically this is the same as the species name, but written in all capital letters and with no spaces or symbols. In the scripts, the ID is used as a symbol (i.e. with a colon in front of it, e.g. :BULBASAUR). The ID is never seen by the player.

### Optional

**Type1, Type2**:  
The ID of the primary and secondary elemental types of the species.
Default value: Normal(type1)

**BaseStats:**   
Six comma-separated values, corresponding to the order that main stats are defined. By default, the order is:
1. HP
2. Attack
3. Defense
4. Speed
5. Special Attack
6. Special Defense  

Each value can be 1 or higher.
Default value: 1,1,1,1,1,1

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

Default value: Female50Percent

**GrowthRate:**  
The rate at which a Pokémon of the species gains levels (i.e. how much Experience is needed to level up). Must be one of the following:
- Fast
- Medium (known elsewhere as Medium Fast))
- Slow
- Parabolic (known elsewhere as Medium Slow)
- Erratic
- Fluctuating

Default value: Medium

**BaseEXP:**  
The base amount of Experience gained from defeating a Pokémon of the species. It must be a whole number that is 1 or higher.
This base amount is used in a calculation to determine the actual number of Exp. points awarded for defeating a Pokémon of the species.
Default value: 100

**EffortPoints:**   
The number of EVs gained by defeating a Pokémon of the species. Is six comma-separated values, corresponding to the order that main stats are defined. By default, the order is:
1. HP
2. Attack
3. Defense
4. Speed
5. Special Attack
6. Special Defense
Each value can be 0 or higher. As a rule, the total of these numbers should be between 1 and 3, and higher evolutions tend to give more EVs. 
   
Default value: 0,0,0,0,0,0

**Rareness:**  
The catch rate of the species. It can be 0 or higher (typically the highest is 255). The higher the number, the more likely a capture (0 means it cannot be caught by anything except a Master Ball).

Default value: 255

**Happiness:**  
The amount of happiness a newly caught Pokémon of the species will have. It can be 0 or higher, although it is typically 70. The game treats 255 as the highest attainable happiness.

Default value: 70

**Abilities:**  
The IDs of one or two abilities that the species can have. If there are two abilities, separate them with a comma.
Default value: none

**HiddenAbility:**    
The IDs of any number of additional abilities that the species can have. If there are multiple abilities here, they are separated by commas.
Pokémon cannot have any Hidden Ability naturally, and must be specially given one.
Default value: none

**Moves:**  
The moves that all Pokémon of the species learn as they level up. This line consists of comma-separated level/move pairs which are themselves comma-separated, i.e. level,move,level,move,level,move.... Each pair contains the level at which the Pokémon will learn the move, followed by the ID of the move it will learn.
A level of 0 means the move will be learned when a Pokémon evolves into the species, and not at any other point (except via the Move Relearner).
Default value: none

**🟢 TutorMoves:**  
A comma-separated list of the IDs of moves that a Pokémon of the species can be taught by a HM, TM, TR or Move Tutor. If a move is not listed here, it cannot be taught by those methods, even if the move appears in its Moves or EggMoves properties.
Default value: none

**EggMoves:**  
A comma-separated list of the IDs of moves that a Pokémon of the species can only learn as an egg (obtained through breeding). Only species that can be in eggs should have this line (typically only unevolved species).
Default value: none


**Compatibility:**  
The egg group(s) that the species belongs to. If there are multiple egg groups here, they are separated by commas. The default available egg group are:
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
Default value: Undiscovered

**StepsToHatch:**  
The number of steps it takes to hatch an egg of the species. It can be 1 or higher. Note that this is not the number of egg cycles for the species, but the actual number of steps. Only species that can be in eggs should have this line (typically only unevolved species).
Default value: 1

**Height:**  
The height of the species in meters, to one decimal place. Use a period for the decimal point, and do not use commas for thousands.
The Pokédex will automatically show this height in feet/inches if the game recognises that the player is in the USA. This is only cosmetic; the rest of the scripts still perform calculations using the meters value defined.
Default value: 0.1

**Weight:**  
The weight of the species in kilograms, to one decimal place. Use a period for the decimal point, and do not use commas for thousands.
The Pokédex will automatically show this weight in pounds if the game recognises that the player is in the USA. This is only cosmetic; the rest of the scripts still perform calculations using the kilograms value defined.
Default value: 0.1

**Color:**  
The main body color of the species. The default available body colors are:
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
Default value: Red


**Shape:**  
The body shape of the species. The Pokédex can search for Pokémon of particular shapes. The default available body shapes are:
- Head
- Serpentine
- Finned
- HeadArms
- HeadBase
- BipedalTail
- HeadLegs
- Quadruped
- Winged
- Multiped
- MultiBody
- Bipedal
- MultiWinged
- Insectoid
Default value: Head


**Habitat:**  
The kind of location that the species can typically be found in. The default available habitats are:
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
Default value: none

**Kind:**  
The species' category, which is displayed in the Pokédex. For example, Bulbasaur is the Seed Pokémon. The word "Pokémon" is automatically added to the end, so only "Seed" needs to be here.
Default value: "???"

**Pokedex:**  
The Pokédex entry.
Default value: "???"

**FormNames:**  
The name of this form of the species (form 0), if it has one.
If this is blank, then its form name as shown in the Pokédex's Forms page will be "Male"/"Female" if the species is gendered. If the species is genderless, its form name will instead be "Genderless" (if this is the only form for the species) or "One Form" (if the species also has other forms).
Default value: none

**🟢 Generation:**  
A number representing the generation of Pokémon games in which this species first appeared. This information is unused in Essentials.
Default value: 0

**🔴 RegionalNumbers:**  
REMOVED 

**WildItemCommon
WildItemUncommon
WildItemRare:**  
The IDs of items that a wild Pokémon of the species may be found holding. Each line can only have one item.
The chances of holding the item are 50%, 5% and 1% respectively. If all three are the same item, then the chance of holding it is 100% instead.
Default value: none

**BattlerPlayerX
BattlerPlayerY:**  
Affects the positioning of the back sprite of the species in battle. A higher number means the back sprite is placed further right/lower down in the screen. Can be positive or negative.
Default value: 0

**BattlerEnemyX
BattlerEnemyY:**  
Affects the positioning of the front sprite of the species in battle. A higher number means the front sprite is placed further right/lower down in the screen. Can be positive or negative.
Default value: 0

**BattlerAltitude:**  
Affects the positioning of the front sprite of the species in battle relative to its base. A higher number means the front sprite is placed further up the screen. Can only be positive or 0.
This property is typically unused because BattlerEnemyY can do the same thing.
Default value: 0

**BattlerShadowX:**  
Affects the horizontal positioning of the shadow beneath the front sprite of the species in battle. A higher number means the shadow is placed further right on the screen. Can be positive or negative.
Default value: 0

**BattlerShadowSize:**  
A number that determines which shadow graphic to place underneath the front sprite of the species in battle. It can be 0 or higher. By default, there are three possible shadow graphics (in the folder "Graphics/Pokemon/Shadow"), ranging from 1 (smallest) to 3 (largest).
Default value: 2

**Evolutions:**  
The evolution paths the species can take. For each possible evolution of the species, there are three parts:
1. The ID of the species it evolves into.

2. The evolution method. Must be one of the methods registered in GameData::Evolution. A full list is on the page Evolution, but examples are:
- Level
- LevelFemale
- Happiness
- Beauty
- HasMove
- Location
- Item
- Trade

3. A parameter used by the evolution method. Depending on the method, this could be blank or a number or the ID of a move/item/ability/species/type/etc.
Default value: none



**Incense:**  
The ID of an item that needs to be held by a parent when breeding in order for the egg to be this species. If neither parent is holding the required item, the egg will be the next evolved species instead.
The only species that should have this line are ones which cannot breed, but which evolve into a species that can. That is, the species should be a "baby" species. Not all baby species need this line. Note that Essentials does not have any formal definition of what a "baby" species is.
Default value: none

### Example:
```
[1]
Name = Bulbasaur
InternalName = BULBASAUR
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


