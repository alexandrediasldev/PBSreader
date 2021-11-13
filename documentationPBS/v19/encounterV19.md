
## 🟡 encounters.txt

Information pulled from the new wiki:  
9 November 2021 - https://essentialsdocs.fandom.com/wiki/Wild_encounters
https://essentialsdocs.fandom.com/wiki/Wild_encounters?oldid=1115

**🟡 1.**  
**Map ID number:**  
The map's ID number. This can be found in the middle of RPG Maker XP's status bar (at the bottom) while the map is open for editing.

**🟢 Version Number:**  
The version number, optional the default is 0.

**🟡 2.**  
**Encounter method:**  
An encounter method. Possible encounter methods are:

This is a set of three comma-separated numbers, which sets the likelihood of an encounter while walking around in long grass, caves and when surfing respectively. This line is optional, and if it does not exist, the densities are set to "25,10,10". A higher number means a greater chance of an encounter with each step.
- Land - For long grass. Pokémon will appear only while moving in the grass.
- LandDay - Same as "Land", but for encounters between 5am and 8pm. If not defined, the "Land" encounter method is used instead.
- LandNight - Same as "Land", but for encounters between 8pm and 5am. If not defined, the "Land" encounter method is used instead.
- LandMorning - Same as "Land", but for encounters between 5am and 10am. If not defined, the "LandDay" encounter method is used instead.
- BugContest - Same as "Land", but for when the player is in a Bug Catching Contest. If not defined, the "Land" encounter method is used instead.
- Cave - For caves and other maps where wild encounters can occur anywhere, not just on particular tiles. An encounter may occur after each step taken.
- Water - For surfing. An encounter may occur after each step taken.
- RockSmash - For when the player smashes a breakable rock.
- OldRod - For when the player uses the Old Rod.
- GoodRod - For when the player uses the Good Rod.
- SuperRod - For when the player uses the Super Rod.
- HeadbuttLow - For when Headbutt is used on a tree. These Pokémon are rare to find in a Headbutt encounter.
- HeadbuttHigh - For when Headbutt is used on a tree. These Pokémon are common to find in a Headbutt encounter.


**Encounter densities:**  
The likelihood of an encounter for this encounter method. This is optional, A higher number means a greater chance of an encounter with each step. Without modifications, the chance of a wild encounter happening per step taken is the appropriate encounter density divided by 180


**🟡 3. List of Pokémon:**  
This is a list of the Pokémon encounterable via the encounter method stated above. Each line in the list contains two or four comma-separated elements:
1. 🟢 An encounter chance.
2. A Pokémon species.
3. A level.
4. A second level. Optional. Must be higher than the first level.
If the second level is defined, the two numbers define a range of levels (inclusive) that the species can be found at. Each level in that range has an equal chance of being chosen.


### Examples
```
[005,1] # Route 1
Land,21
   40,PIDGEY,15,18
   40,RATTATA,14,18
   10,SENTRET,13,17
   5,PIDGEY,14,16
   5,RATTATA,13,16
LandNight,21
   40,RATTATA,14,18
   30,HOOTHOOT,14,17
   20,SPINARAK,12,16
   10,CLEFAIRY,11,15

This example sets the encounters for map number 5 version 1. The probability of an encounter in Land and LandNight are 21/180 per step.

There is two encounter methods (Land and LandNight).For this example we will focus on Land, that has the listed Pokémon (Sentret, Pidgey and Rattata) that can be encountered at the given levels. The chances of encountering a particular species are as follows:

Pidgey (Lv. 14-18) - 45%
Rattata (Lv. 13-18) - 45%
Sentret (Lv. 13-17) - 20%

Sentret has an equal chance of being at each of the levels in their given ranges, but Rattata and Pidgey do not. Because each of the entries in which Rattata and Pidgey are placed have their own encounter probabilities, the chance of encountering a Rattata and Pidgey at a given level also depends on these entry probabilities. In this case, higher levels of Rattata and Pidgey are more likely to be encountered, because lower levels are in the entries with lower probability.

For a more complete example:



[069] # Route 8
Land,21
   20,MAREEP,16,18
   20,ODDISH,15,17
   13,BONSLY,14,16
   10,DITTO,15,17
   10,DITTO,16,18
   10,LOTAD,15,18
   10,LOTAD,15,17
   5,BONSLY,14,17
   1,BONSLY,15,16
   1,BONSLY,15
Water,2
   60,TENTACOOL,14,19
   30,MANTYKE,15,16
   10,REMORAID,14,16
OldRod
   100,MAGIKARP,16,19
GoodRod
   60,BARBOACH,17,18
   20,KRABBY,15,16
   20,SHELLDER,16,19
SuperRod
   40,CHINCHOU,17,19
   40,QWILFISH,16,19
   15,CORSOLA,15,18
   5,STARYU,15,17
  
This example shows how a map can be defined with multiple encounter methods. The encounter methods here are "Land", "Water", "OldRod", "GoodRod" and "SuperRod" (highlighted).

```



