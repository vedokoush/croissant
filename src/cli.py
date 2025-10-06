import handler
import folder
import download
import installer
from templates import eula
import start
import json
import os
import sys
from interactive import interactive_setup


def set_tag(folder_path, tag_name):
    tag_file = os.path.join(folder_path, ".tag")
    with open(tag_file, "w") as f:
        json.dump({"tag": tag_name}, f)


def get_tag(folder_path):
    tag_file = os.path.join(folder_path, ".tag")
    try:
        with open(tag_file, "r") as f:
            data = json.load(f)
        return data.get("tag")
    except (json.JSONDecodeError, OSError, KeyError):
        return None


def main():
    if len(sys.argv) == 1:
        result = interactive_setup()
        if not result:
            return
        folder_name, version, modloader = result
        mldver = "latest"
        folder.init(type("Args", (), {"folder": folder_name}))
        set_tag(folder_name, modloader)
        file_name = download.downloader(version, modloader, mldver, folder_name)
        print(f"Created {folder_name}/{file_name}")
        if modloader in ("forge", "paper"):
            installer.installServer(folder_name, file_name)
        eula.write_eula(folder_name)
        return

    args = handler.info()

    if args.command == "create":
        folder.init(args)
        set_tag(args.folder, args.modloader)
        file_name = download.downloader(args.version, args.modloader, args.mldver, args.folder)
        print(file_name)
        if modloader in ("forge", "paper"):
            installer.installServer(args.folder, file_name)
        eula.write_eula(args.folder)

    elif args.command == "start":
        tag = get_tag(args.folder)
        if tag == "forge":
            start.start_forge_server(args.folder)
        elif tag == "fabric":
            start.start_fabric_server(args.folder)
        else:
            print("Unknown command")


if __name__ == "__main__":
    main()
