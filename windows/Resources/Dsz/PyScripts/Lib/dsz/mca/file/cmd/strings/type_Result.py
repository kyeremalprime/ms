# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.6.0b2 (default, Oct 11 2016, 05:27:10) 
# [GCC 6.2.0 20161005]
# Embedded file name: type_Result.py
from types import *

class Result:

    def __init__(self):
        self.__dict__['offset'] = 0
        self.__dict__['value'] = ''

    def __getattr__(self, name):
        if name == 'offset':
            return self.__dict__['offset']
        if name == 'value':
            return self.__dict__['value']
        raise AttributeError("Attribute '%s' not found" % name)

    def __setattr__(self, name, value):
        if name == 'offset':
            self.__dict__['offset'] = value
        elif name == 'value':
            self.__dict__['value'] = value
        else:
            raise AttributeError("Attribute '%s' not found" % name)

    def Marshal(self, mmsg):
        from mcl.object.Message import MarshalMessage
        submsg = MarshalMessage()
        submsg.AddU64(MSG_KEY_RESULT_OFFSET, self.__dict__['offset'])
        submsg.AddStringUtf8(MSG_KEY_RESULT_VALUE, self.__dict__['value'])
        mmsg.AddMessage(MSG_KEY_RESULT, submsg)

    def Demarshal(self, dmsg, instance=-1):
        import mcl.object.Message
        msgData = dmsg.FindData(MSG_KEY_RESULT, mcl.object.Message.MSG_TYPE_MSG, instance)
        submsg = mcl.object.Message.DemarshalMessage(msgData)
        self.__dict__['offset'] = submsg.FindU64(MSG_KEY_RESULT_OFFSET)
        self.__dict__['value'] = submsg.FindString(MSG_KEY_RESULT_VALUE)