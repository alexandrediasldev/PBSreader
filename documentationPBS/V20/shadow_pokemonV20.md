## 🟡 shadow_pokemons.txt
Information pulled from the new wiki:
11 June 2022 - https://essentialsdocs.fandom.com/wiki/Shadow_Pok%C3%A9mon
https://essentialsdocs.fandom.com/wiki/Shadow_Pok%C3%A9mon?oldid=1325
The PBS file "shadow_pokemon.txt" lists a number of Pokémon species, and each one has a defined Heart Gauge size and a set of moves it will know when it becomes a Shadow Pokémon (i.e. when it is created).

**[Species]:**
The shadow pokemon original species.

**🟢 GaugeSize:**
The default Heart Gauge size is 4000. Stronger Pokémon typically have larger Heart Gauges, which require more work to empty before they can be purified.

**Moves:**
A coma separated list of moves.
If a species is not given one or more moves it will know as a Shadow Pokémon, then it will know the move Shadow Rush. If Shadow Rush is not defined, the Shadow Pokémon of that species will have the usual moves it would know if it was not a Shadow Pokémon.

### Example
```
[BEEDRILL]
GaugeSize = 4500
Moves = SHADOWBLITZ,SHADOWHOLD
#-------------------------------
[EXEGGUTOR]
GaugeSize = 9000
Moves = SHADOWSTORM,SHADOWSHED,SHADOWHOLD,SHADOWEND
#-------------------------------
[SCIZOR]
GaugeSize = 8000
Moves = SHADOWRUSH
```