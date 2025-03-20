import subprocess
from os import name, system
from time import sleep
import requests as rq
from colorama import Fore, init


def main():
    """
    Main function that prompts the user to select an action,
    and executes the corresponding function based on user input.
    It keeps prompting until the user selects a valid choice (1/2/3/4).

    :return: None
    """
    while True:
        choice = input(f"{Fore.BLUE}Enter your choice (1/2/3/4): {Fore.MAGENTA}")

        if choice == "1":
            fetch_package_info()
            break

        elif choice == "2":
            install_package()
            break

        elif choice == "3":
            uninstall_package()
            break

        elif choice == "4":
            clear_terminal()
            print(f"{Fore.BLUE}Exiting program. Goodbye!{Fore.MAGENTA}")
            break

        else:
            print(f"{Fore.RED}Invalid choice! Please enter a valid option (1, 2, 3, 4): ")


def clear_terminal():
    """
    Clears the terminal screen based on the operating system.

    If the operating system is Windows, it uses 'cls' to clear the terminal.
    If the operating system is Linux or Mac, it uses 'clear' to clear the terminal.

    :return: None
    """
    if name == 'nt':  # Windows
        system("cls")
    else:  # Linux/Mac
        system("clear")


def fetch_package_info():
    """
    Fetches package information from PyPI and displays it with animations.
    Allows the user to retry fetching the package information in case of failure.

    The information includes:
    - Name
    - Version
    - Summary
    - Author
    - Documentation URL
    - Source URL

    If an error occurs during the request, the user is given the option to retry or cancel.

    :return: None
    """
    while True:
        clear_terminal()
        package_name = input(f"{Fore.BLUE}Enter package name: {Fore.MAGENTA}")

        url = f"https://pypi.org/pypi/{package_name}/json"
        try:
            response = rq.get(url, timeout=5)
            response.raise_for_status()  # Check for a successful response
            data = response.json()
            package_info = data.get("info", {})

            # Extract relevant package information
            name = package_info.get("name", "Unknown")
            version = package_info.get("version", "Unknown")
            summary = package_info.get("summary", "No description available.")
            author = package_info.get("author", "Unknown")
            project_urls = package_info.get("project_urls", {})
            documentation_url = project_urls.get("Documentation", "No documentation available")

            # Display animations and the fetched data
            clear_terminal()
            print("🔎 Searching.")
            sleep(0.7)
            clear_terminal()
            print("📦 Searching..")
            sleep(0.7)
            clear_terminal()
            print("📩 Searching...")
            sleep(0.7)
            clear_terminal()

            print(
                f"{Fore.BLUE}Package Name: {Fore.MAGENTA}{name}\n"
                f"{Fore.BLUE}Version: {Fore.MAGENTA}{version}\n"
                f"{Fore.BLUE}Description: {Fore.MAGENTA}{summary}\n"
                f"{Fore.BLUE}Author: {Fore.MAGENTA}{author}\n"
                f"{Fore.BLUE}Documentation: {Fore.MAGENTA}{documentation_url}\n"
                f"{Fore.BLUE}Source: {Fore.MAGENTA}{url}"
            )
            break  # Exit the loop after successful fetch
        except rq.exceptions.RequestException as e:
            print(f"{Fore.RED}Error fetching package details: {Fore.MAGENTA}{str(e)}")
            retry = input(f"{Fore.BLUE}Do you want to try again? (y/n): {Fore.MAGENTA}")
            if retry.lower() != 'y':
                print(f"{Fore.BLUE}Operation canceled.{Fore.MAGENTA}")
                break


