## 🟢 ribbons.txt

Information pulled from the new wiki:  
7 November 2021 - https://essentialsdocs.fandom.com/wiki/Defining_a_ribbon
https://essentialsdocs.fandom.com/wiki/Defining_a_ribbon?oldid=1109

**1. ID number:**  
This number must be different for each ribbon. It must be a whole number greater than 0. You can skip numbers (e.g. the sequence 23,24,25,197,198,199,... is allowed). The order in which ribbon are numbered is not important.
The ID number is used to determine which graphic from the file "ribbons.png" (in the folder Graphics/Pictures) should be used for that ribbon. This graphic is 8 ribbons wide and any number of ribbons tall. A ribbon's graphic must be 64x64 pixels in size.

**2. ID:**  
This must be different for each ribbon. This is how the scripts refer to the ribbon. Typically this is the same as the ribbon name, but written in all capital letters and with no spaces or symbols. In the scripts, the ID is used as a symbol (i.e. with a colon in front of it, e.g. :FOOTPRINT). The ID is never seen by the player.

**3. Name:**  
The name of the ribbon, as seen by the player in a Pokémon's summary screen.

**4. Description:**  
The ribbon's description, as seen by the player in a Pokémon's summary screen.
If there are any commas in the description, you must surround the entire description with quote marks. If there are no commas in the description, there's no harm in having those quote marks anyway.

If there are any quote marks in the description itself, you must put a backslash before each of them, e.g. \". The same applies if there are any apostrophes in the description and you haven't surrounded it with quote marks.

### Examples

``
1,HOENNCOOL,Cool Ribbon,"Hoenn Cool Contest Normal Rank winner!"
14,HOENNSMARTSUPER,Smart Ribbon Super,"Hoenn Smart Contest Super Rank winner!"
64,FOOTPRINT,Footprint Ribbon,"A Ribbon awarded to a Pokémon deemed to have a top-quality footprint."
66,EFFORT,Effort Ribbon,"Ribbon awarded for being an exceptionally hard worker."
``