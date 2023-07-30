from files.internal import commands as c
from files.internal import outputLibrary as ol
from files.internal import tools as t

@c.command
def c_help(*extra):
    """v1"""
    t.fprint("MegaShell Help Menu")
    t.fprint("")
    ol.error("/!\\ This command is not yet implemented! /!\\")
    ol.warn("This program is still in development! We are not liable for any damages!")