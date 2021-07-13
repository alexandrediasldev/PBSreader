### 🟢 berryplants.txt

Information pulled from the old wiki on the way back machine:  
March 16th 2017 - http://pokemonessentials.wikia.com/wiki/Berry_planting  
https://web.archive.org/web/20170316172253/http://pokemonessentials.wikia.com/wiki/Berry_planting



Each line in this file is one separate berry plant, and is associated with an item (the one you plant/harvest).

Every line in this file follows the same format.

The item's internal name is first, followed by an equals sign and then four values separated by commas. These values are:

1. The growth rate (i.e. the number of hours between growth stages)
2. How much moisture the soil loses per hour (Gen 4 mechanics only)
3. The minimum yield (how many berries can be picked if the plant is never watered)
4. The maximum yield (how many berries can be picked in the plant is always watered)

If a berry plant is not defined in this file, it will use these default values: 3,15,2,5.

### Example
```
CHERIBERRY=3,15,2,5
WEPEARBERRY=2,35,2,10
OCCABERRY=18,6,1,5
```