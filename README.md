# D2S Save File Editor (LoD and D2R)


## Features
- Reset the cowking quest so the portal can be opened after killing the king (Norm, NM, and Hell)
- Reset the izual quest
- Reset the hell forge quest
- Reset the larzuk item socket quest


## Usage
1. Download [d2s_edit.exe](https://github.com/pairofdocs/d2s_edit_recalc/raw/master/d2s_edit.exe) and [patches.txt](https://github.com/pairofdocs/d2s_edit_recalc/blob/master/patches.txt) (right click "Raw" and "Save Link As") to the same folder
2. Edit `patches.txt` for quests that you want to reset by commenting/uncommenting specific lines ([example below](https://github.com/pairofdocs/d2s_edit_recalc/blob/master/README.md#example))
3. Double click `d2s_edit.exe` to start the app
4. Click on "Open File and Run" to select you `.d2s` character file and apply the edits from `patches.txt`. Save files are in `Saved Games\Diablo II Resurrected Tech Alpha\`
5. Start D2

- ![GUI](https://i.imgur.com/BIRWq8W.png)

**Note**: The first time `d2s_edit.exe` is run on a char file (e.g. `MyAwesomeChar.d2s`), it creates a backup file (`MyAwesomeChar.d2s.bak`). 
This backup can be moved/copied and used if you want to undo any changes.


## Example

`patches.txt:`

This is the NM larzuk quest edit **disabled**:
```txt
# reset larzuk quest NM
# 511, 00 00
```

This is the quest edit **enabled**:
```txt
# reset larzuk quest NM
511, 00 00
```

This is the Map ID, Seed edit **enabled**:
```
# set the char seed to `1337`
171, 1337, decimal
```


## Build GUI
`pip install wxpython pyinstaller`  
`pyinstaller --add-data 'd2logo_sm.png;.' --onefile -w d2s_edit.py`  ([Note](https://pyinstaller.readthedocs.io/en/stable/usage.html#what-to-bundle-where-to-search): use `d2logo_sm.png;.` on windows  and `d2logo_sm.png:.` on most unix systems)


## Credits and Tools 
- d2s save file format, https://user.xmission.com/~trevin/DiabloIIv1.09_File_Format.shtml
- d2s file format https://github.com/krisives/d2s-format
- Themperor on discord for the RecalcCRC.exe tool
- d2s converter, TY Riv, https://d07riv.github.io/d2r.html 
- d2s converter, TY Dschu, https://dschu012.github.io/d2s/
