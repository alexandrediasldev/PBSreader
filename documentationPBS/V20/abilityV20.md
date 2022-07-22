## abilities.txt

Information pulled from the new wiki:
23 May 2022 - https://essentialsdocs.fandom.com/wiki/Defining_an_ability
https://essentialsdocs.fandom.com/wiki/Defining_an_ability?oldid=1227

The PBS file "abilities.txt" lists all the defined abilities in the game. Each section in this file is one separate ability, where a section begins with a line containing an ID in square brackets and ends when the next section begins. Each line in a section is one separate piece of information about that ability.

Aside from the ID line, every line in a section follows the format:
```
XXX = YYY
```
where XXX is a property and YYY is the value or values associated with it (the spaces are optional).

**[ID]:**
This is how the scripts refer to the ability. Each ability must have a different ID. Typically this is the same as the ability name, but written in all capital letters and with no spaces or special characters. In the scripts, the ID is used as a symbol (i.e. with a colon in front of it, e.g. :STENCH). The ID is never seen by the player.
This line must come first in a section, because, as mentioned above, this line defines when a new section begins.

**🔴 Internal name:**
REMOVED

**Name:**
The name of the ability, as seen by the player.

**🟢 Flags:**
Comma-separated labels applied to the ability which can be used to make it behave differently. The existing flags are:
- FasterEggHatching - Eggs hatch twice as fast when there are 1 or more Pokémon in the party whose species has this flag.

**Description:**
The ability's description.

### Examples
```
[STENCH]
Name = Stench
Description = The stench may cause the target to flinch.
#-------------------------------
[MAGMAARMOR]
Name = Magma Armor
Flags = FasterEggHatching
Description = Prevents the Pokémon from becoming frozen.
```
