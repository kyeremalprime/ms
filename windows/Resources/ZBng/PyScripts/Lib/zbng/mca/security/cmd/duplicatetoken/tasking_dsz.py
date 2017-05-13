# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.6.0b2 (default, Oct 11 2016, 05:27:10) 
# [GCC 6.2.0 20161005]
# Embedded file name: tasking_dsz.py
import mcl.framework
import mcl.tasking

class dsz:
    INTERFACE = 16842801
    PFAM = 4168
    PROVIDER_ANY = 4168
    PROVIDER = 16846920
    RPC_INFO_LIST = mcl.tasking.RpcInfo(mcl.framework.DSZ, [INTERFACE, PROVIDER_ANY, 0])
    RPC_INFO_STEAL = mcl.tasking.RpcInfo(mcl.framework.DSZ, [INTERFACE, PROVIDER_ANY, 1])