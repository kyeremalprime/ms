# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.6.0b2 (default, Oct 11 2016, 05:27:10) 
# [GCC 6.2.0 20161005]
# Embedded file name: type_Result.py
from types import *

class Result:

    def __init__(self):
        self.__dict__['logName'] = ''
        self.__dict__['target'] = ''

    def __getattr__(self, name):
        if name == 'logName':
            return self.__dict__['logName']
        if name == 'target':
            return self.__dict__['target']
        raise AttributeError("Attribute '%s' not found" % name)

    def __setattr__(self, name, value):
        if name == 'logName':
            self.__dict__['logName'] = value
        elif name == 'target':
            self.__dict__['target'] = value
        else:
            raise AttributeError("Attribute '%s' not found" % name)

    def Marshal(self, mmsg):
        from mcl.object.Message import MarshalMessage
        submsg = MarshalMessage()
        submsg.AddStringUtf8(MSG_KEY_RESULT_LOG, self.__dict__['logName'])
        submsg.AddStringUtf8(MSG_KEY_RESULT_TARGET, self.__dict__['target'])
        mmsg.AddMessage(MSG_KEY_RESULT, submsg)

    def Demarshal(self, dmsg, instance=-1):
        import mcl.object.Message
        msgData = dmsg.FindData(MSG_KEY_RESULT, mcl.object.Message.MSG_TYPE_MSG, instance)
        submsg = mcl.object.Message.DemarshalMessage(msgData)
        self.__dict__['logName'] = submsg.FindString(MSG_KEY_RESULT_LOG)
        try:
            self.__dict__['target'] = submsg.FindString(MSG_KEY_RESULT_TARGET)
        except:
            pass