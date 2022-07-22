## 🟡 trainer_types.txt

Information pulled from the new wiki:
23 May 2022 - https://essentialsdocs.fandom.com/wiki/Defining_a_trainer
https://essentialsdocs.fandom.com/wiki/Defining_a_trainer?oldid=1229

The PBS file "trainer_types.txt" lists all the defined trainer types in the game. Each section in this file is one separate trainer type, where a section begins with a line containing an ID in square brackets and ends when the next section begins. Each line in a section is one separate piece of information about that trainer type.

🟡 Aside from the ID line, every line in a section follows the format:
```
XXX = YYY
```

where XXX is a property and YYY is the value or values associated with it (the spaces are optional).

**[ID]**
This is how the scripts refer to the trainer type. Each trainer type must have a different ID. Typically this is the same as the trainer type's name, but written in all capital letters and with no spaces or special characters. In the scripts, the ID is used as a symbol (i.e. with a colon in front of it, e.g. :SISANDBRO). The ID is never seen by the player.
This line must come first in a section, because, as mentioned above, this line defines when a new section begins.

**🔴 Internal Name:**
REMOVED

**Name:**
The name of the trainer type, as seen by the player. Multiple trainer types can have the same name, although they cannot share an ID.

**Gender:**
The gender of all trainers of this type. Is one of:
- Male
- Female
- Unknown (e.g. if the type contains both a male and female trainer)

**Base money:**
The base amount of money earned from defeating a trainer of this type. The base money value is multiplied by the highest Level among all the trainer's Pokémon to produce the actual amount of money gained (assuming no other modifiers). Is 0 or a positive number.

**Skill Level:**
The skill level of all trainers of this type, used for battle AI. Higher numbers represent higher skill levels. Is 0 or a positive number. By default, the highest value that makes a difference to the AI is 100.

**🟢 Flags:**
Comma-separated labels applied to the trainer type which can be used to make it behave differently. There are no existing flags.

**🟡 IntroBGM:**
The music that plays before the battle begins, while still talking to the trainer. The name of a background music (BGM) file in the folder "Audio/BGM" (excluding its file extension).

**Battle BGM:**
The music that plays during battles against trainers of this type. Is the name of a background music (BGM) file in the folder "Audio/BGM" (excluding its file extension). Typically only defined for Gym Leaders, Elite Four members and rivals.

**🟡 VictoryBGM:**
The music that plays during battles against trainers of this type. Is the name of a background music (BGM) file in the folder "Audio/BGM" (excluding its file extension). Typically only defined for Gym Leaders, Elite Four members and rivals.

**🔴 Skill codes:**
REMOVED

### Examples
```
[POKEMONTRAINER_Red]
Name = Pokémon Trainer
Gender = Male
BaseMoney = 60
#-------------------------------
[SISANDBRO]
Name = Sis and Bro
Gender = Unknown
BaseMoney = 16
SkillLevel = 48
#-------------------------------
[LEADER_Misty]
Name = Gym Leader
Gender = Female
BaseMoney = 100
BattleBGM = Battle Gym Leader
VictoryBGM = Battle victory leader
```
