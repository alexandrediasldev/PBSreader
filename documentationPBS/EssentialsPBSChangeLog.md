## List of all the changes to PBS files from v15 to v20

## v20

### File structure

- Renamed various PBS files.
- Removed support for the PBS file tm.txt.
- Added "Flags" properties to abilities, map metadata, ribbons, species, trainer types and types.
- Abilities that hasten egg hatching now have a flag in abilities.txt for this effect.
- Removed support for old encounters.txt format.
- Added PBS file pokemon_metrics.txt, for all Pokémon sprite positionings. Can be distributed with sprite pack resources.
- Added new section-based format for ribbons.txt, trainer_types.txt, moves.txt, items.txt, berry_plants.txt.
- Added new section-based format for shadow_pokemon.txt, which can now also define heart gauge sizes and flags.

#### items.txt:
- Added separate "SellPrice" property for items.
- Added "Consumable" property to items.txt.
- An item can now have any number of flags, rather than just one.


#### metadata.txt:
- Split metadata.txt into metadata.txt and map_metadata.txt. Player character data is now in separate sections in metadata.txt, one per character, and you can now have as many characters as you like. NOTE: If you're using old PBS files, you will need to make these changes manually (move map metadata sections into map_metadata.txt without changing them, and move player character metadata into their own sections). Also, calls to pbChangePlayer will need to have their numbers increased by 1.
- Added "Name" property to map_metadata.txt, which is the display name in-game.
- Added map metadata flag "HideEncountersInPokedex" which will make the Pokédex ignore that map’s wild encounters when displaying a Pokémon’s area.


#### pokemon.txt/pokemon_forms.txt:
- Changed the names of some properties in pokemon.txt and pokemon_forms.txt.
- Merged species "Type1"/"Type2" into "Types".
- The "EVs" property's preferred format is now "ATTACK,2,SPEED,1" instead of "0,2,0,1,0,0".
- Allowed the "WildItem" properties for species to contain multiple items each.
- Added pokemon.txt/pokemon_forms.txt property "Offspring" for species that can be produced by breeding instead of itself (although this property can include itself anyway).



### Property changed

#### items.txt:
- Repels now have a flag in items.txt which determines if they can be reused when one runs out.
- Added flags for Fling power and Natural Gift type/power.

#### metadata.txt:
- When rewriting map_metadata.txt via the Debug function, map names will be added if possible and if the map doesn't already have a name in map_metadata.txt.

#### pokemon.txt/pokemon_forms.txt:
- Added species flags that govern form inheritance while breeding, and a flag that sets a particular form by default.
- Renumbered Spiky-Eared Pichu to form 2, so it doesn't clash with Alolan Raichu's form 1.
- The "Shape" property in pokemon.txt must now be a name and not a number.

