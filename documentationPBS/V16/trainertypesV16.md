## 🟡 trainertypes.txt

Information pulled from the old wiki on the way back machine:  
March 17th 2017 - http://pokemonessentials.wikia.com/wiki/Defining_a_trainer  
https://web.archive.org/web/20170316135708/http://pokemonessentials.wikia.com/wiki/Defining_a_trainer

**1. ID number:**  	
The trainer type's ID number.

**2. Internal Name:**  	
The trainer type's internal name. This must be unique amongst all the trainer type internal names.

**3.   Name:**  	
The trainer type's name, as displayed in the game (e.g. "Camper", "Swimmer", "PkMn Trainer"). Two or more trainer types can share the same name (but not the same internal name).

**4.   Base money:**  	
Optional. The amount of money earned from defeating a trainer of this type. This number is multiplied by the highest Level among all the trainer's Pokémon. Must be a number between 0 and 255.
Default is 30.
   
**5. Battle BGM:**  		
Optional. The background music (BGM) file that plays during battles against trainers of this type. Typically only defined for Gym Leaders, Elite Four members and rivals.
If blank, the default BGM is used.

**6. Victory ME:**  	
Optional. The victory background music that plays upon defeat of trainers of this type.
If blank, the default victory BGM is used.

**7. Intro ME:**  		
Optional. The music effect (ME) that plays before the battle begins.
If blank, the default ME is used.

**8. Gender:**  
Optional. The gender of all trainers of this type. Is one of:
- Male
- Female
- Mixed (i.e. if the type shows a pair of trainers)

**9. Skill Level:**  	
Optional. The skill level of the trainer, used for battle AI.
If blank, this becomes equal to the base money for the trainer.

**🟢 10. Skill codes:**  
A text field which can be used to modify the AI behaviour of all trainers of this type. No such modifiers are defined by default, and there is no standard format. See the page Battle AI for more details.
Optional. If undefined, the default is blank.



### Examples
```
0,POKEMONTRAINER_Red,Pokémon Trainer,60,,,,Male,
15,FISHERMAN,Fisherman,32,,,,Male,
55,YOUNGCOUPLE,Young Couple,60,,,,Mixed,32
59,LEADER_Brock,Gym Leader,100,gymleader,,,Male,
60,LEADER_Misty,Gym Leader,100,gymleader,,,Female,
```
