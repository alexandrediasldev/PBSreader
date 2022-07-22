## 🟡 trainers.txt
Information pulled from the new wiki:
21 May 2022 - https://essentialsdocs.fandom.com/wiki/Defining_a_trainer
https://essentialsdocs.fandom.com/wiki/Defining_a_trainer?oldid=1178

The PBS file "trainers.txt" lists all the defined individual trainers in the game. Each section in this file is one separate individual trainer, where a section begins with a line surrounded by square brackets and ends when the next section begins. Each line in a section is one separate piece of information about that trainer or one of their Pokémon.

The section's "header", the line surrounded by square brackets, has a trainer type's ID, followed by a comma and then the name of the individual trainer. If the trainer requires a version number to differentiate it from other trainers with the same type/name (see below), that version number is also included here after another comma.

The rest of the lines in each section are written in the format
```
XXX = YYY
```
where XXX is a property and YYY is the value or values associated with it (the spaces are optional).

Some lines may be indented, but this makes no difference and is just done to make things more legible. Any line beginning with a # (including the lines separating one trainer from the next) are comment lines and are not compiled; again, they are just there to make things more legible.

The order in which these properties are written matters to some extent. Some properties relate to the trainer themselves and must be written before the first Pokémon line for that trainer. Other properties relate to an individual Pokémon owned by the trainer, and relate to the most recently defined Pokémon written above those properties.

### Trainer properties

**[TRAINERTYPE,Name]
[TRAINERTYPE,Name,number]:**
This is the section "header", written in square brackets (rather than in the format XXX = YYY). There are either two or three parts to this line, separated by commas:
1. The ID of the trainer type.
2. This trainer's name.
3. Optional. A version number to distinguish this trainer from other trainers with the same trainer type and name, when a battle against them is called. Default is 0.
Version numbers are useful for rematches, where they represent different versions of the same trainer changing over time. They are also useful for creating groups of "Grunts" (multiple separate trainers with the same name and appearance, e.g. "Team Rocket Grunt", where "Team Rocket" is the trainer type and "Grunt" is the name). Note that there are rules placed on how you use version numbers for rematch trainers.

**Items:**
Optional. The IDs of one or more items that this trainer is able to use in battle, separated by commas. If the trainer is able to Mega Evolve, a Mega Ring item should be listed here.

**LoseText:**
The in-battle text that appears when this trainer is defeated.

**Pokemon:**
There are two parts to this line, which are separated by a comma:
The ID of a Pokémon species.
A level number.
A trainer can have multiple Pokémon - simply have multiple "Pokemon = YYY" lines.


The properties which are specific to a single Pokémon are typically indented to make it easier to see which Pokémon they apply to (the most recently defined one). Indentation is not necessary, though. They can be written in any order within the space after the "Pokemon = YYY" line they apply to.

### Pokemon properties

**Name:**
This Pokémon's nickname. Up to 10 characters long. Default is no nickname.

**Form:**
This Pokémon's form number. Default is 0.

**Gender:**
Either "male" or "female". Default is the same as the trainer's gender, as defined in the PBS file "trainer_types.txt" for their trainer type (male if unknown). If this Pokémon cannot legitimately be the gender set here, it will instead be the gender (or genderless) it can be.

**Shiny:**
Is "yes" if this Pokémon is shiny. Default is "no" (which means it definitely won't be shiny).

**🟢 SuperShiny:**
Is "yes" if this Pokémon is super shiny. Super shininess takes priority over regular shininess. Default is "no" (which means it definitely won't be super shiny).

**Shadow:**
Is "yes" if this Pokémon is a Shadow Pokémon. Default is "no" (which means it definitely won't be a Shadow Pokémon).

**Moves:**
The IDs of this Pokémon's moves, separated by commas.
If at least one move is defined here, then this Pokémon's moveset will consist solely of those move(s), with gaps for undefined move slots. If no moves are defined, then this Pokémon's moveset will be the same as that of a wild Pokémon of the same species/level/form.

**Ability:**
The ID of the ability this Pokémon has. Default is undefined, meaning the "AbilityIndex" property will be used to determine the Pokémon's ability. This can give the Pokémon any ability at all, but it will be lost if the Pokémon changes form or species, and the Pokémon will then determine its ability using the usual calculations instead.

**🟢 AbilityIndex:**
Either "0" (first natural ability), "1" (second natural ability), or "2"+ (hidden abilities). Default is 0.
Unlike the "Ability" property, "AbilityIndex" will not be lost if the Pokémon changes form or species.

**Item:**
The ID of this Pokémon's held item. Default is no held item.

**Nature:**
The ID of this Pokémon's nature. If undefined, the nature depends on this Pokémon's species and the trainer's type (both of which are consistent no matter how many times you battle the trainer, meaning this Pokémon's nature cannot randomly change between battles).

**IV:**
This Pokémon's IV value(s). Is one to six numbers, each of which is between 0 and 31, which are separated by commas. Default is this Pokémon's level divided by 2 (rounded down), up to a maximum of 31 (i.e. the maximum number of IVs a stat can have).
The order of these numbers corresponds to the pbs_order of the main stats. By default, the order is: HP, Attack, Defense, Speed, Special Attack, Special Defense. If there is no number for a stat, it will use the first number given here (HP's value).

**EV:**
This Pokémon's EV value(s). Is one to six numbers, each of which is between 0 and 252, which are separated by commas. Default is this Pokémon's level multiplied by 1.5 (rounded down), up to a maximum of 85 (510/6, i.e. the maximum number of EVs a Pokémon can have, divided equally between its six stats).
The order of these numbers corresponds to the pbs_order of the main stats. By default, the order is: HP, Attack, Defense, Speed, Special Attack, Special Defense. If there is no number for a stat, it will use the first number given here (HP's value).

**Happiness:**
This Pokémon's happiness. Is a value between 0 and 255. Default is 70.

**Ball:**
The ID of the Poké Ball item this Pokémon is kept in. Default is a regular Poké Ball.

### Examples

```
[CAMPER,Liam]
LoseText = A very good battle, indeed!
Pokemon = DIGLETT,10
Pokemon = BONSLY,11
#-------------------------------
[LEADER_Brock,Brock]
Items = FULLRESTORE,FULLRESTORE
LoseText = Very good.
Pokemon = GEODUDE,12
    Gender = male
    Moves = DEFENSECURL,HEADSMASH,ROCKPOLISH,ROCKTHROW
    AbilityIndex = 0
    IV = 20,20,20,20,20,20
Pokemon = ONIX,14
    Name = Rocky
    Gender = male
    Shiny = yes
    Moves = HEADSMASH,ROCKTHROW,RAGE,ROCKTOMB
    AbilityIndex = 0
    Item = SITRUSBERRY
    IV = 20,20,20,20,20,20
    Ball = HEAVYBALL
#-------------------------------
[TEAMROCKET_M,Grunt,1]
LoseText = You're too good for me!
Pokemon = WEEPINBELL,21
    Shadow = yes
```
