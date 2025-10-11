from InquirerPy import prompt

def interactive_setup():
    print("🥐 Welcome to Croissant Interactive Setup!\n")

    loader_type = prompt({
        "type": "list",
        "name": "loader_type",
        "message": "Choose loader type:",
        "choices": [
            "Mod Loader (Forge / Fabric / NeoForge / Quilt)",
            "Plugin Loader (Paper / Purpur / Spigot)"
        ]
    })["loader_type"]

    folder = prompt({
        "type": "input",
        "name": "folder",
        "message": "Enter folder name:",
        "default": "myserver"
    })["folder"]

    version = prompt({
        "type": "input",
        "name": "version",
        "message": "Enter Minecraft version (e.g., 1.20.1):",
        "default": "1.20.1"
    })["version"]

    if "Mod" in loader_type:
        loader = prompt({
            "type": "list",
            "name": "loader",
            "message": "Select mod loader:",
            "choices": ["Forge", "Fabric", "NeoForge", "Quilt"]
        })["loader"]
    else:
        loader = prompt({
            "type": "list",
            "name": "loader",
            "message": "Select plugin loader:",
            "choices": ["Paper", "Purpur", "Spigot"]
        })["loader"]

    mldver_choice = prompt({
        "type": "list",
        "name": "mldver_choice",
        "message": "Select modloader version:",
        "choices": ["Latest", "Custom"]
    })["mldver_choice"]

    if mldver_choice == "custom":
        mldver = prompt({
            "type": "input",
            "name": "mldver",
            "message": f"Enter specific {loader} version (e.g., 47.1.3):"
        })["mldver"]
    else:
        mldver = "latest"

    print("\n+) Summary:")
    print(f"  Folder: {folder}")
    print(f"  Minecraft Version: {version}")
    print(f"  Loader: {loader}")
    print(f"  Modloader Version: {mldver}")
    print()

    confirm = prompt({
        "type": "confirm",
        "name": "confirm",
        "message": "Proceed with creation?",
        "default": True
    })["confirm"]

    if not confirm:
        print("Cancelled.")
        return None

    return folder, version, loader.lower(), mldver