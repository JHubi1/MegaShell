import os
from termcolor import colored
import sys
import platform
import getpass
import re
import datetime

class __info:
    VERSION = "0.0.1"
    AUTHOR = "Xenia Software, Inc."
    LICENSE = "Apache License 2.0"
    LICENSE_WITH_PATH = "Apache License 2.0 (View in '" + os.path.abspath("LICENSE") + "')"
    SYSTEM = platform.system().lower()
info = __info()

class __tools:
    defaultColor = "blue"
    def __init__(self, defaultColor: str = "blue") -> None:
        """Initial function to set the default color.

        Args:
            defaultColor (str, optional): The defualt color. Defaults to "blue".
        """
        self.defaultColor = defaultColor
    def fprint(self, *values: object, sep: str | None = " ", end: str | None = "\n", config: dict = {"color": defaultColor, "start": "|"}) -> None:
        """Prints a text to the terminal in the MegaShell style.

        Args:
            sep (str | None, optional): The seperator to use if `values` is a list. Defaults to " ".
            end (str | None, optional): The end of the line. Defaults to "\n".
            config (_type_, optional): The configuration. Defaults to {"color": defaultColor, "start": "|"}.
        """
        if len(config["start"]) <= 1:
            config["start"] += " "*(2-len(config["start"]))
        if type(values[0]) == list: text = sep.join(values[0])
        else: text = sep.join(values)
        values = colored(config["start"], config["color"]) + text
        print(values, end=end)
    def fprintTitle(self, *values: object, sep: str | None = " ", end: str | None = "\n", config: dict = {"color": defaultColor, "start": "+- "}) -> None:
        """Prints a title and calculates the right space with `-`.

        Args:
            sep (str | None, optional): The seperator to use if `values` is a list. Defaults to " ".
            end (str | None, optional): The end of the line. Defaults to "\n".
            config (_type_, optional): The configuration. Defaults to {"color": defaultColor, "start": "|"}.
        """
        if len(config["start"]) <= 1:
            config["start"] += " "*(2-len(config["start"]))
        if type(values[0]) == list: text = sep.join(values[0])
        else: text = sep.join(values)
        if str(config["start"]).endswith(" "):
            text += " "
        values = colored(config["start"], config["color"]) + text + colored("-"*(os.get_terminal_size().columns-len(text)-len(config["start"])), config["color"])
        print(values, end=end)
    def fline(self, config: dict = {"color": defaultColor, "start": "+"}) -> None:
        """Prints a line to seperate the terminal

        Args:
            config (_type_, optional): The configuration. Defaults to {"color": defaultColor, "start": "|"}.
        """
        text = colored(config["start"] + "-"*(os.get_terminal_size().columns-len(config["start"])), config["color"])
        print(text)
    def finput(self, __prompt: object = "", config: dict = {"color": defaultColor, "start": "|"}) -> str:
        """Asks the user for an input in MegaShell style.

        

        Args:
            __prompt (object, optional): The text to show before the input. Defaults to "".
            config (_type_, optional): The configuration. Defaults to {"color": defaultColor, "start": "|"}.

        Returns:
            str: The users input.
        """
        if len(config["start"]) <= 1:
            config["start"] += " "*(2-len(config["start"]))
        text = colored(config["start"], config["color"]) + str(__prompt)
        return input(text)
    def fhinput(self, __prompt: object = "", config: dict = {"color": defaultColor, "start": "|"}) -> str:
        """Asks for a hidden input in MegaShell style.

        Args:
            __prompt (object, optional): The text to show before the input. Defaults to "".
            config (_type_, optional): The configuration. Defaults to {"color": defaultColor, "start": "|"}.

        Returns:
            str: The users input.
        """
        if len(config["start"]) <= 1:
            config["start"] += " "*(2-len(config["start"]))
        text = colored(config["start"], config["color"]) + str(__prompt)
        return getpass.getpass(text)
    def fpause(self, value: object = colored("Press enter to continue... ", attrs=["dark"]), config: dict = {"color": defaultColor, "start": "|"}) -> None:
        """Waits for the user pressing enter.

        Args:
            value (object, optional): The text to show before the input. Defaults to colored("Press enter to continue... ", attrs=["dark"]).
            config (_type_, optional): The configuration. Defaults to {"color": defaultColor, "start": "|"}.
        """
        if value == colored("Press enter to continue... ", attrs=["dark"]) and not os.name == "nt":
            value = colored("(Press enter to continue...) ")
            config["start"] = ">"
            config["color"] = "red"
        self.fhinput(value, config)
tools = __tools()

