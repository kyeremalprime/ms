# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.6.0b2 (default, Oct 11 2016, 05:27:10) 
# [GCC 6.2.0 20161005]
# Embedded file name: errors.py
import mcl.status
ERR_SUCCESS = mcl.status.MCL_SUCCESS
ERR_INVALID_PARAM = mcl.status.framework.ERR_START
ERR_FAILED = mcl.status.framework.ERR_START + 1
ERR_MARSHAL_FAILED = mcl.status.framework.ERR_START + 2
ERR_CALLBACK_FAILED = mcl.status.framework.ERR_START + 3
ERR_FUNCTION_NOT_FOUND = mcl.status.framework.ERR_START + 4
ERR_ALLOC_FAILED = mcl.status.framework.ERR_START + 5
ERR_QUERY_FAILED = mcl.status.framework.ERR_START + 6
ERR_EXCEPTION_THROWN = mcl.status.framework.ERR_START + 7
ERR_OPEN_FAILED = mcl.status.framework.ERR_START + 8
errorStrings = {ERR_INVALID_PARAM: 'Invalid parameter(s)',
   ERR_FAILED: 'Unspecified failure',
   ERR_MARSHAL_FAILED: 'Failed to marshal data',
   ERR_CALLBACK_FAILED: 'Failed to send callback data',
   ERR_FUNCTION_NOT_FOUND: 'Unable to find a required function',
   ERR_ALLOC_FAILED: 'Failed to allocate necessary memory',
   ERR_QUERY_FAILED: 'Query failed',
   ERR_EXCEPTION_THROWN: 'Exception encountered',
   ERR_OPEN_FAILED: 'Unable to open required resource'
   }