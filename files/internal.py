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
info = __info()

class __tools:
    defaultColor = "blue"
    def __init__(self, defaultColor: str = "blue") -> None:
        self.defaultColor = defaultColor
    def fprint(self, *values: object, sep: str | None = " ", end: str | None = "\n", config: dict = {"color": defaultColor, "start": "|"}) -> None:
        if len(config["start"]) <= 1:
            config["start"] += " "*(2-len(config["start"]))
        if type(values[0]) == list: text = sep.join(values[0])
        else: text = sep.join(values)
        values = colored(config["start"], config["color"]) + text
        print(values, end=end)
    def fprintTitle(self, *values: object, sep: str | None = " ", end: str | None = "\n", config: dict = {"color": defaultColor, "start": "+- "}) -> None:
        if len(config["start"]) <= 1:
            config["start"] += " "*(2-len(config["start"]))
        if type(values[0]) == list: text = sep.join(values[0])
        else: text = sep.join(values)
        if str(config["start"]).endswith(" "):
            text += " "
        values = colored(config["start"], config["color"]) + text + colored("-"*(os.get_terminal_size().columns-len(text)-len(config["start"])), config["color"])
        print(values, end=end)
    def fline(self, config: dict = {"color": defaultColor, "start": "+"}) -> None:
        text = colored(config["start"] + "-"*(os.get_terminal_size().columns-len(config["start"])), config["color"])
        print(text)
    def finput(self, __prompt: object = "", config: dict = {"color": defaultColor, "start": "|"}) -> str:
        if len(config["start"]) <= 1:
            config["start"] += " "*(2-len(config["start"]))
        text = colored(config["start"], config["color"]) + str(__prompt)
        return input(text)
    def fhinput(self, __prompt: object = "", config: dict = {"color": defaultColor, "start": "|"}) -> str:
        if len(config["start"]) <= 1:
            config["start"] += " "*(2-len(config["start"]))
        text = colored(config["start"], config["color"]) + str(__prompt)
        return getpass.getpass(text)
    def fpause(self, value: object = colored("Press enter to continue... ", attrs=["dark"]), config: dict = {"color": defaultColor, "start": "|"}) -> None:
        if value == colored("Press enter to continue... ", attrs=["dark"]) and not os.name == "nt":
            value = colored("(Press enter to continue...) ")
            config["start"] = ">"
            config["color"] = "red"
        self.fhinput(value, config)
tools = __tools()

class __outputLibrary:
    def info(self, text: str, config: dict = {"color": "blue", "start": "|"}) -> None:
        tools.fprint(colored("Info: ", config["color"]) + text, config=config)
    def warn(self, text: str, config: dict = {"color": "yellow", "start": "|"}) -> None:
        tools.fprint(colored("Warning: ", config["color"]) + text, config=config)
    def error(self, text: str, config: dict = {"color": "red", "start": "|"}) -> None:
        tools.fprint(colored("Error: ", config["color"]) + text, config=config)
    def shortText(self, text: str, extra: int = 0) -> str:
        __sice = os.get_terminal_size().columns-5-extra
        return text[:__sice] + (text[__sice:] and '...')
    def restore(self, endline = True):
        console.clear()
        console.setTitleBase("MegaShell")

        tools.fprintTitle("MegaShell")
        tools.fprint("(c) " + str(datetime.date.today().year) + " MegaShell, all rights reserved.")
        tools.fprint("For help type 'help'; for exit type 'exit'.")
        if endline:
            tools.fline()
outputLibrary = __outputLibrary()

class __console:
    def clear(self) -> None:
        if os.name == "nt":
            os.system("cls")
        else:
            os.system("clear")
    def setTitle(self, title: str) -> None:
        if os.name == 'nt':  # Windows
            try:
                os.system(f"title {title}")
            except:
                pass
        else:  # Linux or macOS
            sys.stdout.write(f"\x1b]2;{title}\x07")
    baseTitle = ""
    def setTitleSub(self, title: str, sep: str = " - ", base: str | None = None) -> None:
        if not base is None:
            self.baseTitle = base
        self. setTitle(title + sep + self.baseTitle)
    def setTitleBase(self, base: str | None = None) -> None:
        if not base is None:
            self.baseTitle = base
        self.setTitle(self.baseTitle)
console = __console()

class __system:
    def exit(self, code: int = 0) -> None:
        sys.exit(code)
    def color(self) -> str:
        __sys = platform.system()
        if __sys == "Windows":
            return "cyan"
        elif __sys == "Linux":
            return "red"
        elif __sys == "Darwin":
            return "magenta"
    def path(self) -> str:
        return os.getcwd().strip()
    def friendlyPath(self) -> str:
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
        self.commands[str(func.__name__).removeprefix("c_")] = func
        self.commands_meta[str(func.__name__).removeprefix("c_")] = {"doc": str(func.__doc__).split(","), "annotations": func.__annotations__}
    def get(self, name: str) -> object:
        return self.commands[name]
    def getMeta(self, name: str) -> dict:
        return self.commands_meta[name]
commands = __commands()
