## connections.txt


Information pulled from the old wiki on the way back machine:  
September 28th 2015 - http://pokemonessentials.wikia.com/wiki/Connecting_maps
https://web.archive.org/web/20150928185640/http://pokemonessentials.wikia.com/wiki/Connecting_maps
Map connections are stored in the PBS file "connections.txt". Each line consists of 6 comma-separated elements, as follows:

1. Map 1's ID number.
2. Map 1's edge (one of N, North, S, South, E, East, W, or West).
3. Map 1's connecting point (a positive integer).
4. Map 2's ID number.
5. Map 2's edge (one of N, North, S, South, E, East, W, or West).
6. Map 2's connecting point (a positive integer).

### Examples
```
Note that you can only connect north to south, and east to west.

24,E,3,25,W,8
This example connects maps 24 and 25. The connection will be east-west, with map 25 on the left and map 24 on the right.

Where the two maps join, the 3rd tile from the top of map 24 will be connected directly to the 8th tile from the top of map 25.

37,N,0,38,S,0
This example connects maps 37 and 38. The connection will be north-south, with map 37 below map 38.

Where the two maps join, the left-most tile of map 24 will be connected directly to the left-most tile of map 25.

Non-bordering connected maps
It is possible to connect two maps together even if they don't have sides that touch. In this case, rather than choosing a side and a distance along that side for each map, you should instead use two coordinates. For example:

24,0,0,25,21,14
The top left corner tile (0,0) of map 24 will be at coordinates (21,14) when compared to map 25 (i.e. map 24 is to the bottom-right of map 25).

These "connections" will not be saved by the Visual Editor. You will need to create them manually in the PBS file "connections.txt", and make sure they remain there even if you use the Visual Editor later.

Uses for this kind of map connection include overlapping maps, maps divided by non-traversable blackness, opposite corners of a large city spanning multiple maps, and so on.
```