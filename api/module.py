# -*- coding: utf-8 -*-
from pydoc import ModuleScanner

names = []


def callback(path, modname, desc, modules=names):
    if modname and modname[-9:] == '.__init__':
        modname = modname[:-9]
    if modname.find('.') < 0 and modname not in modules:
        modules.append(modname)


def onerror(modname):
    callback(None, modname, None)


ModuleScanner().run(callback, onerror=onerror)