# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.6.0b2 (default, Oct 11 2016, 05:27:10) 
# [GCC 6.2.0 20161005]
# Embedded file name: commands.py
"""Execute shell commands via os.popen() and return status, output.

Interface summary:

       import commands

       outtext = commands.getoutput(cmd)
       (exitstatus, outtext) = commands.getstatusoutput(cmd)
       outtext = commands.getstatus(file)  # returns output of "ls -ld file"

A trailing newline is removed from the output string.

Encapsulates the basic operation:

      pipe = os.popen('{ ' + cmd + '; } 2>&1', 'r')
      text = pipe.read()
      sts = pipe.close()

 [Note:  it would be nice to add functions to interpret the exit status.]
"""
from warnings import warnpy3k
warnpy3k('the commands module has been removed in Python 3.0; use the subprocess module instead', stacklevel=2)
del warnpy3k
__all__ = [
 'getstatusoutput', 'getoutput', 'getstatus']

def getstatus(file):
    """Return output of "ls -ld <file>" in a string."""
    import warnings
    warnings.warn('commands.getstatus() is deprecated', DeprecationWarning, 2)
    return getoutput('ls -ld' + mkarg(file))


def getoutput(cmd):
    """Return output (stdout or stderr) of executing cmd in a shell."""
    return getstatusoutput(cmd)[1]


def getstatusoutput(cmd):
    """Return (status, output) of executing cmd in a shell."""
    import os
    pipe = os.popen('{ ' + cmd + '; } 2>&1', 'r')
    text = pipe.read()
    sts = pipe.close()
    if sts is None:
        sts = 0
    if text[-1:] == '\n':
        text = text[:-1]
    return (
     sts, text)


def mk2arg(head, x):
    import os
    return mkarg(os.path.join(head, x))


def mkarg(x):
    if "'" not in x:
        return " '" + x + "'"
    s = ' "'
    for c in x:
        if c in '\\$"`':
            s = s + '\\'
        s = s + c

    s = s + '"'
    return s