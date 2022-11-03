## 🟡 ribbons.txt

Information pulled from the new wiki:
21 May 2022 - https://essentialsdocs.fandom.com/wiki/Defining_a_ribbon
https://essentialsdocs.fandom.com/wiki/Defining_a_ribbon?oldid=1177

The PBS file "ribbons.txt" lists all the defined ribbon in the game. Each section in this file is one separate species, where a section begins with a line containing an ID in square brackets and ends when the next section begins. Each line in a section is one separate piece of information about that species.

Aside from the ID line, every line in a section follows the format:
```
XXX = YYY
```

where XXX is a property and YYY is the value or values associated with it (the spaces are optional).

**🔴 ID number:**
Deleted

**[ID]:**
This is how the scripts refer to the ribbon. Each ribbon must have a different ID. Typically this is the same as the ribbon's name, but written in all capital letters and with no spaces or special characters. In the scripts, the ID is used as a symbol (i.e. with a colon in front of it, e.g. :HOENNCOOL). The ID is never seen by the player.
This line must come first in a section, because, as mentioned above, this line defines when a new section begins.

**Name:**
The name of the ribbon, as seen by the player in a Pokémon's summary screen.

**🟢 IconPosition:**
Is a number that determines which sprite to use from the file Graphics/Pictures/ribbons.png as the image of the ribbon. A value of 0 means the top left sprite, 1 means the second one along in the top row, and so on. The graphic is exactly 8 ribbon sprites wide.

**Description:**
The ribbon's description, as seen by the player in a Pokémon's summary screen.

**🟢 Flags:**
Comma-separated labels applied to the ribbon which can be used to make it behave differently. There are no existing flags.

### Examples

```
[HOENNCOOL]
Name = Cool Ribbon
IconPosition = 0
Description = Hoenn Cool Contest Normal Rank winner!
```