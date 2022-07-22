### 🟡 berry_plants.txt

Information pulled from the new wiki:
23 May 2022 - https://essentialsdocs.fandom.com/wiki/Berry_planting
https://essentialsdocs.fandom.com/wiki/Berry_planting?oldid=1224
Every berry plant must be defined in the PBS file "berry_plants.txt". Each section in this file is one separate berry plant, where a section begins with a line containing an item ID in square brackets and ends when the next section begins. Each line in a section is one separate piece of information about that berry plant.

Aside from the ID line, every line in a section follows the format:

```
XXX = YYY
```
where XXX is a property and YYY is the value or values associated with it (the spaces are optional). For example:

**[ID]:**
The ID of the item to be planted to produce the berry plant, which is also the item produced by the berry plant. Each berry plant must produce a different item.

**HoursPerStage:**
The growth rate, i.e. the number of hours between growth stages.

**DryingPerHour	:**
How much moisture the soil loses per hour (newer berry plant mechanics only). A berry plant begins with 100 moisture, and returns to 100 moisture when it is watered.

**🟡 Yield:**
Two numbers that denote a range. The number of berries yielded by the berry plant falls within this range, and is higher the more it was watered.
### Example
```
[CHERIBERRY]
HoursPerStage = 3
DryingPerHour = 15
Yield = 2,5
#-------------------------------
[WEPEARBERRY]
HoursPerStage = 2
DryingPerHour = 35
Yield = 2,10
#-------------------------------
[OCCABERRY]
HoursPerStage = 18
DryingPerHour = 6
Yield = 1,5
```