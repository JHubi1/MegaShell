from files.internal import info as inf
from files.internal import commands as c
from files.internal import outputLibrary as ol
from files.internal import tools as t
from files.help import info as hi

from termcolor import colored
import os

@c.command
def c_help(*extra):
    """v1"""
    t.fprint("<< MegaShell Help Menu >>")
    if len(extra) == 0:
        count = 0
        for i in hi.listAll():
            if count == 5:
                try:
                    t.fpause()
                except:
                    ol.removeLastLine()
                    t.fprint("Help menu cancelled.")
                    break
                ol.removeLastLine()
                count = 0
            text = hi.get(i)
            if text == "":
                if inf.SYSTEM == "windows":
                    text = colored("(No help text available)", attrs=["dark"])
                else:
                    text = colored("(No help text available)", "grey")
            t.fprint(colored(i, "yellow") + ": " + text, config={"color": t.defaultColor,"start": "|-> "})
            count += 1
    else:
        i = extra[0]
        text = hi.get(i)
        if text == "":
            if inf.SYSTEM == "windows":
                text = colored("(No help text available)", attrs=["dark"])
            else:
                text = colored("(No help text available)", "grey")
        t.fprint(colored(i, "yellow") + ": " + text, config={"color": t.defaultColor,"start": "|-> "})
