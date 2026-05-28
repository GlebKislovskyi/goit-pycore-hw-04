import sys
from pathlib import Path
from colorama import Fore, init

init()


def show_directory(path, level=0):
    """
    Recursively displays directory structure with colored output.
    Directories are shown in blue, files in green.
    """
    try:
        directory = Path(path)

        if not directory.exists():
            print(Fore.RED + "Шлях не існує." + Fore.RESET)
            return

        if not directory.is_dir():
            print(Fore.RED + "Це не директорія." + Fore.RESET)
            return

        for item in directory.iterdir():
            indent = "  " * level

            if item.is_dir():
                print(Fore.BLUE + indent + f"{item.name}/" + Fore.RESET)
                show_directory(item, level + 1)
            else:
                print(Fore.GREEN + indent + item.name + Fore.RESET)

    except PermissionError:
        print(Fore.RED + f"Помилка: Доступ заборонено." + Fore.RESET)
    except Exception as e:
        print(Fore.RED + f"Помилка: {e}" + Fore.RESET)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Вкажіть шлях до папки")
    else:
        show_directory(sys.argv[1])
