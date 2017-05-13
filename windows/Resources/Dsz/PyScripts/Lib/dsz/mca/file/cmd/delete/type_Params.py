# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.6.0b2 (default, Oct 11 2016, 05:27:10) 
# [GCC 6.2.0 20161005]
# Embedded file name: type_Params.py
from types import *
PARAMS_FLAG_AFTER_REBOOT = 1
PARAMS_FLAG_SHRED = 2

class Params:

    def __init__(self):
        self.__dict__['flags'] = 0
        self.__dict__['path'] = ''
        self.__dict__['mask'] = ''
        self.__dict__['provider'] = 0
        self.__dict__['maxEntries'] = -1

    def __getattr__(self, name):
        if name == 'flags':
            return self.__dict__['flags']
        if name == 'path':
            return self.__dict__['path']
        if name == 'mask':
            return self.__dict__['mask']
        if name == 'provider':
            return self.__dict__['provider']
        if name == 'maxEntries':
            return self.__dict__['maxEntries']
        raise AttributeError("Attribute '%s' not found" % name)

    def __setattr__(self, name, value):
        if name == 'flags':
            self.__dict__['flags'] = value
        elif name == 'path':
            self.__dict__['path'] = value
        elif name == 'mask':
            self.__dict__['mask'] = value
        elif name == 'provider':
            self.__dict__['provider'] = value
        elif name == 'maxEntries':
            self.__dict__['maxEntries'] = value
        else:
            raise AttributeError("Attribute '%s' not found" % name)

    def Marshal(self, mmsg):
        from mcl.object.Message import MarshalMessage
        submsg = MarshalMessage()
        submsg.AddU16(MSG_KEY_PARAMS_FLAGS, self.__dict__['flags'])
        submsg.AddStringUtf8(MSG_KEY_PARAMS_PATH, self.__dict__['path'])
        submsg.AddStringUtf8(MSG_KEY_PARAMS_MASK, self.__dict__['mask'])
        submsg.AddU32(MSG_KEY_PARAMS_PROVIDER, self.__dict__['provider'])
        submsg.AddS32(MSG_KEY_PARAMS_MAX_ENTRIES, self.__dict__['maxEntries'])
        mmsg.AddMessage(MSG_KEY_PARAMS, submsg)

    def Demarshal(self, dmsg, instance=-1):
        import mcl.object.Message
        msgData = dmsg.FindData(MSG_KEY_PARAMS, mcl.object.Message.MSG_TYPE_MSG, instance)
        submsg = mcl.object.Message.DemarshalMessage(msgData)
        self.__dict__['flags'] = submsg.FindU16(MSG_KEY_PARAMS_FLAGS)
        self.__dict__['path'] = submsg.FindString(MSG_KEY_PARAMS_PATH)
        self.__dict__['mask'] = submsg.FindString(MSG_KEY_PARAMS_MASK)
        try:
            self.__dict__['provider'] = submsg.FindU32(MSG_KEY_PARAMS_PROVIDER)
        except:
            pass

        try:
            self.__dict__['maxEntries'] = submsg.FindS32(MSG_KEY_PARAMS_MAX_ENTRIES)
        except:
            pass