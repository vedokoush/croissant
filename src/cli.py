import handler
import folder
import download
import installer
from templates import eula
import start
import json
import os
import sys

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
    args = handler.info()

    if args.command == "create":
        folder.init(args)
        if args.modloader == "forge":
            set_tag(args.folder, "forge")
        elif args.modloader == "fabric":
            set_tag(args.folder, "fabric")

        # print(args.folder)
        file_name = download.downloader(args.version, args.modloader, args.mldver, args.folder)
        print(file_name)
        if (args.modloader == "forge"):
            installer.installServer(args.folder, file_name)
        eula.write_eula(args.folder)

    elif args.command == "start":
        # print(get_tag(args.folder))
        if (get_tag(args.folder) == "forge"):
            start.start_forge_server(args.folder)
        elif (get_tag(args.folder) == "fabric"):
            start.start_fabric_server(args.folder)
        else:
            print("Unknown command")


if __name__ == "__main__":
    main()
