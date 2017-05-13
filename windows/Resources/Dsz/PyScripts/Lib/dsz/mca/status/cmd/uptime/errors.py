# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.6.0b2 (default, Oct 11 2016, 05:27:10) 
# [GCC 6.2.0 20161005]
# Embedded file name: errors.py
import mcl.status
ERR_SUCCESS = mcl.status.MCL_SUCCESS
ERR_INVALID_PARAM = mcl.status.framework.ERR_START
ERR_NOT_IMPLEMENTED = mcl.status.framework.ERR_START + 1
ERR_MARSHAL_FAILED = mcl.status.framework.ERR_START + 2
ERR_NO_LOCK = mcl.status.framework.ERR_START + 3
ERR_LOCK_FAILED = mcl.status.framework.ERR_START + 4
ERR_ALLOC_FAILED = mcl.status.framework.ERR_START + 5
ERR_FAILED_TO_GET_UPTIME = mcl.status.framework.ERR_START + 6
ERR_TARGET_CONNECT_FAILED = mcl.status.framework.ERR_START + 7
ERR_TARGET_NOT_SUPPORTED = mcl.status.framework.ERR_START + 8
errorStrings = {ERR_INVALID_PARAM: 'Invalid parameter(s)',
   ERR_NOT_IMPLEMENTED: 'Not implemented on this platform',
   ERR_MARSHAL_FAILED: 'Marshaling data failed',
   ERR_NO_LOCK: 'The lock was not available',
   ERR_LOCK_FAILED: 'Unable to obtain the lock',
   ERR_ALLOC_FAILED: 'Failed to allocate memory',
   ERR_FAILED_TO_GET_UPTIME: 'Failed to get uptime',
   ERR_TARGET_CONNECT_FAILED: 'Failed to connect to target',
   ERR_TARGET_NOT_SUPPORTED: 'Remote target option not supported on this platform'
   }