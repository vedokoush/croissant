import handler
import folder

def main():
    args = handler.info()
    if args.command == "create":
        folder.init(args)

if __name__ == "__main__":
    main()