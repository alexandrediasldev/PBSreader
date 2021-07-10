## moves.txt

Information pulled from the old wiki on the way back machine:  
September 28th 2015 - http://pokemonessentials.wikia.com/wiki/Defining_a_move  
https://web.archive.org/web/20150928235759/http://pokemonessentials.wikia.com/wiki/Defining_a_move


Moves are defined in the PBS file "moves.txt", with each line corresponding to one move. Each line consists of the following comma-separated parts (in order)

### Mandatory
**1. ID Number**:  
Each move's ID number must be different. The ID number must be a whole number greater than 0 (i.e. 1,2,3...), up to 999. Missing numbers are not a problem (e.g. the sequence 23,24,25,58,59,60... is allowed).

**2. Internal name:**  	
Typically written only in capital letters with no spaces or symbols. This is the name the scripts refer to and use. This name is never seen by the player.

**3. Display name:**  	
The actual name of the move. This is only used when displaying the move's name on the screen.

**4. Function code:**  
The move's function code. A function code is a 3-digit hexadecimal number that describes a defined effect (e.g. poisons the opponent).

**5. Base damage:**  	
The base amount of damage the move will inflict on the attack target. Is 0 if it is a status move (i.e. doesn't inflict damage). Is 1 if the move calculates the base damage later (e.g. depending on the user's weight). For multi-hit moves, this is the damage dealt per hit.

**6. Type:**  
The internal name of the move's elemental type.

**7. Move category:**  
Is one of the following:
- Physical (calculates damage using Attack and Defense)
- Special (calculates damage using Special Attack and Special Defense)
- Status (inflicts no damage)

**8. Accuracy:**  
The move's accuracy, out of 100. Set to 0 if the move doesn't perform an accuracy check (i.e. it cannot be evaded).

**9. Total PP:**  	
The maximum amount of PP this move can have, not counting modifiers such as the item PP Up. If this is 0, the move is infinite use.

**10. Additional effect chance:**  
The probability that the move's additional effect occurs, out of 100. For example, Poison Sting poisons the opponent 30% of the time, so this value would be 30. Set to 0 if this move does nothing other than its effect (e.g. for all status moves).

**11. Target:**  
The battler(s) that this move will strike. Is one of the following values:
- 00 - Single Pokémon other than the user
- 01 - No target
- 02 - One opposing Pokémon selected at random
- 04 - All opposing Pokémon
- 08 - All Pokémon other than the user
- 10 - User
- 20 - Both sides (e.g. Light Screen, Reflect, Heal Bell)
- 40 - User's side
- 80 - Opposing Pokémon's side
- 100 - User's partner
- 200 - Player's choice of user or user's partner (e.g. Acupressure)
- 400 - Single Pokémon on opponent's side (e.g. Me First)
- 800 - Directly opposite Pokémon on opponent's side (used by Curse)

**12. Priority:**  
The order the move will be used in (overrides Speed calculations). Usually 0, but can be between -6 and 6. A higher value means higher priority. Moves with equal priority will be used depending on their user's Speed.
For example, Quick Attack has a priority of 1.

**13. Flags:**  

Any combination of the following letters:
- a - This move makes physical contact with the opponent.
- b - The opponent can use Protect or Detect to protect itself from this move.
- c - The opponent can use Magic Coat to redirect the effect of this move. Use this flag if the move deals no damage but causes a negative effect on an opponent. (Flags c and d are mutually exclusive.)
- d - The opponent can use Snatch to steal the effect of this move. Use this flag for most moves that target the user. (Flags c and d are mutually exclusive.)
- e - This move can be copied by Mirror Move.
- f - This move has a 10% chance of making the opponent flinch if the user is holding a King's Rock. Use this flag for all damaging moves.
- g - If the user is frozen, this move will thaw it out before it is used.
- h - This move has a high critical hit rate.
- i - This is a healing move.
- j - This move is a punching move.
- k - This is a sound-based move.
- l - While Gravity is in effect, this move is disabled for all active Pokémon.
- m - The move is a pulse-based move (powered up by the ability Mega Launcher).
- n - The move is a bomb-based move (resisted by the ability Bulletproof).

**14. Description:**  
The description of the move.
If there are any commas or apostrophes/double quote marks in the description, the entire description must be enclosed in double quote marks. The double quote marks in the description must also be preceded by a backslash "\".

### Examples

```
303,TACKLE,Tackle,000,50,NORMAL,Physical,100,35,0,00,0,abef,A physical attack in which the user charges and slams into the target with its whole body.
Tackle is a basic move with no special effect. It is a Normal-type physical move that deals 50 base damage with an accuracy of 100%. It has 35 PP, and can target any other Pokémon in battle.

419,TAILWHIP,Tail Whip,043,0,NORMAL,Status,100,30,0,04,0,bce,"The user wags its tail cutely, making opposing Pokémon less wary and lowering their Defense stat."
Tail Whip is a status move, meaning it doesn't inflict damage. It has a function code of 43 (defined as lowering the opponent's Defense by 1 stage). It affects all opposing Pokémon at once, and has an accuracy of 100%.

284,TRIATTACK,Tri Attack,017,80,NORMAL,Special,100,10,20,00,0,be,"The user strikes with a simultaneous three-beam attack. May also burn, freeze, or leave the target with paralysis."
Tri Attack is a special move that inflicts damage and has a 20% of its extra effect (inflicting either paralysis, a burn or freezing the opponent, corresponding to 6.67% chance of each).
```