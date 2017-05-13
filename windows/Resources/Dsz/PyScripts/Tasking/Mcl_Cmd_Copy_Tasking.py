# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.6.0b2 (default, Oct 11 2016, 05:27:10) 
# [GCC 6.2.0 20161005]
# Embedded file name: Mcl_Cmd_Copy_Tasking.py


def TaskingMain(namespace):
    import mcl.imports
    import mcl.target
    import mcl.tasking
    import mcl.tasking.virtualdir
    from mcl.object.Message import MarshalMessage
    mcl.imports.ImportWithNamespace(namespace, 'mca.file.cmd.copy', globals())
    mcl.imports.ImportWithNamespace(namespace, 'mca.file.cmd.copy.tasking', globals())
    lpParams = mcl.tasking.GetParameters()
    if lpParams['src'] == None or len(lpParams['src']) == 0 or lpParams['dst'] == None or len(lpParams['dst']) == 0:
        mcl.tasking.EchoError('A source and destination must be specified')
        return False
    else:
        tgtParams = mca.file.cmd.copy.Params()
        try:
            tgtParams.src = mcl.tasking.virtualdir.GetFullPath(lpParams['src'])
            tgtParams.dst = mcl.tasking.virtualdir.GetFullPath(lpParams['dst'])
        except:
            mcl.tasking.EchoError('Failed to get full paths for file copy')
            return False

        rpc = mca.file.cmd.copy.tasking.RPC_INFO_COPY
        msg = MarshalMessage()
        tgtParams.Marshal(msg)
        rpc.SetData(msg.Serialize())
        rpc.SetMessagingType('message')
        res = mcl.tasking.RpcPerformCall(rpc)
        if res != mcl.target.CALL_SUCCEEDED:
            mcl.tasking.RecordModuleError(res, 0, mca.file.cmd.copy.errorStrings)
            return False
        return True


if __name__ == '__main__':
    import sys
    if TaskingMain(sys.argv[1]) != True:
        sys.exit(-1)