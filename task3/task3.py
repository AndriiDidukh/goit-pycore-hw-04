import sys
from pathlib import Path
from colorama import Fore, Style


def visualize_directory(directory, indent=''):
    try:
        p = Path(directory)
        if not p.exists():
            print(Fore.RED + f"Error: The path {directory} does not exist." + Style.RESET_ALL)
            return
        if not p.is_dir():
            print(Fore.RED + f"Error: The path {directory} is not a directory." + Style.RESET_ALL)
            return

        for item in p.iterdir():
            if item.is_dir():
                print(Fore.BLUE + indent + f"[D] {item.name}" + Style.RESET_ALL)
                visualize_directory(item, indent + '    ')
            else:
                print(Fore.GREEN + indent + f"[F] {item.name}" + Style.RESET_ALL)
    except Exception as e:
        print(Fore.RED + f"An error occurred: {e}" + Style.RESET_ALL)


directory_path = sys.argv[1]
visualize_directory(directory_path)