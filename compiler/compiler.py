import os
import sys
from termcolor import colored
from getpass import getpass
from re import match
from platform import system
import shlex
import keyboard
import time

sys.path.append(os.path.abspath("../files"))
from internal import info as inf

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

clear()

def fprint(*values: object, sep: str | None = " ", end: str | None = "\n", config: dict = {"color": "blue", "start": "|"}) -> None:
    if len(config["start"]) <= 1:
        config["start"] += " "*(2-len(config["start"]))
    if type(values[0]) == list: text = sep.join(values[0])
    else: text = sep.join(values)
    values = colored(config["start"], config["color"]) + text
    print(values, end=end)
def fprintTitle(*values: object, sep: str | None = " ", end: str | None = "\n", config: dict = {"color": "blue", "start": "+- "}) -> None:
    if len(config["start"]) <= 1:
        config["start"] += " "*(2-len(config["start"]))
    if type(values[0]) == list: text = sep.join(values[0])
    else: text = sep.join(values)
    if str(config["start"]).endswith(" "):
        text += " "
    values = colored(config["start"], config["color"]) + text + colored("-"*(os.get_terminal_size().columns-len(text)-len(config["start"])), config["color"])
    print(values, end=end)
def fline(config: dict = {"color": "blue", "start": "+"}) -> None:
    text = colored(config["start"] + "-"*(os.get_terminal_size().columns-len(config["start"])), config["color"])
    print(text)
def finput(__prompt: object = "", config: dict = {"color": "blue", "start": "|"}) -> str:
    if len(config["start"]) <= 1:
        config["start"] += " "*(2-len(config["start"]))
    text = colored(config["start"], config["color"]) + str(__prompt)
    return input(text)
def fpause(value: object = colored("Press enter to continue... ", attrs=["dark"]), config: dict = {"color": "blue", "start": "|"}) -> None:
        if value == colored("Press enter to continue... ", attrs=["dark"]) and not os.name == "nt":
            value = colored("(Press enter to continue...) ")
            config["start"] = ">"
            config["color"] = "red"
        if len(config["start"]) <= 1:
            config["start"] += " "*(2-len(config["start"]))
        text = colored(config["start"], config["color"]) + str(value)
        return getpass(text)


# << MAIN CODE >>

fprintTitle("MegaShell Compiler")
fprint("Made by: @JHubi1 (GitHub)")
fprint("Version: 1.0.0")
fline()
appVersion = ""
while not match(r"[0-9]\.[0-9]\.[0-9](?:-)?[a-zA-Z]{0,10}", appVersion):
    keyboard.write(inf.VERSION)
    appVersion = finput(colored("Enter the version of the app: ", "yellow"))
path = os.path.abspath(os.getcwd() + "/output/" + appVersion + "/" + system().lower())
# file deepcode ignore UpdateAPI: input from user; user = dev
if os.path.exists(path):
    fline()
    fprint("The directory already exists!")
    if finput("Continue? [y/N]: ").lower() == "y":
        fprint("Continuing...")
    else:
        fprint("Aborting...")
        fpause()
        exit()
os.makedirs(path, exist_ok=True)
# file deepcode ignore PT: input from user; user = dev
os.chdir(path)

start_time = time.time()

commands = [
    'pyinstaller --noconfirm --onedir --console --icon "' + os.path.abspath("../../../../images/^logos/logo.ico") + '" --name "MegaShell" --add-data "' + os.path.abspath("../../../../commands") + ';commands" --add-data "' + os.path.abspath("../../../../config") + ';config" "' + os.path.abspath("../../../../main.py") + '";;;pyinstaller --noconfirm --onedir --console --name "MegaShell" --add-data "' +  shlex.quote(os.path.abspath("../../../../commands")) + ';commands" --add-data "' +  shlex.quote(os.path.abspath("../../../../config")) + ';config" "' +  shlex.quote(os.path.abspath("../../../../main.py")) + '"',

    'xcopy /E /I /Y "' + os.path.abspath("dist/MegaShell") + '" "' + os.path.abspath("MegaShell") + '";;;cp -R ' + os.path.abspath("dist/MegaShell") + ' ' + os.path.abspath("MegaShell"),
    'del /F "' + os.path.abspath("MegaShell.spec") + '";;;rm "' + os.path.abspath("MegaShell.spec") + '"',
    'rmdir /S /Q "' + os.path.abspath("dist") + '";;;rm -rf "' + os.path.abspath("dist") + '"',
    'rmdir /S /Q "' + os.path.abspath("build") + '";;;rm -rf "' + os.path.abspath("build") + '"',

    # IMPORTANT: ISCC must be in path!
    'ISCC /O+ /DMyAppVersion="' + appVersion + '" "' + os.path.abspath("../../../installer/windows/MegaShellSetup.iss") + '";;;echo Installer creation not supported in Linux.'
]

fline()
for command in commands:
    command = command.split(";;;")
    if len(command) != 1:
        if system().lower() == "windows":
            command = command[0]
        elif system().lower() == "linux":
            command = command[1]
    else: command = command[0]
    print(colored("Executing: `" + command + "`", "green"))
    # deepcode ignore CommandInjection: commands from list
    os.system(command)
    fline()

end_time = time.time() - start_time

fprint("Compilation finished!")
fprint(colored("Total time: " + str(end_time) + "s", "green"))

fpause()
clear()
