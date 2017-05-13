# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.6.0b2 (default, Oct 11 2016, 05:27:10) 
# [GCC 6.2.0 20161005]
# Embedded file name: Mcl_Cmd_NameServerLookup_Tasking.py


def TaskingMain(namespace):
    import mcl.imports
    import mcl.target
    import mcl.tasking
    from mcl.object.Message import MarshalMessage
    mcl.imports.ImportWithNamespace(namespace, 'mca.network.cmd.nameserverlookup', globals())
    mcl.imports.ImportWithNamespace(namespace, 'mca.network.cmd.nameserverlookup.tasking', globals())
    lpParams = mcl.tasking.GetParameters()
    if lpParams['addr'] == None or len(lpParams['addr']) == 0:
        mcl.tasking.OutputError('A destination must be specified')
        return False
    else:
        tgtParams = mca.network.cmd.nameserverlookup.Params()
        gotValidDst = False
        try:
            import mcl.object.IpAddr
            tgtParams.dstAddr = mcl.object.IpAddr.IpAddr.CreateFromString(lpParams['addr'])
            gotValidDst = True
        except:
            pass

        if not gotValidDst:
            tgtParams.dstHost = lpParams['addr']
        taskXml = mcl.tasking.Tasking()
        taskXml.AddSearchParam(lpParams['addr'])
        mcl.tasking.OutputXml(taskXml.GetXmlObject())
        rpc = mca.network.cmd.nameserverlookup.tasking.RPC_INFO_QUERY
        msg = MarshalMessage()
        tgtParams.Marshal(msg)
        rpc.SetData(msg.Serialize())
        rpc.SetMessagingType('message')
        res = mcl.tasking.RpcPerformCall(rpc)
        if res != mcl.target.CALL_SUCCEEDED:
            mcl.tasking.RecordModuleError(res, 0, mca.network.cmd.nameserverlookup.errorStrings)
            return False
        return True


if __name__ == '__main__':
    import sys
    if TaskingMain(sys.argv[1]) != True:
        sys.exit(-1)