## 🟡 pokemon.txt
Information pulled from the new wiki:
21 May 2022 - https://essentialsdocs.fandom.com/wiki/Defining_a_species
https://essentialsdocs.fandom.com/wiki/Defining_a_species?oldid=1174

The PBS file "pokemon.txt" lists all the defined Pokémon species in the game. Each section in this file is one separate species, where a section begins with a line containing an ID in square brackets and ends when the next section begins. Each line in a section is one separate piece of information about that species.
Aside from the ID line, every line in a section follows the format:
```
XXX = YYY
```

where XXX is a property and YYY is the value or values associated with it (the spaces are optional). For example:

**[ID]**:
This is how the scripts refer to the species. Each species must have a different ID. Typically this is the same as the species name, but written in all capital letters and with no spaces or special characters. In the scripts, the ID is used as a symbol (i.e. with a colon in front of it, e.g. :BULBASAUR). The ID is never seen by the player.
This line must come first in a section, because, as mentioned above, this line defines when a new section begins.

The order in which Pokémon are defined in the PBS file "pokemon.txt" is the order in which they are listed in the National Pokédex; their National Pokédex numbers are determined automatically.

**Name**:
The name of the species, as seen by the player.

**🔴 InternalName**:
REMOVED

**Types**:
One or two elemental types, separated by a comma if there are two.

**BaseStats:**
Six comma-separated values, corresponding to the order that main stats are defined. By default, the order is:
- HP
- Attack
- Defense
- Speed
- Special Attack
- Special Defense
Each value can be 1 or higher. If HP is 1, Pokémon of this species will always have a total HP of exactly 1 (i.e. Shedinja).

**🟡 GenderRatio:**
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
- Medium (known elsewhere as Medium Fast)
- Slow
- Parabolic (known elsewhere as Medium Slow)
- Erratic
- Fluctuating


**BaseEXP:**
The base amount of Experience gained from defeating a Pokémon of the species. It must be a whole number that is 1 or higher.
This base amount is used in a calculation to determine the actual number of Exp. points awarded for defeating a Pokémon of the species.

**🟡 EVs:**
The number of EVs gained by defeating a Pokémon of the species. Is any number of pairs of values, the first of each being a stat and the second of each being the number of EVs of that stat that are gained.
For example, SPECIAL_ATTACK,1 or SPECIAL_ATTACK,2,SPECIAL_DEFENSE,1.

As a rule, the total of these numbers should be between 1 and 3, and higher evolutions tend to give more EVs.

**🟡 CatchRate:**
The catch rate of the species. It can be 0 or higher (typically the highest is 255). The higher the number, the more likely a capture (0 means it cannot be caught by anything except a Master Ball).

**Happiness:**
The amount of happiness a newly caught Pokémon of the species will have. It can be 0 or higher, although it is typically 70. The game treats 255 as the highest attainable happiness.

**Abilities:**
The IDs of one or two abilities that the species can have. If there are two abilities, separate them with a comma.

**HiddenAbility:**
The IDs of any number of additional abilities that the species can have. If there are multiple abilities here, they are separated by commas.
Pokémon cannot have any Hidden Ability naturally, and must be specially given one.

**Moves:**
The moves that all Pokémon of the species learn as they level up. This line consists of comma-separated level/move pairs which are themselves comma-separated, i.e. level,move,level,move,level,move.... Each pair contains the level at which the Pokémon will learn the move, followed by the ID of the move it will learn.
A level of 0 means the move will be learned when a Pokémon evolves into the species, and not at any other point (except via the Move Relearner).

**TutorMoves:**
A comma-separated list of the IDs of moves that a Pokémon of the species can be taught by a HM, TM, TR or Move Tutor. If a move is not listed here, it cannot be taught by those methods, even if the move appears in its Moves or EggMoves properties.

**EggMoves:**
A comma-separated list of the IDs of moves that a Pokémon of the species can only learn as an egg (obtained through breeding). Only species that can be in eggs should have this line (typically only unevolved species).

**🟡 EggGroups:**
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
"Water1" is for sea creatures, "Water2" is for fish, and "Water3" is for shellfish. "Ditto" should contain only Ditto, as a species in that group can breed with any other breedable Pokémon. If any egg group is "Undiscovered", the species cannot breed.

