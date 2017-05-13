# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.6.0b2 (default, Oct 11 2016, 05:27:10) 
# [GCC 6.2.0 20161005]
# Embedded file name: errors.py
import mcl.status
ERR_SUCCESS = mcl.status.MCL_SUCCESS
ERR_INVALID_PARAM = mcl.status.framework.ERR_START
ERR_MARSHAL_FAILED = mcl.status.framework.ERR_START + 1
ERR_DEVICE_OPEN_FAILED = mcl.status.framework.ERR_START + 2
ERR_OUTPUT_SIZE_MISMATCH = mcl.status.framework.ERR_START + 3
ERR_NOT_IMPLEMENTED = mcl.status.framework.ERR_START + 4
errorStrings = {ERR_INVALID_PARAM: 'Invalid parameter(s)',
   ERR_MARSHAL_FAILED: 'Failed to marshal data',
   ERR_DEVICE_OPEN_FAILED: 'Opening of device failed',
   ERR_OUTPUT_SIZE_MISMATCH: 'Data from device was incorrect',
   ERR_NOT_IMPLEMENTED: 'Not implemented on this platform'
   }