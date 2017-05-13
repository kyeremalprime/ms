# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.6.0b2 (default, Oct 11 2016, 05:27:10) 
# [GCC 6.2.0 20161005]
# Embedded file name: type_Params.py
from types import *

class Params:

    def __init__(self):
        self.__dict__['parentId'] = 0
        self.__dict__['command'] = ''
        self.__dict__['memoryProvider'] = 0
        self.__dict__['threadProvider'] = 0

    def __getattr__(self, name):
        if name == 'parentId':
            return self.__dict__['parentId']
        if name == 'command':
            return self.__dict__['command']
        if name == 'memoryProvider':
            return self.__dict__['memoryProvider']
        if name == 'threadProvider':
            return self.__dict__['threadProvider']
        raise AttributeError("Attribute '%s' not found" % name)

    def __setattr__(self, name, value):
        if name == 'parentId':
            self.__dict__['parentId'] = value
        elif name == 'command':
            self.__dict__['command'] = value
        elif name == 'memoryProvider':
            self.__dict__['memoryProvider'] = value
        elif name == 'threadProvider':
            self.__dict__['threadProvider'] = value
        else:
            raise AttributeError("Attribute '%s' not found" % name)

    def Marshal(self, mmsg):
        from mcl.object.Message import MarshalMessage
        submsg = MarshalMessage()
        submsg.AddU32(MSG_KEY_PARAMS_PARENT_PROCESS_ID, self.__dict__['parentId'])
        submsg.AddStringUtf8(MSG_KEY_PARAMS_COMMAND, self.__dict__['command'])
        submsg.AddU32(MSG_KEY_PARAMS_MEMORY_PROVIDER, self.__dict__['memoryProvider'])
        submsg.AddU32(MSG_KEY_PARAMS_INJECT_PROVIDER, self.__dict__['threadProvider'])
        mmsg.AddMessage(MSG_KEY_PARAMS, submsg)

    def Demarshal(self, dmsg, instance=-1):
        import mcl.object.Message
        msgData = dmsg.FindData(MSG_KEY_PARAMS, mcl.object.Message.MSG_TYPE_MSG, instance)
        submsg = mcl.object.Message.DemarshalMessage(msgData)
        self.__dict__['parentId'] = submsg.FindU32(MSG_KEY_PARAMS_PARENT_PROCESS_ID)
        self.__dict__['command'] = submsg.FindString(MSG_KEY_PARAMS_COMMAND)
        try:
            self.__dict__['memoryProvider'] = submsg.FindU32(MSG_KEY_PARAMS_MEMORY_PROVIDER)
        except:
            pass

        try:
            self.__dict__['threadProvider'] = submsg.FindU32(MSG_KEY_PARAMS_INJECT_PROVIDER)
        except:
            pass