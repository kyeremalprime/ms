# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.6.0b2 (default, Oct 11 2016, 05:27:10) 
# [GCC 6.2.0 20161005]
# Embedded file name: type_Params.py
from types import *

class Params:

    def __init__(self):
        self.__dict__['action'] = 0
        self.__dict__['variable'] = ''
        self.__dict__['value'] = ''

    def __getattr__(self, name):
        if name == 'action':
            return self.__dict__['action']
        if name == 'variable':
            return self.__dict__['variable']
        if name == 'value':
            return self.__dict__['value']
        raise AttributeError("Attribute '%s' not found" % name)

    def __setattr__(self, name, value):
        if name == 'action':
            self.__dict__['action'] = value
        elif name == 'variable':
            self.__dict__['variable'] = value
        elif name == 'value':
            self.__dict__['value'] = value
        else:
            raise AttributeError("Attribute '%s' not found" % name)

    def Marshal(self, mmsg):
        from mcl.object.Message import MarshalMessage
        submsg = MarshalMessage()
        submsg.AddU8(MSG_KEY_PARAMS_ACTION, self.__dict__['action'])
        submsg.AddStringUtf8(MSG_KEY_PARAMS_VARIABLE, self.__dict__['variable'])
        submsg.AddStringUtf8(MSG_KEY_PARAMS_VALUE, self.__dict__['value'])
        mmsg.AddMessage(MSG_KEY_PARAMS, submsg)

    def Demarshal(self, dmsg, instance=-1):
        import mcl.object.Message
        msgData = dmsg.FindData(MSG_KEY_PARAMS, mcl.object.Message.MSG_TYPE_MSG, instance)
        submsg = mcl.object.Message.DemarshalMessage(msgData)
        self.__dict__['action'] = submsg.FindU8(MSG_KEY_PARAMS_ACTION)
        self.__dict__['variable'] = submsg.FindString(MSG_KEY_PARAMS_VARIABLE)
        try:
            self.__dict__['value'] = submsg.FindString(MSG_KEY_PARAMS_VALUE)
        except:
            pass