import argparse

def info():
    parser = argparse.ArgumentParser(
        prog="croissant",
        description="setup a minecraft server for lazy"
    )

    subparsers = parser.add_subparsers(dest="command", required=True)

    create_parser = subparsers.add_parser("create", help="create a new minecraft server setup")
    create_parser.add_argument("folder", help="target folder name")
    create_parser.add_argument("version", help="minecraft version")
    create_parser.add_argument("modloader", help="minecraft modloader")
    create_parser.add_argument("mldver", help="minecraft modloader version")


    args = parser.parse_args()

    return args