class __outputLibrary:
    def info(self, text: str, config: dict = {"color": "blue", "start": "|"}) -> None:
        """Prints a info message.

        Args:
            text (str): The text to print.
            config (_type_, optional): The configuration. Defaults to {"color": defaultColor, "start": "|"}.
        """
        tools.fprint(colored("Info: ", config["color"]) + text, config=config)
    def warn(self, text: str, config: dict = {"color": "yellow", "start": "|"}) -> None:
        """Prints a warning

        Args:
            text (str): The text to print.
            config (_type_, optional): The configuration. Defaults to {"color": defaultColor, "start": "|"}.
        """
        tools.fprint(colored("Warning: ", config["color"]) + text, config=config)
    def error(self, text: str, config: dict = {"color": "red", "start": "|"}) -> None:
        """Prints an error

        Args:
            text (str): The text to print.
            config (_type_, optional): The configuration. Defaults to {"color": defaultColor, "start": "|"}.
        """
        tools.fprint(colored("Error: ", config["color"]) + text, config=config)
    def shortText(self, text: str, extra: int = 0) -> str:
        """Cuts the text so it fits into the terminal.

        Args:
            text (str): The text to give back.
            extra (int, optional): The number of characters to calculate in. Defaults to 0.

        Returns:
            str: The short text. 
        """
        __sice = os.get_terminal_size().columns-5-extra
        return text[:__sice] + (text[__sice:] and '...')
    def restore(self, endline = True) -> None:
        """Recreates the console to it's beginning state.

        Args:
            endline (bool, optional): If a line at the end should be drawn. Defaults to True.
        """
        console.clear()
        console.setTitleBase("MegaShell")

        tools.fprintTitle("MegaShell")
        tools.fprint("(c) " + str(datetime.date.today().year) + " MegaShell, all rights reserved.")
        tools.fprint("For help type 'help'; for exit type 'exit'.")
        if endline:
            tools.fline()
    def removeLastLine(self, size: int = os.get_terminal_size().columns) -> None:
        """Deletes the last printed characters.

        Args:
            size (int, optional): The size of the deleted characters. Defaults to os.get_terminal_size().columns.
        """
        print("\033[A{}\033[A".format(' '*size))
outputLibrary = __outputLibrary()

class __console:
    def clear(self) -> None:
        """Clears the console.
        """
        if os.name == "nt":
            os.system("cls")
        else:
            os.system("clear")
    def setTitle(self, title: str) -> None:
        """Sets the title of the console.

        Args:
            title (str): The new title
        """
        if os.name == 'nt':  # Windows
            try:
                os.system(f"title {title}")
            except:
                pass
        else:  # Linux or macOS
            sys.stdout.write(f"\x1b]2;{title}\x07")
    baseTitle = ""
    def setTitleSub(self, title: str, sep: str = " - ", base: str | None = None) -> None:
        """Sets the subtitle of the console. If no base is given the attribute `base` is print.

        Args:
            title (str): The new subtitle
            sep (str, optional): The seperator between the title and basetitle. Defaults to " - ".
            base (str | None, optional): The base. If none the last base is used. Defaults to None.
        """
        if not base is None:
            self.baseTitle = base
        self. setTitle(title + sep + self.baseTitle)
    def setTitleBase(self, base: str | None = None) -> None:
        """Sets the base title.

        Args:
            base (str | None, optional): New base title. Defaults to None.
        """
        if not base is None:
            self.baseTitle = base
        self.setTitle(self.baseTitle)
console = __console()

class __system:
    def exit(self, code: int = 0) -> None:
        """Exits the program.

        Args:
            code (int, optional): The exit code. Defaults to 0.
        """
        sys.exit(code)
    def color(self) -> str:
        """Returns the color of the system in MegaShell style.

        Returns:
            str: The color of the system.
        """
        __sys = info.SYSTEM
        if __sys == "Windows":
            return "cyan"
        elif __sys == "Linux":
            return "red"
        elif __sys == "Darwin":
            return "magenta"
    def path(self) -> str:
        """Get the current working directory.

        Returns:
            str: The working directory.
        """
        return os.getcwd().strip()
    def friendlyPath(self) -> str:
        """Shorts the name.

        Returns:
            str: The new path.
        """
        __user = getpass.getuser()
        __path = self.path()
        __path = __path.replace("\\", "/")
        __path = re.sub(r".*?" + __user, "", __path, 1)
        __path = str(__path).replace("Desktop", "dt")
        __path = __path.removeprefix("/").removesuffix("/")
        if __path == "":
            __path = "/"
        return __path
system = __system()

class __commands:
    commands = {}
    commands_meta = {}
    def command(self, func):
        """Usage as decorator. Ads a function to the command list.

        Args:
            func (_type_): The function.
        """
        self.commands[str(func.__name__).removeprefix("c_")] = func
        self.commands_meta[str(func.__name__).removeprefix("c_")] = {"doc": str(func.__doc__).split(","), "attr": func.__dir__()}
    def get(self, name: str) -> object:
        """Returns a specific function.

        Args:
            name (str): The name of the function.

        Returns:
            object: The function.
        """
        return self.commands[name]
    def getMeta(self, name: str) -> dict:
        """Returns the meta info of a function.

        Args:
            name (str): The name of the function.

        Returns:
            dict: The meta info.
        """
        return self.commands_meta[name]
commands = __commands()
class __constants:
    constants = {}
    def constant(self, name: str | list, value: str):
        """Ads a value to the constants list.

        Args:
            name (str | list): The name of the constant.
            value (str): The value of the constant.
        """
        if type(name) == str:
            self.constants[name.lower()] = value
            self.constants[name.upper()] = value
        else:
            for names in name:
                self.constants[names.lower()] = value
                self.constants[names.upper()] = value
    def get(self, name: str) -> object:
        """Returns a specific value.

        Args:
            name (str): The name of the constant.

        Returns:
            object: The value.
        """
        return self.constants[name]
constants = __constants()
