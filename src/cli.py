import handler
import folder
import download
import installer
from templates import eula
import start

def main():
    args = handler.info()
    if args.command == "create":
        folder.init(args)
        file_name = download.downloader(args.version, args.modloader, args.mldver, args.folder)
        installer.installServer(args.folder, file_name)
        eula.write_eula(args.folder)

    elif args.command == "start":
        start.startServer()


if __name__ == "__main__":
    main()
