## 🟡 items.txt

Information pulled from the new wiki:
24 June 2022 -  https://essentialsdocs.fandom.com/wiki/Defining_an_item
https://essentialsdocs.fandom.com/wiki/Defining_an_item?oldid=1403
The PBS file "items.txt" lists all the defined items in the game. Each section in this file is one separate item, where a section begins with a line containing an ID in square brackets and ends when the next section begins. Each line in a section is one separate piece of information about that item.

🟡 Aside from the ID line, every line in a section follows the format:

```
XXX = YYY
```

where XXX is a property and YYY is the value or values associated with it (the spaces are optional).

**[ID]**:
This is how the scripts refer to the item. Each item must have a different ID. Typically this is the same as the item name, but written in all capital letters and with no spaces or special characters. In the scripts, the ID is used as a symbol (i.e. with a colon in front of it, e.g. :POTION). The ID is never seen by the player.
This line must come first in a section, because, as mentioned above, this line defines when a new section begins.

In Bag pockets that auto-sort themselves, items will be sorted in the same order that they are defined in the PBS file "items.txt".

**🔴 Internal name:**
REMOVED

**Name:**
The name of the item, as seen by the player.

**NamePlural**
The plural form of the name of the item, as seen by the player. For example, "Potions".

**Pocket:**
The Bag pocket number the item is stored in. By default, is one of:
1. - Items
2. - Medicine
3. - Poké Balls
4. - TMs & HMs
5. - Berries
6. - Mail
7. - Battle Items
8. - Key Items

The list of Bag pockets is in the script section Settings, in def self.bag_pocket_names.

**Price:**
The cost of the item when the player buys it from a Poké Mart. Note that when the player sells the item to a Poké Mart, it is sold for half this price (by default; see SellPrice). If an item has a price of 0, the player cannot sell it.

**🟢 SellPrice:**
The amount of money gained when selling the item to a Poké Mart.


**FieldUse:**
How the item can be used outside of battle. Is one of the following:
- OnPokemon - The item can be used on a Pokémon (e.g. Potions, Elixirs). The party screen will appear when using this item, allowing you to choose the Pokémon to use it on. Not for TMs, TRs and HMs, though.
- Direct - The item can be used out of battle, but it isn't used on a Pokémon (e.g. Repel, Escape Rope, usable Key Items).
- TR - The item is a TR. It teaches a move to a Pokémon, and disappears after use.
- TM - The item is a TM. It teaches a move to a Pokémon, but does not disappear after use.
- HM - The item is a HM. It teaches a move to a Pokémon, but does not disappear after use. Moves taught by a HM cannot be forgotten.

**BattleUse:**
How the item can be used in battle. Is one of the following:
- OnPokemon - The item can be used on one of your party Pokémon (e.g. Potions, Elixirs, Blue Flute). The party screen will appear when using this item, allowing you to choose the Pokémon to use it on.
- OnMove - The item can be used on one of the moves known by one of your party Pokémon (e.g. Ether). The party screen will appear when using this item, followed by a list of moves to choose from.
- OnBattler - The item is used on the Pokémon in battle that you are choosing a command for (e.g. X Accuracy, Red/Yellow Flutes).
- OnFoe - The item is used on an opposing Pokémon in battle (Poké Balls). If there is more than one opposing Pokémon, you will be able to choose which of them to use it on.
- Direct - The item is used with no target (e.g. Poké Doll, Guard Spec., Poké Flute).

**🟢 Consumable:**
Whether the item will be consumed after being used from the Bag. Is true or false. Usually only used to make a non-Key Item infinite use (e.g. Black/White Flutes).

**🟡 Special Items -> Flags:**
Comma-separated labels applied to the item which can be used to make it behave differently. The existing flags are:
- Mail - The item is a Mail item.
- IconMail - The item is a Mail item, and the images of the holder and two other party Pokémon appear on the Mail.
- PokeBall - The item is a Poké Ball item.
- SnagBall - The item is a Snag Ball (i.e. it can capture enemy trainers' Shadow Pokémon).
- Berry - The item is a berry that can be planted.
- KeyItem - The item is a Key Item.
- EvolutionStone - The item is an evolution stone.
- Fossil - The item is a fossil that can be revived. Not to be used for the incomplete fossils from Gen 8 which are pieced together to revive a Pokémon.
- Apricorn - The item is an Apricorn that can be converted into a Poké Ball.
- TypeGem - The item is an elemental power-raising Gem.
- Mulch - The item is mulch that can be spread on berry patches.
- MegaStone - The item is a Mega Stone. This does NOT include the Red/Blue Orbs.
- MegaRing - The item is a Mega Ring, which allows Mega Evolution.
- Repel - The item is a Repel, and can be used automatically when a Repel runs out.
- Fling_30 - The item can be thrown by the move Fling. The number is Fling's base power when used with the item. The number can be any number, but should be greater than 0.
- NaturalGift_POISON_80 - The item can be used by the move Natural Gift. The type and number are Natural Gift's type and base power when used with the item. The type can be any type, and the number can be any number but should be greater than 0.

**Move:**
The ID of the move that this item teaches. For HMs, TMs and TRs only.
A Pokémon is compatible with a HM/TM/TR if and only if the move it teaches is listed a a Tutor Move for its species in the PBS file "pokemon.txt" (or in "pokemon_forms.txt" if appropriate). The species having access to that move via its level-up moveset or as an egg move will not count. See the page Learning moves for more information.

**Description:**
The item's description. Typically, HMs, TMs and TRs will have the same description as the moves they teach, but they don't need to.

### Examples
```
[POTION]
Name = Potion
NamePlural = Potions
Pocket = 2
Price = 200
FieldUse = OnPokemon
BattleUse = OnPokemon
Flags = Fling_30
Description = A spray-type medicine for treating wounds. It can be used to restore 20 HP to a single Pokémon.
#-------------------------------
[TM42]
Name = TM42
NamePlural = TM42s
Pocket = 4
Price = 3000
FieldUse = TR
Flags = Fling_70
Move = FACADE
Description = This attack move doubles its power if the user is poisoned, burned, or paralyzed.
#-------------------------------
[TOWNMAP]
Name = Town Map
NamePlural = Town Maps
Pocket = 8
Price = 0
FieldUse = Direct
Flags = KeyItem
Description = A very convenient map that can be viewed anytime. It even shows your present location.
```