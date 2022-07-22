## 🟡 trainers.txt
# TODO
Information pulled from the new wiki:
30 September 2020 - https://essentialsdocs.fandom.com/wiki/Defining_a_trainer
https://essentialsdocs.fandom.com/wiki/Defining_a_trainer?oldid=938


### Trainer properties

**🟡 Trainer type, trainer's name[, version number]:**
This is the section "header", written in square brackets (rather than in the format XXX = YYY). There are either two or three parts to this line, separated by commas:
1. The internal name of the trainer type.
2. This trainer's name.
3. Optional. A version number to distinguish this trainer from other trainers with the same trainer type and name, when a battle against them is called. Default is 0.
Version numbers are useful for rematches, where they represent different versions of the same trainer changing over time. They are also useful for creating groups of "Grunts" (multiple separate trainers with the same name and appearance, e.g. "Team Rocket Grunt", where "Team Rocket" is the trainer type and "Grunt" is the name). Note that there are rules placed on how you use version numbers for rematch trainers.

**🟡 Items:**
Optional. The internal names of one or more items that this trainer is able to use in-battle, separated by commas.

**🟢 LoseText:**
The in-battle text that appears when this trainer is defeated.

**🟡 Pokemon:**
There are two parts to this line, which are separated by a comma:
1. The internal name of a Pokémon species.
2. A level number.
A trainer can have multiple Pokémon - simply have multiple "Pokemon = YYY" lines.


The properties which are specific to a single Pokémon are typically indented to make it easier to see which Pokémon they apply to (the most recently defined one). Indentation is not necessary, though. They can be written in any order. The available properties are as follows:

### Pokemon properties

**Item:**
The internal name of this Pokémon's held item. Default is no held item.

**Moves:**
The internal names of this Pokémon's moves, separated by commas.
If at least one move is defined here, then this Pokémon's moveset will consist solely of those move(s), with gaps for undefined move slots. If no moves are defined, then this Pokémon's moveset will be the same as for a wild Pokémon of the same species/level/form.

**Ability:**
Either "0" (first natural ability), "1" (second natural ability) or "2" through "5" (hidden abilities). Default is 0.

**Gender:**
Either "male" or "female". Default is the same as the trainer's gender as defined in the PBS file "trainertypes.txt" for their trainer type (male if uncertain). If this Pokémon cannot legitimately be the gender set here, it will instead be the gender (or genderless) it can be.

**Form:**
This Pokémon's form number. Default is 0.

**Shiny:**
Is "yes" if this Pokémon is shiny. Default is "no" (which means it definitely won't be shiny).

**Nature:**
The internal name of this Pokémon's nature. If undefined, the nature depends on this Pokémon's species and the trainer's type (both of which are consistent no matter how many times you battle the trainer, meaning this Pokémon's nature cannot randomly change between battles).

**🟢 IV:**
This Pokémon's IV value(s). Is one to six numbers, each of which is between 0 and 31, which are separated by commas. Default is this Pokémon's level divided by 2 (rounded down), up to a maximum of 31 (i.e. the maximum number of IVs a stat can have).
The IV numbers are written in the order: HP, Attack, Defense, Speed, Special Attack, Special Defense. If there is no number for a stat, it will use the first number (HP's value).

**🟢 EV:**
This Pokémon's EV value(s). Is one to six numbers, each of which is between 0 and 252, which are separated by commas. Default is this Pokémon's level multiplied by 1.5 (rounded down), up to a maximum of 85 (510/6, i.e. the maximum number of EVs a Pokémon can have divided equally between its six stats).
The EV numbers are written in the order: HP, Attack, Defense, Speed, Special Attack, Special Defense. If there is no number for a stat, it will use the first number (HP's value).

**Happiness:**
This Pokémon's happiness. Is a value between 0 and 255. Default is 70.

**Name:**
This Pokémon's nickname. Up to 10 characters long.

**Shadow:**
Is "yes" if this Pokémon is a Shadow Pokémon. Default is "no" (which means it definitely won't be a Shadow Pokémon).

**Ball:**
A number referring to the type of Poké Ball this Pokémon is kept in. These numbers are written in the $BallTypes hash at the top of the script section PokeBall_CatchEffects. Default is 0, which is a regular Poké Ball.

### Examples

```
[CAMPER,Liam]
LoseText = "A very good battle, indeed!"
Pokemon = DIGLETT,10
Pokemon = BONSLY,11
#-------------------------------
[LEADER_Brock,Brock]
Items = FULLRESTORE,FULLRESTORE
LoseText = "Very good."
Pokemon = GEODUDE,12
    Gender = male
    Moves = DEFENSECURL,HEADSMASH,ROCKPOLISH,ROCKTHROW
    Ability = 0
    IV = 20
Pokemon = ONIX,14
    Name = Rocky
    Gender = male
    Shiny = yes
    Moves = HEADSMASH,ROCKTHROW,RAGE,ROCKTOMB
    Ability = 0
    Item = SITRUSBERRY
    IV = 20
    Ball = 19
#-------------------------------
[TEAMROCKET_M,Grunt,1]
LoseText = "You're too good for me!"
Pokemon = WEEPINBELL,21
    Shadow = yes
```

The order in which these properties are written matters to some extent. Some properties relate to the trainer themselves and can be written anywhere within the section (although traditionally they go at the top). Other properties relate to an individual Pokémon owned by the trainer, and relate to the most recently defined Pokémon written above those properties.
