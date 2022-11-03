## 🟢 pokemonforms.txt

Information pulled from the new wiki:
7 July 2020 - https://essentialsdocs.fandom.com/wiki/Forms
https://essentialsdocs.fandom.com/wiki/Forms?oldid=897

The PBS file "pokemonforms.txt" is laid out in nearly the same way as "pokemon.txt".

The first main difference is in the section names (the lines that have square brackets around them to mark the beginning of a new species/form). In "pokemon.txt" these names are simply numbers (the ID of each species), whereas in "pokemonforms.txt" they are the internal name of a species, followed by a hyphen, followed by a form number:
### Example
```
[PICHU-1]
[UNOWN-16]
[SAWSBUCK-2]
```

The other difference is in which properties can be defined. All of this information is optional, even if is it required in "pokemon.txt".

**[Name and IDnumber]**:
 the internal name of a species, followed by a hyphen, followed by a form number

### Opional override

**Type1, Type2**:
If just Type1 is defined, then this form's second type will be the same as this form's first type (i.e. the form will be a single type), rather than inheriting the second type from the base form.
If just Type2 is defined, then this form's first type will be inherited from the base form. There is no harm in defining Type1 as well, though, even if it will be the same as the base form's.

**BaseStats:**
All six stats must be defined if any are.

**BaseExp:**
_



**EffortPoints:**
All six EV stats must be defined if any are.


**Rareness:**
_

**Happiness:**
_

**Abilities
HiddenAbility:**
Both of these properties must be defined if either are any different to the base form's. If one of these properties is left blank, it will not inherit from the base form, but will instead be treated as empty.

**Moves:**
The entire moveset must be defined here if it is at all different to that of the base form's.

**EggMoves:**
The entire set of egg moves must be defined here if it is at all different to that of the base form's.
Species with different egg moves depending on their form should not be able to change their form at all. The breeding code does not support that.


**StepsToHatch:**
_

**Height:**
_

**Weight:**
_

**Color:**
_

**Shape:**
_

**Habitat:**
_

**Kind:**
_

**Pokedex:**
_

**FormName:**
If this is blank, then this form will not appear in the Pokédex.
If you have a species which has gender differences in an alternate form, you should define them as two separate forms instead. Only one version of each alternate form will appear in the Pokédex.

**WildItemCommon,WildItemUncommon,WildItemRare:**
All three of these properties must be defined if any are different to the base form's. If one of these properties is left blank, it will not inherit from the base form, but will instead be treated as empty.

**BattlerPlayerY
BattlerEnemyY
BattlerAltitude:**
_

**Evolutions:**
These should only affect the evolution method and associated variable (e.g. Alolan Vulpix using an Ice Stone rather than a Fire Stone), and not which species a Pokémon can evolve into. The code does not well support varying evolution paths between forms of a species (i.e. evolving into different species depending on form).
If you want to have varying evolution paths, though (i.e. different forms evolve into different species), then the base form defined in "pokemon.txt" should list ALL of those species, not just the one(s) the base form can evolve into. To ensure that the base form cannot evolve into a species it shouldn't, make it evolve into those unattainable species via evolution methods that are impossible for it to achieve (e.g. levelling up on a non-existent map). Just be aware that you may run into other difficulties too.

If you just want to change HOW a particular form evolves (e.g. change which evolution stone is required, or change the evolution method), but not WHAT it evolves INTO, you can ignore the previous paragraph.

### Exclusive

In addition to the above, there are also some properties exclusive to alternate forms which can also be defined. These properties are all relevant to Mega Evolution forms.

**MegaStone:**
The internal name of an item which needs to be held to allow the holder to Mega Evolve into this form.
These items cannot be dropped or otherwise lost in battle.

**UnmegaForm:**
A Pokémon of this Mega Evolved form reverts to its unmega form at the end of battle. If undefined, this is 0.


**MegaMove:**
The internal name of a move which needs to be known by a Pokémon to allow that Pokémon to Mega Evolve into this form. This typically only applies to Rayquaza (whose move is Dragon Ascent).


**MegaMessage:**
A number which indicates the message that is shown when a Pokémon is Mega Evolving into this form. The messages themselves are hardcoded in def pbMegaEvolve in script section PokeBattle_Battle. If undefined, this is 0. This typically only applies to Rayquaza (which uses message 1).
- 0 = "{Pokémon}'s {Mega Stone} is reacting to {Player}'s {Mega Ring}!"
- 1 = "{Player}'s fervent wish has reached {Pokémon}!"

### Forbidden

For completion's sake, the following properties cannot be defined for an alternate form, even though they can be defined in "pokemon.txt". The reasons for why they are disabled vary.

**Name:**
The species name is for the species as a whole, not for individual forms.

**InternalName:**
The internal name is for the species as a whole, not for individual forms.

**GenderRate:**
There can be a clash between having a form-specific gender rate and forms which depend on the Pokémon's gender (e.g. Meowstic).

**GrowthRate:**
If a Pokémon's form changes, this property being form-specific will change the Pokémon's level, which is not desirable.

**Compatibility:**
No real reason, but it doesn't make sense for a form to be so different to its base form that it can breed with different species.

**RegionalNumbers:**
The Regional Dex numbers are for the species as a whole, not for individual forms.

**Incense:**
Difficulties ensuring that breeding will produce the correct offspring.
