## 🟡 pokemon_forms.txt

Information pulled from the new wiki:
31 May 2022 - https://essentialsdocs.fandom.com/wiki/Forms
https://essentialsdocs.fandom.com/wiki/Forms?oldid=1267

A Pokémon's base form is defined in the PBS file "pokemon.txt", while its alternate forms are defined in the PBS file "pokemon_forms.txt". Alternate forms will inherit the properties of the base form, except ones that are defined in "pokemon_forms.txt" for that form. The PBS file "pokemon_forms.txt" therefore only needs to list the differences between each form of a species compared to its base form.

With a few exceptions (see below), anything defined about a species in the PBS file "pokemon.txt" can be overridden for an alternate form of that species.

The PBS file "pokemon_forms.txt" is laid out in nearly the same way as "pokemon.txt". It has a number of sections, each beginning with something in square brackets followed by any number of lines in the form XXX = YYY. The latter are exactly the same as in "pokemon.txt". Any line beginning with a # (including the lines separating one form from the next) are comment lines and are not compiled; they are just there to make things more legible and are not required.

The sections names (the text in square brackets) are comprised of two parts: a species ID and a form number. They are separated by a comma.



Most properties that are defined in the PBS file "pokemon.txt" can also be defined for a form in "pokemonforms.txt". All of these properties are optional for a form. If a property is not defined for a form, that form will inherit the property from the base form in "pokemon.txt".
Remember that form 0 is the base form that is defined in "pokemon.txt", so a form number of 0 cannot be used in "pokemon_forms.txt".

**🟡 [Name, IDnumber]**:
 the internal name of a species, followed by a comma

### Definable properties

**Types:**
_

**BaseStats:**
All six stats must be defined if any are, even if some are the same as the base form's.

**BaseExp:**
_

**🟡 EVs:**
_

**🟡 CatchRate:**
_

**Happiness:**
_

**Abilities
HiddenAbility:**
If either of these properties is blank, it will inherit from the base form even if the other property is defined for this form.

**Moves:**
The entire moveset must be defined here if it is at all different to that of the base form.

**TutorMoves:**
The entire set of TM/tutor moves must be defined here if it is at all different to that of the base form.


**EggMoves:**
The entire set of egg moves must be defined here if it is at all different to that of the base form.
Species with different egg moves depending on their form should not be able to change their form at all. The breeding code does not support that.

**🟡 EggGroups:**
Generally used to put a certain form in the Undiscovered egg group, i.e. making that form unable to breed.

**🟡 HatchSteps:**
_

**🟢 Offspring:**
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

**🟡 Category:**
_

**Pokedex:**
_

**FormName:**
If this is blank, then this form will not appear in the Pokédex.
If you have a species which has gender differences in an alternate form, you should define them as two separate forms instead. Only one version of each alternate form will appear in the Pokédex.

**Generation:**
_

**🟢 Flags:**
_

**WildItemCommon
WildItemUncommon
WildItemRare:**
All three of these properties must be defined if any are different to the base form's. If one of these properties is left blank, it will not inherit from the base form, but will instead be treated as empty.

**🔴 BattlerPlayerX
BattlerPlayerY
BattlerEnemyX
BattlerEnemyY
BattlerAltitude
BattlerShadowX
BattlerShadowSize:**
REMOVED

**Evolutions:**
These may change how a Pokémon evolves (e.g. Alolan Vulpix using an Ice Stone rather than a Fire Stone), change what it evolves into (e.g. Galarian Yamask evolving into Runerigus rather than Cofagrigus), or remove evolution paths (e.g. Spiky-Eared Pichu cannot evolve, which means it evolves using the evolution method "None"; the species it mentions that it evolves into is irrelevant).

### Exclusive

In addition to the above, there are also some properties exclusive to alternate forms which can also be defined. These properties are mostly relevant to Mega Evolution forms.

**MegaStone:**
The ID of an item which needs to be held to allow the holder to Mega Evolve into this form.
These items cannot be dropped or otherwise lost in battle if held by a Pokémon that can make use of them.

**MegaMove:**
The ID of a move which needs to be known by a Pokémon to allow that Pokémon to Mega Evolve into this form. This typically only applies to Rayquaza (whose move is Dragon Ascent).

**MegaMessage:**
A number which indicates the message that is shown when a Pokémon is Mega Evolving into this form. The messages themselves are hardcoded in def pbMegaEvolve in the script section Battle_Action_Other. If undefined, this is 0. This typically only applies to Rayquaza (which uses message 1).
0 = "{Pokémon}'s {Mega Stone} is reacting to {Player}'s {Mega Ring}!"
1 = "{Player}'s fervent wish has reached {Pokémon}!"

**UnmegaForm:**
A Pokémon of this Mega Evolved form reverts to its unmega form at the end of battle. If undefined, this is 0.

**PokedexForm:**
Used instead of the "FormName" property. When a Pokémon of this form is being registered as seen in the Pokédex, the form number given by this property is what will be registered instead of this Pokémon's actual form. This only applies if this property is greater than 0. If undefined, this is 0.
This is used by duplicate forms which are needed to make other code work. For example, Zygarde has two "Complete Forme" forms defined, because it can turn into Complete Form from two other forms and needs to remember which of those forms (10% and 50%) it originally was. Having two Complete Formes is the most convenient way to remember this. One of those Complete Forms can be registered in the Pokédex, while the other one uses this property to point to the first Complete Form, ensuring that only one Complete Forme can be registered as seen no matter which of the two was actually seen (because they're both treated the same from the player's perspective).


### Forbidden

The following properties cannot be defined for an alternate form, even though they can be defined in "pokemon.txt". The reasons for why they are disabled vary.

**Name:**
The species name is for the species as a whole, not for individual forms.

**🔴 InternalName:**
REMOVED

**🟡 GenderRatio:**
There can be a clash between having a form-specific gender rate and forms which depend on the Pokémon's gender (e.g. Meowstic).

**GrowthRate:**
If a Pokémon's form changes, this property being form-specific will change the Pokémon's level (because the same number of Exp Points corresponds to different levels using different growth rates), which is not desirable.

**Incense:**
Difficulties ensuring that breeding will produce the correct offspring.


### Example
```
[PICHU,2]
FormName = Spiky-Eared
Generation = 4
Evolutions = PIKACHU,None,
#-------------------------------
[UNOWN,16]
FormName = Q
#-------------------------------
[CASTFORM,2]
FormName = Rainy Form
Types = WATER
Color = Blue
Pokedex = This is the form Castform takes when soaked with rain. When its body is compressed, water will seep out as if from a sponge.
```