## List of all the changes to PBS files from v15 to v19.1


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

