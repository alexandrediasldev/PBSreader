## 🟢 map_metadata.txt


Information pulled from the new wiki:
23 May 2022 - https://essentialsdocs.fandom.com/wiki/Map_metadata
https://essentialsdocs.fandom.com/wiki/Map_metadata?oldid=1230

The PBS file "map_metadata.txt" contains all the map metadata defined in the game. Each section in this file is one separate map's metadata, where a section begins with a line containing an ID number in square brackets and ends when the next section begins. Each line in a section is one separate piece of metadata for that map.
Aside from the ID number line, every line in a section follows the format:
```
XXX = YYY
```

where XXX is a property and YYY is the value or values associated with it (the spaces are optional). For example:



**🟢 Name:**
The name of the map, as seen by the player. If undefined, the RPG Maker map's name will be taken and added here.
This allows an RPG Maker map's name to be more identifiable to the developer while not affecting its name as shown in-game.

**MapPosition:**
The position on the region map where this map is located. This metadata consists of three comma-separated numbers that indicate the region number and this map's X and Y coordinates on that region map.
When standing in this map and looking at the Town Map, the player's head icon will be placed on this point to show their current location. Note that this is (pretty much) the only purpose of this setting - it does not name the point or make it a Fly destination - see the page Region map for those features.

For large maps, this should be the top left square of the map (even if that particular square isn't part of the map).

**MapSize:**
The size and shape of this map in region map squares. This metadata consists of two comma-separated numbers:
1. The width of the map, in squares. This can be 1.
2. A string of 1s and 0s, which describe the shape of the map. It is more easily visualised by breaking it up into chunks with "width" number of digits each; each successive chunk comes underneath the previous chunk. A 1 represents a square that is part of the map, and a 0 represents a square that isn't. The numbers are not comma-separated in any way.
For example, if the width of the map is 2, and the layout is "1011", then the map is a 2x2 L-shaped map with the gap in the top right corner.

Maps with this metadata calculate the relative position of the player on that map, and show the player's head icon in the appropriate place depending on this position.

**Outdoor:**
If this is TRUE, this map is an outdoor map. If this is FALSE (or this line doesn't exist), this map is an indoor map. Only outdoor maps will have day/night tinting. The hidden move Fly can only be used on an outdoor map.

**Weather:**
The weather in effect on this map, and the likelihood of it. This setting consists of two fields: the weather type and the probability (out of 100) of that weather occurring when the player enters this map. The possible weather types are as follows:
- Rain
- HeavyRain
- Storm
- Snow
- Blizzard
- Sandstorm
- Sun
- Fog
It is not recommended to have a probability of less than 100, because it is used whenever the player enters this map. The player could quickly step between this map and another one until randomness makes the weather appear/not appear (whichever the player prefers).

**ShowArea:**
If this is TRUE, a location signpost stating the map's name will be displayed at the top left of the screen when it is entered. If this is FALSE (or this line doesn't exist), it won't.
Typically, this metadata should only be TRUE for outdoor maps and other important areas (e.g. some caves).

There are some cases where a location signpost will not be displayed even if this metadata says it should. See the page Map transfers for more details.

**Bicycle:**
If this is TRUE, the bicycle can be used on this map. If this is FALSE, it cannot. If this line doesn't exist, then the player will only be able to ride a bicycle if this map is an outdoor map.
Note that caves are not outdoor maps, and therefore cave maps must have this metadata (set to TRUE) in order to allow the player to cycle in caves. This can also apply to gatehouses.

**BicycleAlways	:**
If this is TRUE, the player will automatically mount their bicycle upon entering this map, and they cannot dismount it (not even to fish or surf) while on this map.
Note that the player will mount a bicycle upon entering this map even if they don't own one. Checks should be made before the player can enter one of these maps, to allow them through only if they own a bicycle.

**HealingSpot:**
This is a set of three comma-separated numbers: a map ID number followed by the X and Y coordinates of a particular tile in that map.
When a map with this metadata is entered (e.g. the interior of a Poké Center), the Teleport destination is changed to the spot described by this metadata. Note that the spot itself is not usually on the same map as the one that has this metadata set; the spot is the tile just in front of the entrance to this map (e.g. just in front of a Poké Center's entrance).

Note that the only thing this metadata affects is the Teleport destination. It does not determine Fly destinations (those are set on the region map in the PBS file "town_map.txt"), nor does it determine where the player goes to after blacking out (this is either set by the script pbSetPokemonCenter which is part of the Poké Center nurse event, or the "Home" |global metadata).

**DiveMap:**
The underwater layer of this map. This metadata defines the map ID of the underwater map related to this map, and is required if this map contains accessible patches of deep water (tiles with terrain tag 5) where the move Dive can be used.
Multiple maps cannot refer to the same underwater map, as the game wouldn't know which map to return the player to when surfacing.


**DarkMap:**
If this is TRUE, this map is enshrouded in darkness and a small circle of light will appear around the player. If this is FALSE (or this line doesn't exist), there is no darkness. The player can use the move Flash to illuminate the surroundings, and can only use Flash on dark maps (if it has not already been used).

**SafariMap:**
If this is TRUE, this map is part of the Safari Zone.
Walking in a map that is part of the Safari Zone will decrease the player's Safari Zone step count. Wild Pokémon battles that occur in these maps will be Safari encounters (i.e. the player doesn't use Pokémon, but instead throws bait/rocks, and the wild Pokémon either stays or flees, etc.).

**Dungeon:**
If this is TRUE, this map is a randomly generated dungeon map which changes layout each time the player enters it. This map should not be connected to any other map.

**SnapEdges:**
If this is TRUE, then the screen cannot scroll past the edges of the map. This avoids showing the black borders beyond the edges of maps, but the camera will not be centred on the player if they are close to the edges.
This metadata does not work well with connected maps. Pokémon games usually don't have maps that snap to their edges.

**BattleBack:**
The backdrop picture used for all battles that take place on this map. This setting is a word or phrase which corresponds to a particular backdrop; see the page Backgrounds and music for more information.

**Environment:**
The environment in effect on this map, which affects the environment in battles. The possible environment types are as follows:
- None
- Grass
- TallGrass
- MovingWater
- StillWater
- Puddle
- Underwater
- Cave
- Rock
- Sand
- Forest
- ForestGrass
- Snow
- Ice
- Volcano
- Graveyard
- Sky
- Space
- UltraSpace
The default depends on the terrain tag of the tile that a battle takes place on, and is "None" if no other effects apply.

**WildBattleBGM:**
The music played during any wild battles that take place on this map. See the page Backgrounds and music for more information.

**🟡 WildVictoryBGM:**
The music played when the player wins a wild Pokémon battle that takes place on this map. See the page Backgrounds and music for more information.

**TrainerBattleBGM:**
The music played during any trainer battle that takes place on this map. See the page Backgrounds and music for more information.

**🟡 TrainerVictoryBGM:**
The music played when the player wins a trainer Pokémon battle that takes place on this map. See the page Backgrounds and music for more information.

**WildCaptureME:**
The music played when the player captures a Pokémon in a wild Pokémon battle that takes place on this map. See the page Backgrounds and music for more information.

**🟢 Flags:**
Comma-separated labels applied to the map which can be used to make it behave differently. The existing flags are:
- DisableBoxLink - Access to the Box Link system is disabled in this map.
- MossRock - This map has a mossy rock in it. Used by some species with the evolution method LocationFlag.
- IceRock - This map has an icy rock in it. Used by some species with the evolution method LocationFlag.
- Magnetic - This map has a magnetic field in it. Used by some species with the evolution method LocationFlag.
- DistortionWorld - This map is part of the Distortion World. Giratina appears in Origin Forme in this map.

### Example

```
[002]   # Lappet Town
Name = Lappet Town
Outdoor = true
ShowArea = true
MapPosition = 0,13,12
BattleBack = field
#-------------------------------
[008]   # Daisy's house
Name = Lappet Town
MapPosition = 0,13,12
#-------------------------------
[028]   # Natural Park
Name = Natural Park
Outdoor = true
ShowArea = true
Weather = Rain,100
MapPosition = 0,16,8
BattleBack = field
Flags = MossRock
```