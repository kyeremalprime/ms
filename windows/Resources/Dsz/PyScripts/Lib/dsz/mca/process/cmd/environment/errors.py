# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.6.0b2 (default, Oct 11 2016, 05:27:10) 
# [GCC 6.2.0 20161005]
# Embedded file name: errors.py
import mcl.status
ERR_SUCCESS = mcl.status.MCL_SUCCESS
ERR_INVALID_PARAM = mcl.status.framework.ERR_START
ERR_MARSHAL_FAILED = mcl.status.framework.ERR_START + 1
ERR_NOT_SUPPORTED = mcl.status.framework.ERR_START + 2
ERR_SET_FAILED = mcl.status.framework.ERR_START + 3
ERR_ALLOC_FAILED = mcl.status.framework.ERR_START + 4
ERR_GETQUERY_FAILED = mcl.status.framework.ERR_START + 5
ERR_DELETE_FAILED = mcl.status.framework.ERR_START + 6
ERR_NOT_FOUND = mcl.status.framework.ERR_START + 7
ERR_EXPAND_FAILED = mcl.status.framework.ERR_START + 8
errorStrings = {ERR_INVALID_PARAM: 'Invalid parameter(s)',
   ERR_MARSHAL_FAILED: 'Marshaling data failed',
   ERR_NOT_SUPPORTED: 'Function not supported on this platform',
   ERR_SET_FAILED: 'Set of environment variable failed',
   ERR_ALLOC_FAILED: 'Memory allocation failed',
   ERR_GETQUERY_FAILED: 'Get of environment value failed',
   ERR_DELETE_FAILED: 'Delete of environment variable failed',
   ERR_NOT_FOUND: 'The environment variable does not exist',
   ERR_EXPAND_FAILED: 'Expansion of environment variable failed'
   }