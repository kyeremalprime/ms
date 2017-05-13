# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.6.0b2 (default, Oct 11 2016, 05:27:10) 
# [GCC 6.2.0 20161005]
# Embedded file name: __init__.py


def getErrorString(error):
    import winnt_system1_errors
    errorStr = winnt_system1_errors.getErrorString(error)
    if errorStr != None:
        return errorStr
    else:
        import winnt_system2_errors
        errorStr = winnt_system2_errors.getErrorString(error)
        if errorStr != None:
            return errorStr
        import winnt_wsa_errors
        errorStr = winnt_wsa_errors.getErrorString(error)
        if errorStr != None:
            return errorStr
        import winnt_net_errors
        errorStr = winnt_net_errors.getErrorString(error)
        if errorStr != None:
            return errorStr
        import winnt_wmi_errors
        errorStr = winnt_wmi_errors.getErrorString(error)
        if errorStr != None:
            return errorStr
        return