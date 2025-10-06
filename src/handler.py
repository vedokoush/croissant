import argparse
import sys

VERSION = "0.1.0"

def help():
    print("Usage: croissant [OPTIONS] / [OPERATIONS]...\n")
    print("  Setup a Minecraft server effortlessly.\n")
    print("  Croissant helps you create and start Minecraft servers with your preferred")
    print("  modloader. Designed for lazy people.\n")
    print("Operations:")
    print("  croissant create [folder] [version] [modloader] [modloader_version]")
    print("  croissant start [folder]\n")

    print("Options:")
    print("  -h, --help        Show this message and exit.")
    print("  -v, --version     Show the version and exit.\n")
    print("Commands:")
    print("  create   Create a new Minecraft server setup (folder + modloader)")
    print("  start    Start an existing Minecraft server\n")

def info():
    if "-h" in sys.argv or "--help" in sys.argv:
        help()
        sys.exit(0)

    if "-V" in sys.argv or "--version" in sys.argv:
        print(f"croissant {VERSION}")
        sys.exit(0)

    parser = argparse.ArgumentParser(add_help=False)
    subparsers = parser.add_subparsers(dest="command")

    create_parser = subparsers.add_parser("create")
    create_parser.add_argument("folder")
    create_parser.add_argument("version")
    create_parser.add_argument("modloader")
    create_parser.add_argument("mldver")

    start_parser = subparsers.add_parser("start")
    start_parser.add_argument("folder")

    args = parser.parse_args()

    if not args.command:
        print("Error: missing command.\n")
        print("Try 'croissant --help' for usage.")
        sys.exit(1)

    return args