#### moves.txt:
- Deprecated three move flags (can Magic Coat, can Snatch, affected by King's Rock) as they should depend on move effects instead.
- Turned move flags into separate words rather than letters in a string.
- Added move flag "TramplesMinimize" instead of having that effect be related to function codes.
- Added move flag "CannotMetronome" instead of hardcoding the signature moves Metronome is forbidden to use.

#### trainers.txt:
Removed support for the old trainers.txt format.
The "Ability" property in trainers.txt can now only be an ability ID.
The "Ball" property in trainers.txt can now only be an item ID (specifically an item that is a Poké Ball).
Added Gen 6 PBS files for completeness.

## v19.1/v19

### File structure
#### "tm.txt"
-   Merged into pokemon.txt/pokemonforms.txt as the property "TutorMoves".

#### "pokemon.txt" and "pokemonforms.tx"
-    Removed Regional Dex numbers information
-   Added the "Generation" property, and filled these in.
-    Added "TutorMoves"

#### "regionaldexes.txt"
-   Created PBS file and extracted the Regional Dex numbers information from pokemon.txt/pokemonforms.txt.

#### "ribbons.txt"
-   Created PBS file rather than hardcoding their data.

#### "encounters.txt"
-    Implemented a new format, which allows any number of slots, customised probabilities per slot and encounter type-specific step trigger chances. It also supposed multiple versions of encounter tables for the same map.


### Property changed
#### "moves.txt"
-    Move targets defined in moves.txt can no longer be ID numbers.
#### "items.txt"
-    Added item field use number 6 for TRs, which are one-use TMs.



## v18.1/v18
### File structure
- Created Gen 7 versions of several PBS files, which are provided alongside the Gen 5 versions
-Tweaked the layouts of some PBS files, such as adding header comments and separator lines where appropriate
- Lines in PBS files that are written like "XXX=YYY" will now have spaces put around the "=" when they are modified and saved in-game (all PBS files are now written like this, although no-spaces versions are still usable)
- Made several tweaks and fixes to PBS files to fix values and adjust descriptions to make them fit the spaces they're displayed in


#### "pokemon.txt" and "pokemonforms.txt":
-	Added more sprite positioning metrics, and added support for multiple sizes of Pokémon shadows in battle, as well as species-specific shadows
-	Changed the sprite position editor to work for all metrics
-	Updated Pokémon colours to Gen 7 standards, including differing colours for different forms
-	Added the evolution method LevelEvening
-	Added support for an evolution method's parameter being an ability's internal name
-	Added data for the glowing fused Kyurem forms

#### "pokemonforms.txt":
-	added the new PokedexForm property which is the form that should be registered as seen in the Pokédex instead of this one
-	allowed Compatibility to be a defined property
-	a form can now be defined with an evolution method of "None", which overrides the base form's evolutions but is treated as non-existent (used for spiky-eared Pichu)
-	allowed the sections to be written like [PIKACHU,1] and [PIKACHU 1] as well as [PIKACHU-1]
-	Each form defined in "pokemonforms.txt" is now given its own species internal name in the form of PBSpecies::PIKACHU_1 (most places where you might think of using it are untested)

#### "trainers.txt":
-	Rewrote the trainers.txt compiler and related scripts to add support for another data format
-	Added the ability to set all 6 IVs for a trainer's Pokémon individually, or use a single value for all of them (new trainers.txt format only)
-	Added the ability to edit the EVs of a trainer's Pokémon, with the same functionality as setting IVs (new trainers.txt format only)
-	Added the new LoseText property, which is used if no message is given as an argument in the battle-starting method

#### "metadata.txt":
-	Added a new map-specific metadata: "Environment"
-	Allowed the successful wild Pokémon capture ME to be defined in the metadata (both global and per-map) and to be overridden for the next battle

### Property changed
#### "moves.txt":
-	Added support for move targets to be words (enums) as well as numbers, and renamed those enums
-	Updated moves.txt with new move targets (as enums) to support their usability in triple battles
-	Added more available move flags, all the way to z
-	Move function codes are now strings rather than hexadecimal numbers and can be any length
-	Move base powers can now exceed 255

#### "items.txt":
-	changed various "item usage in battle" numbers

#### "tm.txt" and "encounters.txt":
-	now allow the use of form internal names such as PBSpecies::PIKACHU_1

#### "encounters.txt":
-	Made encounter species lines indented when the game rewrites that file (e.g. after changing the wild encounters via the editor) for legibility


## v17.2/v17.1/v17
### File structure
#### "pokemonforms.txt":
-	Implemented the PBS files for pokemon forms

#### "pokemon.txt":
-	Added shape property

### Property changed
#### "items.txt":
-	Added Item data for whether an item is an evolution stone, gem, mulch or Mega Stone.

## v16.2/v16.1/v16
### File structure
#### "pokemon.txt":
-	Added the Incense property

#### "items.txt":
-	Added item name plurals

#### "trainertypes.txt":
-	Added skillcode

#### "berryplants.txt"
-	Moved berry plant data into their own PBS file.

## v15.1/v15
- Base version of the PBS files this program reads.

-----
Changes are signaled by color
red: removed 🔴
yellow: modified 🟡
green: added 🟢

