from files import internal as i
from files.internal import commands as c
from files.internal import outputLibrary as ol
from files.internal import console as con
from files.internal import tools as t
from files.commandtools import commandtools as ct

os = i.os
colored = i.colored
import subprocess
from time import sleep as wait

@c.command
def c_reset(*extra):
    """v1"""
    ol.restore(False)
@c.command
def c_clear(*extra):
    """v1"""
    con.clear()
@c.command
def c_wait(*extra):
    """v1,disable"""
    t.fpause()

@c.command
def c_cd(*extra):
    """v1"""
    os.chdir(os.path.abspath(str(extra[0]).replace("dt", "Desktop")))
@c.command
def c_ld(*extra):
    """v1"""
    __files = os.listdir(os.getcwd())
    for i in __files:
        if os.path.isfile(os.path.abspath(i)) == True: __color = "cyan"
        else: __color = "green"
        t.fprint(colored(i, __color), config={"color": t.defaultColor,"start": "|-> "})
@c.command
def c_start(file = "", **extra):
    """v2"""
    file = ct.parse(extra, file)
    file = os.path.abspath(file)
    try: os.startfile(str(file))
    except: subprocess.Popen(["xdg-open", file], stdout=subprocess.DEVNULL,  stderr=subprocess.STDOUT)
    wait(0.1)
@c.command
def c_wait(time = "", **extra):
    """v2"""
    time = ct.parse(extra, time)
    wait(float(time))
@c.command
def c_pause(*extra):
    """v1"""
    t.fpause()

@c.command
def c_getCommandMeta(*extra):
    """v1"""
    t.fprint(str(c.getMeta(extra[0])), config={"color": t.defaultColor,"start": "|-> "})
