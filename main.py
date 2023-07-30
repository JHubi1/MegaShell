# MegaShell

import dotenv
import sys
from termcolor import colored
from time import sleep as wait
import yaml
import glob
import importlib

dotenv.load_dotenv()

from files import internal as i
from files.internal import info as inf
from files.internal import tools as t
from files.internal import console as con
from files.internal import outputLibrary as ol
from files.internal import system as s
from files.internal import commands as c
from files.argparser import argparser as a
from files.commandtools import commandtools as ct
from files import debugger as d

app = {
    "version": inf.VERSION,
}

if "--nocolor" in sys.argv:
    def colored(text, *arg): return text
    i.colored = colored
    d.colored = colored

# ,disable

# Declaring commands
# Import from folder
files = glob.glob("commands/*.py")
for file in files:
    modulname = file[:-3].replace('/', '.')
    modul = importlib.import_module(modulname.replace("\\", "/").replace("/", "."))
# Import from folder end
@c.command
def c_echo(*text):
    """v1"""
    t.fprint(*text)
@c.command
def c_test(a="", b="", **extra):
    """v2"""
    a, b = ct.parse(extra, a, b)
    t.fprint("a: " + a)
    t.fprint("b: " + b)
@c.command
def c_exit(*extra):
    """v1"""
    sys.exit()
# Declaring commands end

def run_command(name: str, args: list | tuple):
    con.setTitleSub(name)
    if type(args) == dict: c.commands[name](**args)
    # deepcode ignore DictPassedAsArgs: works as intended
    else: c.commands[name](*args)
    con.setTitleBase()

ol.restore()

while True:
    try: ui = t.finput(colored("<", s.color()) + colored(s.friendlyPath(), "yellow") + colored("> ", s.color())).strip()
    except: pass

    if ui != "":
        commands = ui.split(" && ")
        for command in commands:
            runCommand = command.split(" ")
            runCommandName = runCommand.pop(0)
            runCommandArgs = runCommand

            if runCommandName in c.commands:
                if "disable" in c.commands_meta[runCommandName]["doc"]:
                    ol.error("Command '" + ol.shortText(runCommandName, 30) + "' is disabled.")
                    t.fline()
                    continue
                finishedText = {}
                if "v1" in c.commands_meta[runCommandName]["doc"]:
                    finishedText = tuple(runCommandArgs)
                elif "v2" in c.commands_meta[runCommandName]["doc"]:
                    finishedText, otherArguments = a.parse(runCommandArgs)
                    runCommandArgs.pop(len(runCommandArgs) - 1)
                    finishedText["extra"] = otherArguments
                # if True:
                try:
                    run_command(runCommandName, finishedText)
                except KeyError as e:
                    ol.error("KeyError: " + colored(str(e), "magenta") + " is not a wanted argument.") 
                except TypeError as e:
                    error = str(e)
                    if error == "cannot unpack non-iterable bool object":
                        ol.error("TypeError: A wanted argument is not given.")
                    else:
                        ol.error("TypeError: " + colored(str(e), "magenta"))
                except ValueError as e:
                    ol.error("ValueError: " + colored(str(e), "magenta"))
                except Exception as e:
                   error = str(e)
                   if error == "tuple index out of range": error = "Too few arguments given."
                   ol.error("An error has occured during execution: " + colored(error, "magenta"))
            else:
                ol.error("Command '" + ol.shortText(runCommandName, 30) + "' not found.")
        t.fline()

con.clear()