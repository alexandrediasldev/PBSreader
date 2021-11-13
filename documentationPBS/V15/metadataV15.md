## metadata.txt


Information pulled from the old wiki on the way back machine:  
September 28th 2015 - http://pokemonessentials.wikia.com/wiki/Metadata
https://web.archive.org/web/20150928191301/http://pokemonessentials.wikia.com/wiki/Metadata

### Global metadata

**PlayerA ,PlayerB ,PlayerC ,PlayerD ,PlayerE ,PlayerF ,PlayerG ,PlayerH:**  

Information on the player characters in the game. The "PlayerA" line is required, and the other seven are optional. This setting consists of a number of comma-separated fields, as follows:
1. The player's trainer type. This is the internal name of a trainer type, as defined in the PBS file "trainertypes.txt". This trainer type is defined in exactly the same way as any other trainer type, and is typically only used by this player character (although some games may turn an unused player character into a rival instead).
2. The character's walking charset, as found in "Graphics/Characters".
3. The character's cycling charset, as found in "Graphics/Characters".
4. The character's surfing charset, as found in "Graphics/Characters".
5. The character's running charset, as found in "Graphics/Characters".
6. The character's diving charset, as found in "Graphics/Characters".
7. The character's fishing-while-standing charset, as found in "Graphics/Characters".
8. The character's fishing-while-surfing charset, as found in "Graphics/Characters".
Typically, "PlayerA" will correspond to the male player character, and "PlayerB" the female one. The charsets mentioned should depict the "default" outfit for that player character, i.e. they have no outfit ID number at the end of their filenames.

If a charset includes the word "offset", then it will be shifted 1 tile south when being displayed. This is useful for any charset which extends below the tile the player is currently on (such as fishing).

It is possible to modify the scripts to allow for more than eight player options, but this requires some scripting knowledge.

**Home:**  

The point that the player is transferred to when they black out but no Poké Center has been visited yet. This line consists of four comma-separated numbers in the following order:
1. Map ID.
2. X coordinate on that map.
3. Y coordinate on that map.
4. Direction the player should face (2=down, 4=left, 6=right, 8=up, 0=retain direction).
The map identified by this metadata must have an event page with the "Autorun" trigger, which depends on the Global Switch called "Starting Over" (number 1 by default). This event page, when run, must heal all Pokémon in the player's party (use the event command "Recover All: Entire Party" for this), and then turn that Global Switch OFF again.

This metadata is required.

**BicycleBGM:**  
The background music that plays while the player is cycling.

**SurfBGM:**  
The background music that plays while the player is surfing.

**WildBattleBGM:**  
The default music that plays during wild Pokémon battles. It should be placed in the "Audio/BGM" directory.

**TrainerBattleBGM:**  
The default music that plays during trainer battles. It should be placed in the "Audio/BGM" directory.

**WildVictoryME:**  
The default victory music that plays at the end of a won wild Pokémon battle. It should be placed in the "Audio/ME" directory.

**TrainerVictoryME:**  
The default victory music that plays at the end of a won Trainer battle. It should be placed in the "Audio/ME" directory.

### Example

```
[000]
PlayerA=POKEMONTRAINER_Red,trchar000,boy_bike,boy_surf_offset,boy_run,boy_dive_offset,boy_fish_offset,boy_fishsurf_offset
PlayerB=POKEMONTRAINER_Leaf,trchar001,girl_bike,girl_surf_offset,girl_run,girl_dive_offset,girl_fish_offset,girl_fishsurf_offset
Home=3,7,5,8
BicycleBGM=Airship.mid
SurfBGM=Ship.mid
WildBattleBGM=002-Battle02.mid
TrainerBattleBGM=005-Boss01.mid
```
### Map-specific metadata

