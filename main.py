import argparse
import os
import sys


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--path", "-p", default=os.getcwd(), help="path [default=cwd]")
    parser.add_argument("--file", "-f", help="name of file to find")
    args = parser.parse_args()

    path = os.path.abspath(args.path)

    try:
        for root_path, _dirs, files in os.walk(path):
            for basename in files:
                if args.file is not None:
                    if args.file in basename:
                        print(os.path.join(root_path, basename))
                else:
                    print(os.path.join(root_path, basename))

    except KeyboardInterrupt:
        sys.exit("Keyboard interrupt, quiting..")


if __name__ == "__main__":
    main()
