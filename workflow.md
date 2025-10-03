# 🥐 Croissant - Tasks

## Task 1 - CLI Skeleton 🤓
- Create a Python CLI using argparse
- Cmd format:
```bash
croissant create <name-folder> <mc-ver> <modloader> <modloader-ver>
```
- Test: simply print the arguments w no logic yet

## Task 2 - Folder n file skeleton 🤓
- Creat a new folder from name-folder
- Generate basic placeholder files inside it

- Test: after running, the files and folders exist w content

## Task 3 - Templates Files
- Move file content gen into a new module templates.py
- Update start.sh to contain read start cmd:
```
java -Xmx4G -Xms2G -jar server.jar nogui
```

## Task 4 - Download vanilla server
- Use mojang ver manifest api to get correct server.jar url for the requested ver
- Download and save as server.jar
- Test: produces a valid vanilla

## Task 5 - Setup modloader
- Run it via subprocess to gen server files
