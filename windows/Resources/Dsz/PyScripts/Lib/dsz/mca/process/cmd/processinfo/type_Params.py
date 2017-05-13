# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.6.0b2 (default, Oct 11 2016, 05:27:10) 
# [GCC 6.2.0 20161005]
# Embedded file name: type_Params.py
from types import *
PARAMS_FLAG_ELEVATE = 1
PARAMS_FLAG_HASH_MODULES = 2

class Params:

    def __init__(self):
        self.__dict__['id'] = 0
        self.__dict__['flags'] = 0

    def __getattr__(self, name):
        if name == 'id':
            return self.__dict__['id']
        if name == 'flags':
            return self.__dict__['flags']
        raise AttributeError("Attribute '%s' not found" % name)

    def __setattr__(self, name, value):
        if name == 'id':
            self.__dict__['id'] = value
        elif name == 'flags':
            self.__dict__['flags'] = value
        else:
            raise AttributeError("Attribute '%s' not found" % name)

    def Marshal(self, mmsg):
        from mcl.object.Message import MarshalMessage
        submsg = MarshalMessage()
        submsg.AddU32(MSG_KEY_PARAMS_ID, self.__dict__['id'])
        submsg.AddU32(MSG_KEY_PARAMS_FLAGS, self.__dict__['flags'])
        mmsg.AddMessage(MSG_KEY_PARAMS, submsg)

    def Demarshal(self, dmsg, instance=-1):
        import mcl.object.Message
        msgData = dmsg.FindData(MSG_KEY_PARAMS, mcl.object.Message.MSG_TYPE_MSG, instance)
        submsg = mcl.object.Message.DemarshalMessage(msgData)
        self.__dict__['id'] = submsg.FindU32(MSG_KEY_PARAMS_ID)
        self.__dict__['flags'] = submsg.FindU32(MSG_KEY_PARAMS_FLAGS)