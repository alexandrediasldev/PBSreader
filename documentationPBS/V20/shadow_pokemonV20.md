## shadowmoves.txt
#TODO
Information pulled from the old wiki on the way back machine:
September 28th 2015 - http://pokemonessentials.wikia.com/wiki/Shadow_Pok%C3%A9mon
https://web.archive.org/web/20150928235526/http://pokemonessentials.wikia.com/wiki/Shadow_Pok%C3%A9mon

To define which Shadow moves a Shadow Pokémon of each species can know, edit the PBS file "shadowmoves.txt" to include lines such as:

### Example
```
TEDDIURSA=SHADOWBLITZ,SHADOWMIST
FARFETCHD=SHADOWBREAK,SHADOWSKY,SHADOWPANIC
LUGIA=SHADOWBLAST,SHADOWSHED,SHADOWDOWN,SHADOWSTORM
```

If a species does not have any Shadow moves defined for it, then its only Shadow move will be Shadow Rush.
When a Shadow Pokémon is generated, it will first be given its initial moveset as normal. Then, starting from the first move, some/all of the initial moves are replaced with the Shadow moves defined for that species. This is its Shadow moveset. All Shadow moves will be available immediately, while the other moves are unlocked while opening that Pokémon's door to the heart.

It is recommended that you specifically define the initial movesets for all Shadow Pokémon (in the PBS file "trainers.txt"), to make sure that the appropriate moves are replaced by Shadow moves.

You don't have to list just Shadow moves in the PBS file "shadowmoves.txt"; you can list any move that exists.