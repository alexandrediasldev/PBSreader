## 🟡 metadata.txt

Information pulled from the new wiki:
23 May 2022 - https://essentialsdocs.fandom.com/wiki/Metadata
https://essentialsdocs.fandom.com/wiki/Metadata?oldid=1231

The PBS file "metadata.txt" contains various information used throughout the game (global metadata), as well as information about the defined player characters.
Each section in this file is either the global metadata or one separate player character, where a section begins with a line containing a number in square brackets and ends when the next section begins. Each line in a section is one separate piece of metadata.
Aside from the square bracketed number line, every line in a section follows the format:
```
XXX = YYY
```

where XXX is a property and YYY is the value or values associated with it (the spaces are optional).

### Global metadata

The first section of the PBS file "metadata.txt" begins with [0], and contains various general information about the game.

**🔴 PlayerA ,PlayerB ,PlayerC ,PlayerD ,PlayerE ,PlayerF ,PlayerG ,PlayerH:**
REMOVED

**🟢 StartMoney:**
The amount of money that the player starts the game with. If undefined, this is 3000.

**🟢 StartItemStorage:**
A comma-separated set of IDs of items that are in the player's PC at the start of the game. If undefined, there are no items there.

**Home:**
The point that the player is transferred to when they black out but no Poké Center has been visited yet. This line consists of four comma-separated numbers in the following order:
1. Map ID
2. X coordinate on that map
3. Y coordinate on that map
4. Direction the player should face (2=down, 4=left, 6=right, 8=up, 0=retain direction)
The map identified by this metadata must have an event page with the "Autorun" trigger, which depends on the Game Switch called "Starting Over" (number 1 by default). This event page, when run, must heal all Pokémon in the player's party (use the event command "Recover All: Entire Party" for this), and then turn that Game Switch OFF again.

This metadata is required.

**StorageCreator:**
The name of the person that created the Pokémon storage system. The storage system will be called "Someone's PC" until the player has met this person, and afterwards it will be called "<name>'s PC".

**WildBattleBGM:**
The default music that plays during wild Pokémon battles. It should be placed in the "Audio/BGM" directory.

**TrainerBattleBGM:**
The default music that plays during trainer battles. It should be placed in the "Audio/BGM" directory.

**🟡 WildVictoryBGM:**
The default victory music that plays at the end of a won wild Pokémon battle. It should be placed in the "Audio/ME" directory.

**🟡 TrainerVictoryBGM:**
The default victory music that plays at the end of a won Trainer battle. It should be placed in the "Audio/ME" directory.

**WildCaptureME:**
The default capture music that plays at the end of a captured Pokémon battle. It should be placed in the "Audio/ME" directory.

**SurfBGM:**
The background music that plays while the player is surfing.

**BicycleBGM:**
The background music that plays while the player is cycling.


### Example

```
[0]
StartMoney = 3000
StartItemStorage = POTION
Home = 3,7,5,8
StorageCreator = Bill
WildBattleBGM = Battle wild
TrainerBattleBGM = Battle trainer
WildVictoryBGM = Battle victory wild
TrainerVictoryBGM = Battle victory trainer
SurfBGM = Surfing
BicycleBGM = Bicycle
```

### 🟢 Player characters
All other sections of the PBS file "metadata.txt" begins with [1], [2] and so on. Each of these sections defines a player character, whose character ID is the number in that section's square brackets.

**TrainerType:**
The ID of this player character's trainer type. This trainer type is defined in exactly the same way as any other trainer type, and is typically only used by this player character (although some games may turn an unused player character into a rival instead).

**WalkCharset:**
This player character's walking charset, as found in "Graphics/Characters".

**RunCharset:**
This player character's running charset, as found in "Graphics/Characters". If undefined, the WalkCharset will be used instead when running.

**CycleCharset:**
This player character's cycling charset, as found in "Graphics/Characters". If undefined, the RunCharset will be used instead when cycling.

**SurfCharset:**
This player character's surfing charset, as found in "Graphics/Characters". If undefined, the CycleCharset will be used instead when surfing.

**DiveCharset:**
This player character's diving charset, as found in "Graphics/Characters". If undefined, the SurfCharset will be used instead when diving.

**FishCharset:**
This player character's fishing-while-standing charset, as found in "Graphics/Characters".

**SurfFishCharset:**
This player character's fishing-while-surfing charset, as found in "Graphics/Characters". If undefined, the FishCharset will be used instead when fishing while surfing.

**Home:**
The point that this player character is transferred to when they black out but no Poké Center has been visited yet. If defined, this overrides the "Home" global metadata defined above if the player is this character. It is defined in the same way as the "Home" global metadata.

### Example

```
[1]
TrainerType = POKEMONTRAINER_Red
WalkCharset = trainer_POKEMONTRAINER_Red
RunCharset = boy_run
CycleCharset = boy_bike
SurfCharset = boy_surf
FishCharset = boy_fish_offset
```
### 🔴 Map-specific metadata
MOVED TO "map_metadata.txt"