def install_package():
    """
    Prompts the user to input a package name and attempts to install it using pip.
    If the package is already installed, it notifies the user.

    If the package is not found or there is an error during installation, the user is given the option to retry or cancel.

    :return: None
    """
    while True:
        clear_terminal()
        package_name = input(f"{Fore.BLUE}Enter package name: {Fore.MAGENTA}")

        try:
            subprocess.check_output(["pip", "show", package_name])
            print(f"{Fore.MAGENTA}{package_name} is already installed.")
            break
        except subprocess.CalledProcessError:
            try:
                subprocess.check_call(["pip", "install", package_name])
                print(f"{Fore.MAGENTA}{package_name} has been installed successfully.")
                break
            except subprocess.CalledProcessError:
                print(f"{Fore.RED}Couldn't find or install {package_name}. Please check if the package name is correct.")
                retry = input(f"{Fore.BLUE}Do you want to try again? (y/n): {Fore.MAGENTA}")
                if retry.lower() != 'y':
                    print(f"{Fore.BLUE}Operation canceled.{Fore.MAGENTA}")
                    break


def uninstall_package():
    """
    Prompts the user to input a package name and attempts to uninstall it using pip.
    If the package is not found, it notifies the user.

    If the package is installed, it will be uninstalled successfully. If there is an error, the user is given the option to retry or cancel.

    :return: None
    """
    while True:
        clear_terminal()
        package_name = input(f"{Fore.BLUE}Enter package name: {Fore.MAGENTA}")
        try:
            subprocess.check_output(["pip", "show", package_name])
            subprocess.check_call(["pip", "uninstall", package_name, "-y"])
            print(f"{Fore.MAGENTA}{package_name} has been uninstalled successfully.")
            break
        except subprocess.CalledProcessError as e:
            if "not found" in str(e):
                print(f"{Fore.RED}{package_name} is not installed.{Fore.MAGENTA}")
            else:
                print(f"{Fore.RED}An error occurred while uninstalling {package_name}.{Fore.MAGENTA}")
            retry = input(f"{Fore.BLUE}Do you want to try again? (y/n): {Fore.MAGENTA}")
            if retry.lower() != 'y':
                print(f"{Fore.BLUE}Operation canceled.{Fore.MAGENTA}")
                break


if __name__ == "__main__":
    """
    This is the entry point of the program. It clears the terminal screen,
    initializes colorama for colored output, and prints the welcome message.
    Then, it calls the main() function to start the user interaction.

    :return: None
    """
    clear_terminal()
    init()

    print(Fore.BLUE + """███╗   ███╗██╗███╗   ██╗██╗    ██████╗ ██╗   ██╗██████╗ ██╗
████╗ ████║██║████╗  ██║██║    ██╔══██╗╚██╗ ██╔╝██╔══██╗██║
██╔████╔██║██║██╔██╗ ██║██║    ██████╔╝ ╚████╔╝ ██████╔╝██║
██║╚██╔╝██║██║██║╚██╗██║██║    ██╔═══╝   ╚██╔╝  ██╔═══╝ ██║
██║ ╚═╝ ██║██║██║ ╚████║██║    ██║        ██║   ██║     ██║
╚═╝     ╚═╝╚═╝╚═╝  ╚═══╝╚═╝    ╚═╝        ╚═╝   ╚═╝     ╚═╝""")

    print(Fore.MAGENTA + "━" * 100)
    print(f"{Fore.BLUE}Developer: Vahid Siyami")
    print(f"{Fore.BLUE}GitHub: https://github.com/BraveVahid")
    print(f"{Fore.BLUE}Telegram: https://t.me/pycevz")
    print(Fore.MAGENTA + "━" * 100)
    print(f"{Fore.BLUE}I'm here to help you search and find Python packages based on your needs. Let’s get started!")
    print(f"\t{Fore.MAGENTA}【1】 {Fore.BLUE}Search for the package: ")
    print(f"\t{Fore.MAGENTA}【2】 {Fore.BLUE}Install package: ")
    print(f"\t{Fore.MAGENTA}【3】 {Fore.BLUE}Uninstall package: ")
    print(f"\t{Fore.MAGENTA}【4】 {Fore.BLUE}Exit")

    # Start the main menu
    main()
