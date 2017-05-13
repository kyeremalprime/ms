# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.6.0b2 (default, Oct 11 2016, 05:27:10) 
# [GCC 6.2.0 20161005]
# Embedded file name: __init__.py


def CheckValue(name, globalValue=False):
    import mcl_platform.tasking.env
    return mcl_platform.tasking.env.CheckValue(name, globalValue)


def DeleteValue(name, globalValue=False):
    import mcl_platform.tasking.env
    mcl_platform.tasking.env.DeleteValue(name, globalValue)


def GetValue(name, globalValue=False):
    import mcl_platform.tasking.env
    return mcl_platform.tasking.env.GetValue(name, globalValue)


def IsTrue(name, globalValue=False):
    import mcl_platform.tasking.env
    if mcl_platform.tasking.env.CheckValue(name, globalValue):
        value = mcl_platform.tasking.env.GetValue(name, globalValue).lower()
        if value == 'true' or value == 'on' or value == 'yes' or value == '1':
            return True
    return False


def SetValue(name, value, globalValue=False):
    import mcl_platform.tasking.env
    mcl_platform.tasking.env.SetValue(name, value, globalValue)