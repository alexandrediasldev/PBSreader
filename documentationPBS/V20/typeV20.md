## types.txt

Information pulled from the new wiki:
2 July 2022 - https://essentialsdocs.fandom.com/wiki/Defining_a_type
https://essentialsdocs.fandom.com/wiki/Defining_a_type?oldid=1404

The PBS file "types.txt" lists all the defined types in the game. Each section in this file is one separate type, where a section begins with a line containing an ID in square brackets and ends when the next section begins. Each line in a section is one separate piece of information about that type.

Aside from the ID line, every line in a section follows the format:

```
XXX = YYY
```

where XXX is a property and YYY is the value or values associated with it (the spaces are optional).

**[ID]**:
This is how the scripts refer to the type. Each type must have a different ID. Typically this is the same as the type's name, but written in all capital letters and with no spaces or special characters. In the scripts, the ID is used as a symbol (i.e. with a colon in front of it, e.g. :NORMAL). The ID is never seen by the player.
This line must come first in a section, because, as mentioned above, this line defines when a new section begins.

**Name**:
The name of this type, as seen by the player.

**🔴 InternalName**:
The name used by the scripts to refer to this type. It is never shown to the player. It is typically the type's name but in all capitals.

**🟢 IconPosition:**
Is a number that determines which icon to use to represent this type. See below for a list of graphics that use this number. A value of 0 means the top icon in these graphics, 1 means the second icon, and so on.
This value is also used by Hidden Power when determining its type.

**IsSpecialType**:
Is either true or false. If true, moves of this type will use the special stats for damage calculation. If false or undefined, they will use the physical stats.
This only applies if the setting MOVE_CATEGORY_PER_MOVE is false, though, which is only the case in the Gen 3 and older games. If that setting is true (as in Gen 4 and later), each move individually determines whether it is physical or special.

**IsPseudoType**:
Is either true or false. If true, this type is a pseudotype, i.e. not a "proper" type. The ??? type is an example of a pseudotype. If false or undefined, this type will NOT be a pseudotype.
No Pokémon should have a pseudotype as one of its elemental types. Pseudotypes cannot be searched for in the Pokédex, the move "Conversion" and the ability "Color Change" cannot change a Pokémon's type to a pseudotype, and so on.

**🟢 Flags:**
Comma-separated labels applied to the species which can be used to make it behave differently. There are no existing flags.

**Weaknesses**:
A comma-separated list of the IDs of all the elemental types that will inflict double damage (i.e. are super effective) against a Pokémon of this type.

**Resistances**:
A comma-separated list of the IDs of all the elemental types that will inflict half damage (i.e. are not very effective) against a Pokémon of this type.

**Immunities**:
A comma-separated list of the IDs of all the elemental types that cannot inflict any damage on a Pokémon of this type.




### Example

```
[NORMAL]
Name = Normal
IconPosition = 0
Weaknesses = FIGHTING
Immunities = GHOST
#-------------------------------
[DARK]
Name = Dark
IconPosition = 17
IsSpecialType = true
Weaknesses = FIGHTING,BUG,FAIRY
Resistances = GHOST,DARK
Immunities = PSYCHIC
```

