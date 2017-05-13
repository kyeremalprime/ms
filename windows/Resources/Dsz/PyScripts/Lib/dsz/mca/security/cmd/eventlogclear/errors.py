# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.6.0b2 (default, Oct 11 2016, 05:27:10) 
# [GCC 6.2.0 20161005]
# Embedded file name: errors.py
import mcl.status
ERR_SUCCESS = mcl.status.MCL_SUCCESS
ERR_INVALID_PARAM = mcl.status.framework.ERR_START
ERR_MARSHAL_FAILED = mcl.status.framework.ERR_START + 1
ERR_NOT_IMPLEMENTED = mcl.status.framework.ERR_START + 2
ERR_EVENTLOGKEY_ERROR = mcl.status.framework.ERR_START + 3
ERR_OPENLOG_FAILED = mcl.status.framework.ERR_START + 4
ERR_CLEARLOG_FAILED = mcl.status.framework.ERR_START + 5
ERR_API_NOT_FOUND = mcl.status.framework.ERR_START + 6
ERR_CONNECT_FAILED = mcl.status.framework.ERR_START + 7
errorStrings = {ERR_INVALID_PARAM: 'Invalid parameter(s)',
   ERR_MARSHAL_FAILED: 'Marshaling data failed',
   ERR_NOT_IMPLEMENTED: 'Not implemented on this platform',
   ERR_EVENTLOGKEY_ERROR: 'Specified eventlog name not found in registry',
   ERR_OPENLOG_FAILED: 'Open of event log failed',
   ERR_CLEARLOG_FAILED: 'Clear of event log failed',
   ERR_API_NOT_FOUND: 'Required API was not found',
   ERR_CONNECT_FAILED: 'Connect to remote target failed'
   }