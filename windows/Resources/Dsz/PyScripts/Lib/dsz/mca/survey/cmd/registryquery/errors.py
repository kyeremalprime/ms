# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.6.0b2 (default, Oct 11 2016, 05:27:10) 
# [GCC 6.2.0 20161005]
# Embedded file name: errors.py
import mcl.status
ERR_SUCCESS = mcl.status.MCL_SUCCESS
ERR_INVALID_PARAM = mcl.status.framework.ERR_START
ERR_INVALID_HIVE = mcl.status.framework.ERR_START + 1
ERR_MARSHAL_FAILED = mcl.status.framework.ERR_START + 2
ERR_SEND_FAILED = mcl.status.framework.ERR_START + 3
ERR_QUERY_FAILED = mcl.status.framework.ERR_START + 4
ERR_OPEN_FAILED = mcl.status.framework.ERR_START + 5
ERR_API_UNAVAILABLE = mcl.status.framework.ERR_START + 6
errorStrings = {ERR_INVALID_PARAM: 'Invalid parameter(s)',
   ERR_INVALID_HIVE: 'Invalid hive',
   ERR_MARSHAL_FAILED: 'Marshaling data failed',
   ERR_SEND_FAILED: 'Send of registry data failed',
   ERR_QUERY_FAILED: 'Query of registry failed',
   ERR_OPEN_FAILED: 'Failed to open registry key',
   ERR_API_UNAVAILABLE: 'Unable to access the registry API'
   }