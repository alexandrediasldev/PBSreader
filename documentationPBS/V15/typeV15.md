## types.txt

Information pulled from the old wiki on the way back machine:
September 28th 2015 - http://pokemonessentials.wikia.com/wiki/Defining_a_type
https://web.archive.org/web/20150928175604/http://pokemonessentials.wikia.com/wiki/Defining_a_type
### Mandatory

**[IDnumber]**:
Each section begins with a number in square brackets, followed by a number of lines.
The number in square brackets must be different for each type. It should begin with 0 and continue with no missing numbers.

**Name**:
The name of this type (e.g. Fire, Water).

**InternalName**:
The name used by the scripts to refer to this type. It is never shown to the player. It is typically the type's name but in all capitals.


### Optional

**IsPseudoType**:
Is either TRUE or FALSE. If TRUE, this type is a pseudotype, i.e. not a "proper" type. The ??? type is an example of a pseudotype. If this line isn't included, this type will NOT be a pseudotype.
No Pokémon should have a pseudotype as one of its elemental types. Pseudotypes cannot be searched for in the Pokédex, and the move "Conversion" and the ability "Color Change" cannot change a Pokémon's type to a pseudotype.

**IsSpecialType**:
Is either TRUE or FALSE. If TRUE, moves of this type will use the special stats for damage calculation. If FALSE, they will use the physical stats. If this line isn't included, this type will be a physical type.
This doesn't normally matter, though, as by default a move is defined individually as physical or special rather than determining this based on its elemental type (like in newer games). By changing an option in the script section Settings, though, moves can be made to be physical or special depending on their type (like in older games).

**Weaknesses**:
A comma-separated list of the internal names of all the elemental types that will inflict double damage (i.e. are super effective) against a Pokémon of this type.

**Resistances**:
A comma-separated list of the internal names of all the elemental types that will inflict half damage (i.e. are not very effective) against a Pokémon of this type.

**Immunities**:
A comma-separated list of the internal names of all the elemental types that cannot inflict any damage on a Pokémon of this type.




### Example

```
[0]
Name=Normal
InternalName=NORMAL
Weaknesses=FIGHTING
Immunities=GHOST

[17]
Name=Dark
InternalName=DARK
IsSpecialType=true
Weaknesses=FIGHTING,BUG
Resistances=GHOST,DARK
Immunities=PSYCHIC
```

