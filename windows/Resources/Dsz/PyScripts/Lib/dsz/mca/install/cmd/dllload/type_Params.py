# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.6.0b2 (default, Oct 11 2016, 05:27:10) 
# [GCC 6.2.0 20161005]
# Embedded file name: type_Params.py
from types import *
import array

class Params:

    def __init__(self):
        self.__dict__['chunkOffset'] = 0
        self.__dict__['totalSize'] = 0
        self.__dict__['ordinal'] = 0
        self.__dict__['exportName'] = ''
        self.__dict__['chunk'] = array.array('B')
        self.__dict__['pid'] = 0

    def __getattr__(self, name):
        if name == 'chunkOffset':
            return self.__dict__['chunkOffset']
        if name == 'totalSize':
            return self.__dict__['totalSize']
        if name == 'ordinal':
            return self.__dict__['ordinal']
        if name == 'exportName':
            return self.__dict__['exportName']
        if name == 'chunk':
            return self.__dict__['chunk']
        if name == 'pid':
            return self.__dict__['pid']
        raise AttributeError("Attribute '%s' not found" % name)

    def __setattr__(self, name, value):
        if name == 'chunkOffset':
            self.__dict__['chunkOffset'] = value
        elif name == 'totalSize':
            self.__dict__['totalSize'] = value
        elif name == 'ordinal':
            self.__dict__['ordinal'] = value
        elif name == 'exportName':
            self.__dict__['exportName'] = value
        elif name == 'chunk':
            self.__dict__['chunk'] = value
        elif name == 'pid':
            self.__dict__['pid'] = value
        else:
            raise AttributeError("Attribute '%s' not found" % name)

    def Marshal(self, mmsg):
        from mcl.object.Message import MarshalMessage
        submsg = MarshalMessage()
        submsg.AddU32(MSG_KEY_PARAMS_CHUNK_OFFSET, self.__dict__['chunkOffset'])
        submsg.AddU32(MSG_KEY_PARAMS_TOTAL_SIZE, self.__dict__['totalSize'])
        submsg.AddU16(MSG_KEY_PARAMS_ORDINAL, self.__dict__['ordinal'])
        submsg.AddStringUtf8(MSG_KEY_PARAMS_EXPORT_NAME, self.__dict__['exportName'])
        submsg.AddData(MSG_KEY_PARAMS_CHUNK, self.__dict__['chunk'])
        submsg.AddU32(MSG_KEY_PARAMS_PROCESS_ID, self.__dict__['pid'])
        mmsg.AddMessage(MSG_KEY_PARAMS, submsg)

    def Demarshal(self, dmsg, instance=-1):
        import mcl.object.Message
        msgData = dmsg.FindData(MSG_KEY_PARAMS, mcl.object.Message.MSG_TYPE_MSG, instance)
        submsg = mcl.object.Message.DemarshalMessage(msgData)
        self.__dict__['chunkOffset'] = submsg.FindU32(MSG_KEY_PARAMS_CHUNK_OFFSET)
        self.__dict__['totalSize'] = submsg.FindU32(MSG_KEY_PARAMS_TOTAL_SIZE)
        try:
            self.__dict__['ordinal'] = submsg.FindU16(MSG_KEY_PARAMS_ORDINAL)
        except:
            pass

        try:
            self.__dict__['exportName'] = submsg.FindString(MSG_KEY_PARAMS_EXPORT_NAME)
        except:
            pass

        self.__dict__['chunk'] = submsg.FindData(MSG_KEY_PARAMS_CHUNK)
        try:
            self.__dict__['pid'] = submsg.FindU32(MSG_KEY_PARAMS_PROCESS_ID)
        except:
            pass