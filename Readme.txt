[h1]Load Order[/h1]
Not important.

[h1]Older Versions[/h1]
[url=https://steamcommunity.com/sharedfiles/filedetails/?id=1885029758]For 2.3[/url]
[url=https://steamcommunity.com/sharedfiles/filedetails/?id=1897590215]For 2.4[/url]

[h1]FAQ[/h1]
[i]What does this mod do?[/i]
It allows you as a player via edict to set a number of allowed subspecies (per empire) up to 20. It doesn't do anything more or less.

[i]Does the limit apply to player?[/i]
No.

[i]What's the point of this mod?[/i]
Well... The AI creates all sorts of subspecies whether it needs to or not. That can clutter the UI so I kinda thought you might want to limit that and make AI stop spamming so many subspecies.

[i]Have you tested this?[/i]
Not very much. I used a "has_country_flag" instead of "is_ai = no" to switch between players in order to test this on the species screen. Cannot exactly test "is_ai = no" condition really any other way.

[i]Is it compatible with xyz mod?[/i]
It is compatible with any mod (in theory) which doesn't modify "can_modify_species" game rule.

[i]Is it Ironman or Achievement compatible?[/i]
Please, this is a scripting change. It obviously is not compatible.

[i]Can you do xyz?[/i]
Maybe, if I want to really.

[i]What languages are supported?[/i]
English. English is also not my primary language FYI (if you find spelling mistakes report them and I will fix them).

[i]Is it savegame compatible?[/i]
In short: yes. You can install it safely on top of an existing save game. The only drawback is that the mod will kick in from the moment you installed that mod. Which means that any species created up until that point will remain in the game. That is beyond the scope of this mod however.

[i]Can I uninstall it safely?[/i]
Yes, you can install\uninstall as you wish and it shouldn't mess up your game. Upon uninstallation some country flags will remain which should never have any impact upon your game. In fact if I didn't mention these flags (not literal flags though) you probably wouldn't even know of these. That's how insignificant they are.

[i]Is it possible to shutdown AI's ability to modify species completely?[/i]
That's been possible from day one. Recent changes better explain that functionality in the mod. In short just set the number of allowed species to 1 and consider it shut down.

[i]I want to prevent the mod from using the edicts menu, is there anything that I can do?[/i]
Check out [url=https://steamcommunity.com/sharedfiles/filedetails/?id=1840010432]Dynamic Mod Menu[/url], this mod has full support for it.

[i]Can you limit the number of hybrid species being created?[/i]
I am sorry to disappoint I can't prevent half species from being created programmatically or limit them at all. Paradox's conditions don't work, namely the "is_half_species" trigger which is the only way to find out if a species is a hybrid. No way to workaround the issue as no other exposed API calls can be used to find out if a species is a hybrid. Until it's fixed your best bet is:
1. Cope with it (not what you wanted to hear)
2. Nag PDX to fix the feature 
3. Nag PDX to fix "is_half_species" trigger
4. Disable Xeno-Compatibility
...