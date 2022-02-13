import argparse
import os
import sys


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--path", "-p", default=os.getcwd(), help="path [default=cwd]")
    parser.add_argument("--file", "-f", help="name of file to find")
    args = parser.parse_args()

    try:
        for root, _dirs, files in os.walk(os.path.normpath(args.path)):
            for name in files:
                if args.file:
                    if args.file in name:
                        print(os.path.join(root, name))
                else:
                    print(os.path.join(root, name))

    except KeyboardInterrupt:
        sys.exit("Keyboard interrupt, quiting..")


if __name__ == "__main__":
    main()
