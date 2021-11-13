## townmap.txt

Information pulled from the old wiki on the way back machine:  
September 28th 2015 - http://pokemonessentials.wikia.com/wiki/Region_map  
https://web.archive.org/web/20150601025650/http://pokemonessentials.wikia.com/wiki/Region_map

**[Region number]**  
Region number, comes first in a section

**Current Position:**  
The coordinates of the point on the region map. Every point must have these coordinates. This is filled in automatically when you click a part of the map in "townmapgen.html".
You cannot have more than one line in the same region with the same coordinates.

**Name:**  
The location's name (e.g. Route 101, Rustboro City, Mt. Moon).
Several squares can have the same name (e.g. you can give both squares of a large city that takes up 2 squares the same name).

**Point of Interest	:**  
The name of a particular building or cave or other feature within that location (e.g. Pokémon Tower, Desert, Safari Zone). You should only have one Point of Interest per square. A game will typically only have a few Points of Interest at all.

**Fly Destination:**  
This is a Fly destination, and is three comma-separated numbers: the map ID followed by X and Y coordinates of the location Fly will take you to when you choose this square to Fly to. This location is usually just in front of a Poké Center building, hence its old name "Healing Spot".

**Switch:**  
If this is a number, then the Global Switch of that number must be ON in order to show the square's information. That is, the map's name and Point of Interest will not be shown unless that switch is ON. This only affects non-wall maps.
Multiple squares can depend on the same Global Switch.

Typically used for special locations outside of the storyline. Note that only the name and point of interest are not displayed; you can still Fly there (if "Fly Destination" is defined). However, as you can only Fly to maps you have already visited, this shouldn't usually matter as you should set this Global Switch ON at the same time as visiting the map.

### Example
```
[0]
Name=Essen Region
Filename=mapRegion0.png
Point=13,12,"Lappet Town","Oak's Lab",2,8,8,
Point=13,11,"Route 1",,,,,
Point=13,10,"Cedolan City","Cedolan Dept. Store",7,47,11,
Point=14,10,"Cedolan City",,7,47,11,
Point=14,9,"Route 2",,,,,
Point=14,8,"Route 2",,,,,
Point=15,8,"Lerucean Town",,23,11,15,

The first point defined has a location name, a Point of Interest, and is a Fly destination - when choosing to Fly to this square, the player will move to map number 2, at coordinates (8,8).

Note that all the commas must be there in each line, even if there is no information for them to separate.
```