## 🟡 moves.txt

Information pulled from the new wiki:
12 June 2022 - https://essentialsdocs.fandom.com/wiki/Defining_a_move
https://essentialsdocs.fandom.com/wiki/Defining_a_move?oldid=1358


The PBS file "moves.txt" lists all the defined moves in the game. Each section in this file is one separate move, where a section begins with a line containing an ID in square brackets and ends when the next section begins. Each line in a section is one separate piece of information about that move.

🟡 Aside from the ID line, every line in a section follows the format:

```
XXX = YYY
```

where XXX is a property and YYY is the value or values associated with it (the spaces are optional).

**[ID]**:
This is how the scripts refer to the move. Each move must have a different ID. Typically this is the same as the move name, but written in all capital letters and with no spaces or special characters. In the scripts, the ID is used as a symbol (i.e. with a colon in front of it, e.g. :TACKLE). The ID is never seen by the player.
This line must come first in a section, because, as mentioned above, this line defines when a new section begins

**Name:**
The name of the move, as seen by the player.

**🔴 Display name:**
REMOVED

**Type:**
The ID of the move's elemental type.

**Category:**
Is one of the following:
- Physical
- Special
- Status

**Base damage:**
The move's base power value. Moves with a variable base power are defined here with a base power of 1. For multi-hit moves, this is the base power of a single hit. Status moves do not need this line, as their base power is 0 which is the default value.

**Accuracy:**
The move's accuracy, as a percentage. An accuracy of 0 means the move doesn't perform an accuracy check (i.e. it will always hit, barring effects like semi-invulnerability).

**TotalPP:**
The maximum amount of PP this move can have, not counting modifiers such as the item PP Up. If the total PP is 0, the move can be used infinitely.

**Target:**
The Pokémon that the move will strike. Is one of the following:
- None - For Bide, Counter, Metal Burst, Mirror Coat.
- User
- NearAlly - For Aromatic Mist, Helping Hand, Hold Hands.
- UserOrNearAlly - For Acupressure.
- AllAllies - For Coaching.
- UserAndAllies - For Aromatherapy, Gear Up, Heal Bell, Life Dew, Magnetic Flux, Howl (in Gen 8+).
- NearFoe - For Me First.
- RandomNearFor - For Petal Dance, Outrage, Struggle, Thrash, Uproar.
- AllNearFoes
- Foe - For throwing a Poké Ball.
- AllFoes - Unused by default.
- NearOther
- AllNearOthers
- Other - For most Flying-type moves and pulse moves.
- AllBattlers - For Flower Shield, Perish Song, Rototiller, Teatime.
- UserSide - Affects the side itself rather than any Pokémon.
- FoeSide - Affects the side itself rather than any Pokémon. For entry hazards.
- BothSides - Affects the battle as a whole rather than any Pokémon. For weather, etc.

The word "near" means the move will be unable to target a Pokémon that is not near to the user (e.g. when they are at opposite ends in a triple battle).

**Priority:**
The move's priority, between -6 and 6 inclusive. This is usually 0. A higher priority move will be used before all moves of lower priority, regardless of Speed calculations. Moves with equal priority will be used depending on which move user is faster.
For example, Quick Attack has a priority of 1.

**Function code:**
The move's function code. This is a string of text. Each function code represents a different effect (e.g. poisons the target). A move can only have one function code.

**Flags:**
A comma-separated list of labels applied to the move which can be used to make it behave differently. The existing flags are:
- Contact - The move makes physical contact with the target.
- CanProtect - The target can use Protect or Detect to protect itself from the move.
- CanMirrorMove - The move can be copied by Mirror Move.
- ThawsUser - If the user is frozen, the move will thaw it out before it is used.
- HighCriticalHitRate - The move has a high critical hit rate.
- Biting - The move is a biting move (powered up by the ability Strong Jaw).
- Punching - The move is a punching move (powered up by the ability Iron Fist).
- Sound - The move is a sound-based move.
- Powder - The move is a powder-based move (Grass-type Pokémon are immune to them).
- Pulse - The move is a pulse-based move (powered up by the ability Mega Launcher).
- Bomb - The move is a bomb-based move (resisted by the ability Bulletproof).
- Dance - The move is a dance move (repeated by the ability Dancer).
- CannnotMetronome - This move cannot be used by the move Metronome. Used for signature moves that are intended to remain exclusive to their associated Pokémon.

There are no flags for whether a move can be redirected by Magic Coat, stolen by Snatch, or can have a chance to cause flinching when the user holds King's Rock/Razor Fang. This is because these effects are related directly to compatible move effects and are hardcoded to them.

**EffectChance:**
The probability that the move's additional effect occurs, as a percentage. If the move has no additional effect (e.g. all status moves), this value is 0.
Note that some moves have an additional effect chance of 100 (e.g. Acid Spray), which is not the same thing as having an effect that will always occur. Abilities like Sheer Force and Shield Dust only affect additional effects, not regular effects.

**Description:**
The move's description.

### Example
```
[FLAMETHROWER]
Name = Flamethrower
Type = FIRE
Category = Special
BaseDamage = 90
Accuracy = 100
TotalPP = 15
Target = NearOther
FunctionCode = BurnTarget
Flags = CanProtect,CanMirrorMove
EffectChance = 10
Description = The target is scorched with an intense blast of fire. It may also leave the target with a burn.
#-------------------------------
[TAILWHIP]
Name = Tail Whip
Type = NORMAL
Category = Status
Accuracy = 100
TotalPP = 30
Target = AllNearFoes
FunctionCode = LowerTargetDefense1
Flags = CanProtect,CanMirrorMove
Description = The user wags its tail cutely, making opposing Pokémon less wary and lowering their Defense stat.
```
