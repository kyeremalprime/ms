# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.6.0b2 (default, Oct 11 2016, 05:27:10) 
# [GCC 6.2.0 20161005]
# Embedded file name: D:\Development\Dsz_1.3.0\DevDisk\Resources\Dsz\PyScripts\Lib\dsz\lp\gui\terminal\__init__.py
# Compiled at: 2012-10-22 17:30:11
import dsz
import dsz.lp.alias
import dsz.lp.cmdline
import dsz.path
import dsz.version
import os
import re
import sys
import xml.dom.minidom

class NewTerminal:

    def __init__(self):
        self.bFocus = False
        self.bClose = False
        self.bDisable = False
        self.dst = dsz.script.Env['target_address']
        self.bDetach = False
        self.locX = 0
        self.locY = 0
        self.sizeWidth = 0
        self.sizeHeight = 0
        self.name = None
        self.command = None
        return

    def setDetach(self, width, height, x, y):
        self.bDetach = True
        self.locX = x
        self.locY = y
        self.sizeWidth = width
        self.sizeHeight = height
        return True

    def setLocation(self, x, y):
        self.bDetach = True
        self.locX = x
        self.locY = y
        return True

    def setSize(self, width, height):
        self.sizeWidth = width
        self.sizeHeight = height
        return True

    def setFocus(self, value=True):
        self.bFocus = value

    def setClose(self, value=True):
        self.bClose = value

    def setDisable(self, value=True):
        self.bDisable = value

    def setDestination(self, dest):
        self.dst = dest

    def setName(self, newName):
        self.name = newName

    def setCommand(self, cmd):
        self.command = cmd

    def spawn(self):
        cmd = 'gui -command ".newterm '
        if self.bFocus:
            cmd += '-focus '
        if self.bClose:
            cmd += '-close '
        if self.bDisable:
            cmd += '-disable '
        if self.bDetach:
            cmd += '-detach=%dx%d@%d,%d ' % (self.sizeWidth, self.sizeHeight, self.locX, self.locY)
        if self.dst != None:
            cmd += '-dst=%s ' % self.dst
        if self.name != None:
            cmd += '-name=\\"%s\\" ' % self.name
        if self.command != None:
            cmd += '-cmd=\\"%s\\" ' % self.command
        cmd += '"'
        return dsz.cmd.Run(cmd)