## abilities.txt

Information pulled from the old wiki on the way back machine:
September 28th 2015 - http://pokemonessentials.wikia.com/wiki/Defining_an_ability
https://web.archive.org/web/20150928174615/http://pokemonessentials.wikia.com/wiki/Defining_an_ability

### Mandatory

**ID number:**
Each ability's ID number must be different. The ID number must be a whole number greater than 0 (i.e. 1,2,3...), up to 255 inclusive. Missing numbers are not a problem (e.g. the sequence 23,24,25,58,59,60,... is allowed).

**Internal name:**
Typically written only in capital letters with no spaces or symbols. This is the name the scripts refer to and use. This name is never seen by the player.

**Display name:**
The actual name of the ability. This is only used when displaying the ability's name on the screen.

**Description:**
The description of the ability.
If there are any commas or apostrophes/double quote marks in the description, the entire description must be enclosed in double quote marks. The double quote marks in the description must also be preceded by a backslash "\".

### Examples
```
1,STENCH,Stench,"The stench may cause the target to flinch."
2,DRIZZLE,Drizzle,"The Pokémon makes it rain if it appears in battle."
3,SPEEDBOOST,Speed Boost,"Its Speed stat is gradually boosted."
```
