
## encounters.txt

Information pulled from the old wiki on the way back machine:  
August 22th 2015 - http://pokemonessentials.wikia.com/wiki/Encounters
https://web.archive.org/web/20150822133755/http://pokemonessentials.wikia.com/wiki/Encounters

**1. Map ID number:**  
The map's ID number. This can be found in the middle of RPG Maker XP's status bar (at the bottom) while the map is open for editing.

**2. Encounter densities:**  
This is a set of three comma-separated numbers, which sets the likelihood of an encounter while walking around in long grass, caves and when surfing respectively. This line is optional, and if it does not exist, the densities are set to "25,10,10". A higher number means a greater chance of an encounter with each step.

**3. Encounter type:**  
An encounter type followed by a list of Pokémon (each on a new line) that can be encountered this way. Possible encounter types are:
- Land - For long grass. Pokémon will appear only while walking in the grass.
- LandDay - Same as "Land", but for encounters between 6am and 8pm. If defined, overrides the "Land" encounter type during that time.
- LandNight - Same as "Land", but for encounters between 8pm and 6am. If defined, overrides the "Land" encounter type during that time.
- LandMorning - Same as "Land", but for encounters between 6am and noon. If defined, overrides the "Land" and "LandDay" encounter types during that time.
- BugContest - Same as "Land", but for when the player is in a Bug Catching Contest. If undefined, "Land" is used instead.
- Cave - For caves and other maps where wild encounters can occur anywhere, as long as the player is walking.
- Water - For surfing.
- RockSmash - For when the player smashes a breakable rock.
- OldRod - For when the player uses the Old Rod.
- GoodRod - For when the player uses the Good Rod.
- SuperRod - For when the player uses the Super Rod.
- HeadbuttLow - For when Headbutt is used on a tree. These Pokémon are rare to find in a Headbutt encounter.
- HeadbuttHigh - For when Headbutt is used on a tree. These Pokémon are common to find in a Headbutt encounter.

**Pokémon to encounter:**  
This is a list of the Pokémon associated with that encounter type. Each line in the list contains two or three comma-separated elements:
1. A Pokémon species.
2. A level.
3. A second level. Optional. Must be higher than the first level.
If the second level is defined, the two numbers define a range of levels that the species can be found at (inclusive). If that line is chosen for the wild encounter, then there is an equal chance of the wild Pokémon being any of those levels.

The position of a species within the list determines the rarity of that species (higher up means more common). The list must contain a specific number of lines, depending on the encounter type. See the table below for the encounter probabilities and list lengths for each encounter type.

### Probabilty of encounter
Type: Land, LandMorning, LandDay, LandNight, Cave, BugContest  
Number of entries: 12  
Probability of encounter: 20, 20, 10, 10, 10, 10, 5, 5, 4, 4, 1, 1  

Type: Water, Rocksmash  
Number of entries: 5  
Probability of encounter: 60, 30, 5, 4, 1  

Type: OldRod  
Number of entries: 2  
Probability of encounter: 70, 30  

Type: GoodRod  
Number of entries: 3  
Probability of encounter: 60, 20, 20  

Type: SuperRod  
Number of entries: 5  
Probability of encounter: 40, 40, 15, 4, 1  

Type: HeadbuttLow, HeadbuttHigh  
Number of entries: 8    
Probability of encounter: 30, 25, 20, 10, 5, 5, 4, 1  

### Examples
```
019
25,10,10
Land
SENTRET,12,15
PIDGEY,12,15
RATTATA,12
RATTATA,12
RATTATA,13
RATTATA,13
RATTATA,14
RATTATA,14
RATTATA,15
RATTATA,15
RATTATA,16
RATTATA,17

This example sets the encounters for map number 019. The probability of an encounter in tall grass is 2.5 times higher than an encounter while surfing or walking in a cave (although the cave probability is ignored here because this map has Land encounters and therefore cannot have Cave encounters).
There is one encounter type (Land), and the listed Pokémon (Sentret, Pidgey and Rattata) can be encountered at the given levels.
The chances of encountering a Pokémon are as follows:

Sentret - 20%
Pidgey - 20%
Rattata - 60%

The chances of encountering a Pokémon at a given level are more complicated, as this chance includes not only the probability of choosing the line(s) naming that species, but also the probability of choosing a particular level in the ranges given.
For example, there are four possible levels Sentret can have (12, 13, 14 or 15), and the 20% chance of choosing a Sentret for the encounter is divided evenly between each of these possible levels (i.e. 5% chance of encountering a level 12 Sentret).

These probabilities can easily become very complicated.

011
25,10,10
Land
PIDGEY,16
PARAS,16
PARAS,16
RATTATA,17
RATTATA,18
PIDGEY,17
RATTATA,19
RATTATA,18
PIDGEY,19
RATTATA,18
PIDGEY,20
RATTATA,20
Water
MAGIKARP,2
GOLDEEN,3
POLIWAG,3
FEEBAS,3
FEEBAS,3
OldRod
MAGIKARP,2
GOLDEEN,3
GoodRod
MAGIKARP,2
GOLDEEN,3
POLIWAG,3
SuperRod
MAGIKARP,2
GOLDEEN,3
POLIWAG,3
FEEBAS,3
FEEBAS,3
```