**Outdoor:**  
If this is TRUE, this map is an outdoor map. If this is FALSE (or this line doesn't exist), this map is an indoor map. Only outdoor maps will have day/night tinting. The hidden move Fly can only be used on an outdoor map.

**Bicycle:**  
If this is TRUE, the bicycle can be used on this map. If this is FALSE, it cannot. If this line doesn't exist, then the player will only be able to ride a bicycle if this map is an outdoor map.
Note that caves are not outdoor maps, and therefore cave maps must have this metadata (set to TRUE) in order to allow the player to cycle in caves. This can also apply to gatehouses.

**BicycleAlways	:**  
If this is TRUE, the player will automatically mount their bicycle upon entering this map, and they cannot dismount it (not even to fish or surf) while on this map.
Note that the player will mount a bicycle upon entering this map even if they don't own one. Checks should be made before the player can enter one of these maps, to allow them through only if they own a bicycle.

**HealingSpot:**  
This is a set of three comma-separated numbers: a map ID number followed by the X and Y coordinates of a particular tile in that map.
When a map with this metadata is entered (e.g. the interior of a Poké Center), the Teleport destination is changed to the spot described by this metadata. The Teleport destination itself is not usually the same map as the one that has this metadata set; the destination will be the tile just in front of the entrance to this map (e.g. just in front of a Poké Center's entrance).

Note that the only thing this metadata affects is the Teleport destination. It does not determine Fly destinations (those are set on the region map), nor does it determine where the player goes to after blacking out (this is either set by the script Kernel.pbSetPokemonCenter which is part of the Poké Center nurse event, or the "Home" global metadata mentioned above).

**MapPosition:**  
The position on the region map where this map is located. This metadata consists of three comma-separated numbers that indicate the region number and this map's X and Y coordinates on that region map.
When standing in this map and looking at the Town Map, the player's head icon will be placed on this point to show their current location. Note that this is (pretty much) the only purpose of this setting - it does not name the point or make it a Fly destination - see the article Region map for those features.

For large maps, this should be the top left square of the map (even if that particular square isn't part of the map).

**MapSize:**  
The size and shape of this map in region map squares. This metadata consists of two comma-separated numbers that indicate the overall width and the layout of the map. The width can be 1. The overall height is calculated from these two numbers.
The layout is a string of 1s and 0s, where 1 represents a square which is part of the map and 0 is a square which isn't. For example, if the width of the map is 2, and the layout is "1011", then the map is a 2x2 L-shaped map with the gap in the top right corner. The layout should not be comma-separated.

Maps with this metadata calculate the relative position of the player on that map, and show the player's head icon in the appropriate place depending on this position.

**ShowArea:**  
If this is TRUE, a location signpost stating the map's name will be displayed at the top left of the screen when it is entered. If this is FALSE (or this line doesn't exist), it won't.
Typically, this metadata should only be TRUE for outdoor maps and other important areas (e.g. some caves).

There are some cases where a location signpost will not be displayed even if this metadata says it should. See the article Map transfers for more details.

**Weather:**  
The weather in effect on this map, and the likelihood of it. This setting consists of two fields: the weather type and the probability (out of 100). The possible weather types are as follows:
- Rain
- Storm
- Snow
- Sandstorm
- Sunny

**DarkMap:**  
If this is TRUE, this map is enshrouded in darkness and a small circle of light will appear around the player. If this is FALSE (or this line doesn't exist), there is no darkness. The player can use the move Flash to illuminate the surroundings, and can only use Flash on dark maps (if it has not already been used).

**DiveMap:**  
The underwater layer of this map. This metadata defines the map ID of the underwater map related to this map, and is required if this map contains accessible patches of deep water (tiles with terrain tag 5) where the move Dive can be used.
Multiple maps cannot refer to the same underwater map.

**SafariMap:**  
If this is TRUE, this map is part of the Safari Zone.
Walking in a map that is part of the Safari Zone will decrease the player's Safari Zone step count. Wild Pokémon battles that occur in these maps will be Safari encounters (i.e. the player doesn't use Pokémon, but instead throws bait/rocks, and the wild Pokémon either stays or flees, etc.)

**SnapEdges:**  
If this is TRUE, then the screen cannot scroll past the edges of the map. This avoids showing the black borders beyond the edges of maps, but the camera will not be centred on the player if they are close to the edges.

**Dungeon:**  
If this is TRUE, this map is a randomly generated dungeon map which changes layout each time the player enters it. This map should not be connected to any other map.

**BattleBack:**  
The backdrop picture used for all battles that take place on this map. This setting is a phrase which corresponds to a particular backdrop; see the article Backgrounds and music for more information.

**WildBattleBGM:**  
The music played during any wild battles that take place on this map. See the article Backgrounds and music for more information.

**TrainerBattleBGM:**  
The music played during any trainer battle that takes place on this map. See the article Backgrounds and music for more information.

**WildVictoryME:**  
The music played when the player wins a wild Pokémon battle that takes place on this map. See the article Backgrounds and music for more information.

**TrainerVictoryME:**  
The music played when the player wins a trainer Pokémon battle that takes place on this map. See the article Backgrounds and music for more information.

### Example

```
[004]
Outdoor=true
Bicycle=true
MapPosition=0,6,4
ShowArea=true
Weather=Rain,100
```