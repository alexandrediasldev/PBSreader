## items.txt

Information pulled from the old wiki on the way back machine:
September 28th 2015 - http://pokemonessentials.wikia.com/wiki/Defining_an_item
https://web.archive.org/web/20150928235506/http://pokemonessentials.wikia.com/wiki/Defining_an_item


**1. ID Number**:
Each item's ID number must be different. The ID number must be a whole number greater than 0 (i.e. 1,2,3...). Missing numbers are not a problem (e.g. the sequence 23,24,25,58,59,60,... is allowed).

**2. Internal name:**
Typically written only in capital letters with no spaces or symbols. This is the name the scripts refer to and use. This name is never seen by the player.

**3. Display name:**
The actual name of the item. This is only used when displaying the item's name on the screen.

**4. Pocket:**
The Bag pocket number the item is stored in. By default, is one of:
1. - Items
2. - Medicine
3. - Poké Balls
4. - TMs & HMs
5. - Berries
6. - Mail
7. - Battle Items
8. - Key Items

**5. Price:**
The cost of the item when you buy it. Note that when the item is sold, it is sold for half this price (by default). If an item has a price of 0, it cannot be sold.

**6. Description:**
The description of the item.
If there are any commas or apostrophes/double quote marks in the description, the entire description must be enclosed in double quote marks. The double quote marks in the description must also be preceded by a backslash "\".
Typically TMs and HMs will have the same description as the moves they teach, but they don't need to.

**7. Usability out of battle:**
Is one of the following values:
0. - The item cannot be used out of battle.
1. - The item can be used on a Pokémon, and disappears after use (e.g. Potions, Elixirs). The party screen will appear when using this item, allowing you to choose the Pokémon to use it on. Not for TMs and HMs, though.
2. - The item can be used out of battle, but it isn't used on a Pokémon (e.g. Repel, Escape Rope, usable Key Items).
3. - The item is a TM. It teaches a move to a Pokémon, and disappears after use.
4. - The item is a HM. It teaches a move to a Pokémon, but does not disappear after use.
5. - The item can be used on a Pokémon, but it does not disappear after use (e.g. Poké Flute).

**8. Usability in battle:**
Is one of the following values:
0. - The item cannot be used in battle.
1. - The item can be used on one of your party Pokémon, and disappears after use (e.g. Potions, Elixirs). The party screen will appear when using this item, allowing you to choose the Pokémon to use it on.
2. - The item is a Poké Ball, or the item can be used directly (e.g. X Accuracy et al, Poké Doll).
3. - The item can be used on a Pokémon, but does not disappear after use (e.g. Poké Flute).
4. - The item can be used directly, but does not disappear after use.

**9. Special items:**
Is one of the following values:
0. - The item is none of the items below.
1. - The item is a Mail item.
2. - The item is a Mail item, and the images of the holder and two other party Pokémon appear on the Mail.
3. - The item is a Snag Ball (i.e. it can capture enemy trainers' Shadow Pokémon).
4. - The item is a Poké Ball item.
5. - The item is a berry that can be planted.
6. - The item is a Key Item

**10. TM/HM move:**
This field is for TMs and HMs only, and contains the internal name of the move that it teaches.


### Examples
```
217,POTION,Potion,2,300,"A spray-type medicine for wounds. It restores the HP of one Pokémon by just 20 points.",1,1,0
This is a typical item. It goes in the "Medicine" pocket of the Bag (pocket 2), costs $300 to buy (and sells for $150), and is usable both in and outside battle (and disappears after use).

12,FIRESTONE,Fire Stone,1,2100,"A peculiar stone that makes certain species of Pokémon evolve. It is colored orange.",1,0,0,
This is an evolution stone. It is defined exactly the same way as a regular item. It is usable on a Pokémon outside of battle, but it cannot be used in battle.

288,TM01,TM01,4,3000,"The user sharpens its claws to boost its Attack stat and accuracy.",3,0,0,HONECLAWS
This is a TM. It goes in the "TMs & HMs" pocket of the Bag (pocket 4), costs $3000 to buy (and sells for $1500), is not usable in battle, and teaches the move Hone Claws.

HMs are defined in exactly the same way, except field number 7 (the one immediately after the description) contains the number "4" instead of "3".

510,TOWNMAP,Town Map,8,0,"A very convenient map that can be viewed anytime. It even shows your present location.",2,0,6
This is a Key Item. It goes in the "Key Items" pocket of the Bag (pocket 8), has a price of $0 (and thus cannot be bought; it can't be sold because it is a Key Item), can be used out of battle by itself (i.e. not on a Pokémon), and cannot be used in battle.
```