**🟡 HatchSteps:**
The number of steps it takes to hatch an egg of the species. It can be 1 or higher. Note that this is not the number of egg cycles for the species, but the actual number of steps. Only species that can be in eggs should have this line (typically only unevolved species).

**🟢 Offspring:**
One or more species IDs that an egg can be will be when produced by a mother of this species. This property can include this species. If this property is not defined, then the species of eggs produced by mothers of this species will be determined normally. If multiple species are listed, an egg has an equal chance to be each of them.
For example, Volbeat lists VOLBEAT,ILLUMISE, and Manaphy lists PHIONE.

**Height:**
The height of the species in meters, to one decimal place. Use a period for the decimal point, and do not use commas for thousands.
The Pokédex will automatically show this height in feet/inches if the game recognises that the player is in the USA. This is only cosmetic; the rest of the scripts still perform calculations using the meters value defined.

**Weight:**
The weight of the species in kilograms, to one decimal place. Use a period for the decimal point, and do not use commas for thousands.
The Pokédex will automatically show this weight in pounds if the game recognises that the player is in the USA. This is only cosmetic; the rest of the scripts still perform calculations using the kilograms value defined.

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

This information is unused in Essentials.

**🟡 Category:**
The species' category, which is displayed in the Pokédex. For example, Bulbasaur is the Seed Pokémon. The word "Pokémon" is automatically added to the end, so only "Seed" needs to be here.

**Pokedex:**
The text of the Pokédex entry.

**FormNames:**
The name of this form of the species (form 0), if it has one.
If this is blank, then its form name as shown in the Pokédex's Forms page will be "Male"/"Female" if the species is gendered. If the species is genderless, its form name will instead be "Genderless" (if this is the only form for the species) or "One Form" (if the species also has other forms).

**Generation:**
A number representing the generation of Pokémon games in which this species first appeared. This information is unused in Essentials.

**🟢 Flags:**
Comma-separated labels applied to the species which can be used to make it behave differently. The existing flags are:
- UltraBeast - The Beast Ball has a different catch rate for Pokémon with this flag.
- DefaultForm_0, DefaultForm_1, DefaultForm_2 - The form that Pokémon of a species with this flag will have by default. The number can be any number, not just the ones listed here.
- InheritFormFromMother - An egg produced by a mother with this flag will inherit the mother's form.
- InheritFormWithEverStone - An egg produced by a parent with this flag will inherit that parent's form if that parent is holding an Ever Stone. The mother's form takes priority.

**WildItemCommon
WildItemUncommon
WildItemRare:**
The IDs of items that a wild Pokémon of the species may be found holding. Each line can have any number of items, which are equally likely to be chosen if that rarity of item will be used.
The chances of holding the item for each rarity are 50%, 5% and 1% respectively. If all three are the same item, then the chance of holding it is 100% instead.

**🔴 BattlerPlayerX
BattlerPlayerY
BattlerEnemyX
BattlerEnemyY
BattlerAltitude
BattlerShadowX
BattlerShadowSize:**
REMOVED




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
If there are multiple evolution paths, they are separated by commas. The three parts of each evolution path are also separated by commas. Be careful to include the correct number of commas when writing an evolution path whose method doesn't use a parameter.

**Incense:**
The ID of an item that needs to be held by a parent when breeding in order for the egg to be this species. If neither parent is holding the required item, the egg will be the next evolved species instead.
The only species that should have this line are ones which cannot breed, but which evolve into a species that can. That is, the species should be a "baby" species. Not all baby species need this line. Note that Essentials does not have any formal definition of what a "baby" species is.


### Example:
```
[1]
[BULBASAUR]
Name = Bulbasaur
Types = GRASS,POISON
BaseStats = 45,49,49,45,65,65
GenderRatio = FemaleOneEighth
BaseExp = 64
Moves = 1,TACKLE,1,GROWL,3,VINEWHIP,6,GROWTH,9,LEECHSEED,12,RAZORLEAF,15,POISONPOWDER,15,SLEEPPOWDER,18,SEEDBOMB,21,TAKEDOWN,24,SWEETSCENT,27,SYNTHESIS,30,WORRYSEED,33,DOUBLEEDGE,36,SOLARBEAM
Height = 0.7
Pokedex = Bulbasaur can be seen napping in bright sunlight. There is a seed on its back. By soaking up the sun's rays, the seed grows progressively larger.
Evolutions = IVYSAUR,Level,16
```


