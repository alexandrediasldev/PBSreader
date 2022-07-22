## 🟢 pokemon_metrics.txt

Information pulled from the new wiki:
21 May 2022 - https://essentialsdocs.fandom.com/wiki/Defining_a_species
https://essentialsdocs.fandom.com/wiki/Defining_a_species?oldid=1174

The PBS file "pokemon_metrics.txt" lists all of these metrics. Each section in this file is one separate species or form, where a section begins with a line containing an ID (and optional form number) in square brackets and ends when the next section begins. Each line in a section is one separate metric.

Aside from the ID line, every line in a section follows the format:
```
XXX = YYY
```
where XXX is a property and YYY is the value or values associated with it (the spaces are optional).


**[ID] [ID,form]:**
A species ID (see above), or a species ID with a form number. For example, [BULBASAUR] or [CASTFORM,2].
This line must come first in a section, because, as mentioned above, this line defines when a new section begins.

**BackSprite:**
X and Y offsets of the back sprite in pixels. A higher number means the back sprite is placed further right/lower down in the screen. Each value can be positive or negative. The number of pixels moved in a direction is double the corresponding value given here.

**FrontSprite:**
X and Y offsets of the front sprite in pixels. A higher number means the front sprite is placed further right/lower down in the screen. Each value can be positive or negative. The number of pixels moved in a direction is double the corresponding value given here.

**FrontSpriteAltitude:**
Another Y offset of the front sprite in pixels, used to represent the Pokémon's height above the ground. A higher number means the front sprite is placed further up the screen. Can be positive or negative. The number of pixels moved is double the value given here.
This property is typically unused because FrontSprite can do the same thing.

**ShadowX:**
Affects the horizontal positioning of the shadow beneath the front sprite of the species in battle. A higher number means the shadow is placed further right on the screen. Can be positive or negative. The number of pixels moved is double the value given here.

**ShadowSize:**
A number that determines which shadow graphic to place underneath the front sprite of the species in battle. It can be 0 or higher. By default, there are three possible shadow graphics (in the folder "Graphics/Pokemon/Shadow"), ranging from 1 (smallest) to 3 (largest).

### Example

```
[BULBASAUR]
BackSprite = -4,0
FrontSprite = -1,26
ShadowX = 0
ShadowSize = 2
```