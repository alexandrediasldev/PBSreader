## trainers.txt

Information pulled from the old wiki on the way back machine:  
September 28th 2015 - http://pokemonessentials.wikia.com/wiki/Defining_a_trainer  
https://web.archive.org/web/20150928175006/http://pokemonessentials.wikia.com/wiki/Defining_a_trainer

**1. Trainer type:**  	
The internal name of the trainer's type, as defined above.

**2. Trainer Name:**  	
The trainer's name (e.g. Dave).
If there is more than one trainer with the same name and trainer type, then add on a comma and a number (between 0 and 255) at the end of this line, to distinguish between them. When creating the trainer event, include this number to show which version you want. The number will not be shown anywhere. Typically done to allow rematches with a trainer, when they will have stronger Pokémon (not necessary if the trainer will be identical each time), or to make a bunch of "Grunt"s (the "Team Rocket" part of a "Team Rocket Grunt" will be the trainer type's name).
You should start with 0 and work onwards from there without skipping any numbers. This order determines the order in which each version of the trainer is rebattled (i.e. the trainer should get stronger as its version number gets higher).
You do not need to include a number if the trainer types are different, e.g. Camper Dave and Fisherman Dave.

**3. Items**  	
There are two main parts to this line, with each part separated by a comma:
First, the number of Pokémon this trainer has.
Second, a comma-separated list of all the items this trainer has. They are the internal names of those items. The limit is 8 items.
The Pokémon count is necessary, but the items are all optional. If the trainer does not have any items, the line will simply consist of a single number (no commas).

**4.   Pokemon:**  	
There are a number of lines here, each one corresponding to a single Pokémon. The total number of Pokémon lines is the Pokémon count number in line 3. Each Pokémon line has up to 17 parts (only the first two, species and level, are necessary), with each part separated by a comma:
1. Species - The internal name thereof.
2. Level.
3. Held item - The internal name thereof.
4. Move 1 - The internal name thereof. If at least one move is given, then the Pokémon's moveset will consist solely of those move(s). If no moves are given, then the moveset will be the same as a wild Pokémon of the same species and Level.
5. Move 2 - The internal name thereof.
6. Move 3 - The internal name thereof.
7. Move 4 - The internal name thereof.
8. Ability - Either 0 (first natural ability), 1 (second natural ability) or 2-5 (hidden abilities). Leave blank to have it be determined by the personal ID normally.
9. Gender - Either M or 0 (male) or F or 1 (female). Leave blank to have it be determined by the personal ID normally.
10. Form - Default is 0.
11. Shininess - shiny or TRUE if the Pokémon is shiny, FALSE if not. Default is FALSE.
12. Nature - The internal name thereof. Leave blank to have it be determined by the personal ID normally.
13. IVs - A single value between 0 and 31. Each of the Pokémon's IVs (HP, Attack, Defense, Speed, Special Attack, Special Defense) will be equal to this number. Default is 10.
14. Happiness - A value between 0 and 255. Default is 70.
15. Nickname - Up to 10 characters long.
16. Shadow Pokémon - TRUE if the Pokémon is a Shadow Pokémon, FALSE if not. Default is FALSE.
17. Ball type - The type of Poké Ball the Pokémon is kept in.
   
### Exampless

```
YOUNGSTER
Ben
2
RATTATA,11
EKANS,12
This describes Youngster Ben, who has 2 Pokémon (Rattata and Ekans) and no items.
Rattata is level 11, and Ekans is level 12. Neither Pokémon have any specifically-defined properties.

LEADER_Brock
Brock,0
2,FULLRESTORE,FULLRESTORE
GEODUDE,12,,DEFENSECURL,HEADSMASH,ROCKPOLISH,ROCKTHROW,,0,,,,20
ONIX,14,SITRUSBERRY,HEADSMASH,ROCKTHROW,RAGE,ROCKTOMB,,0,,true,,20,,Rocky,,19
This describes one version of Leader Brock (as noted by the "0" after his name).
This version has two Pokémon (Geodude and Onix) and two items (both of them Full Restores).
Geodude is level 12, and Onix is level 14. Both Pokémon have a custom moveset, are male, and have IVs of 20.
Onix holds a Sitrus Berry, is shiny, is nicknamed "Rocky" and comes in Poké Ball number 19 (a Heavy Ball).
```