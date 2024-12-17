import sys
from pathlib import Path
from colorama import Fore, Style

def main(path):
    """
    Takes the path to a directory and visualizes 
    the structure of this directory, displaying 
    the names of all subdirectories and files
    """
    try:
        for obj in path.iterdir():
            if obj.is_dir():
                print(Fore.YELLOW + obj.name)
                main(path / obj.name)
            else:
                print(Fore.BLUE + obj.name)
    except NotADirectoryError:
        print("Заданий шлях не веде до директорії")
    except FileNotFoundError:
        print("Заданий шлях не існує")


if __name__ == '__main__':
    main(Path(sys.argv[1]))
    print(Style.RESET_ALL)