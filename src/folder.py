import os

def init(args):
    folder = args.folder
    os.makedirs(folder, exist_ok=True)

    # print(f"Created folder: {folder}")
    # print(f"Version: {args.version}")
    # print(f"Modloader: {args.modloader}")
    # print(f"Modloader version: {args.mldver}")