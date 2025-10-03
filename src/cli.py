import handler
import folder
import download

def main():
    args = handler.info()
    if args.command == "create":
        folder.init(args)
        download.downloader(args.version, args.modloader, args.mldver, args.folder)

if __name__ == "__main__":
    main()
