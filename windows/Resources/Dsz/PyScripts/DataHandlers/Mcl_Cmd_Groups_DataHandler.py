# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.6.0b2 (default, Oct 11 2016, 05:27:10) 
# [GCC 6.2.0 20161005]
# Embedded file name: Mcl_Cmd_Groups_DataHandler.py


def DataHandlerMain(namespace, InputFilename, OutputFilename):
    import mcl.imports
    import mcl.data.Input
    import mcl.data.Output
    import mcl.msgtype
    import mcl.status
    import mcl.target
    import mcl.object.Message
    mcl.imports.ImportNamesWithNamespace(namespace, 'mca.survey.cmd.groups', globals())
    _GROUP_FLAGS = {RESULT_GROUP_ATTRIBUTE_ENABLED: 'SeGroupEnabled',
       RESULT_GROUP_ATTRIBUTE_ENABLED_BY_DEFAULT: 'SeGroupEnabledByDefault',
       RESULT_GROUP_ATTRIBUTE_LOGON_ID: 'SeGroupLogonId',
       RESULT_GROUP_ATTRIBUTE_MANDATORY: 'SeGroupMandatory',
       RESULT_GROUP_ATTRIBUTE_OWNER: 'SeGroupOwner',
       RESULT_GROUP_ATTRIBUTE_RESOURCE: 'SeGroupResource',
       RESULT_GROUP_ATTRIBUTE_USE_FOR_DENY_ONLY: 'SeGroupUseForDenyOnly'
       }
    input = mcl.data.Input.GetInput(InputFilename)
    output = mcl.data.Output.StartOutput(OutputFilename, input)
    output.Start('Groups', 'groups', [])
    msg = mcl.object.Message.DemarshalMessage(input.GetData())
    if input.GetStatus() != mcl.status.MCL_SUCCESS:
        errorMsg = msg.FindMessage(mcl.object.Message.MSG_KEY_RESULT_ERROR)
        moduleError = errorMsg.FindU32(mcl.object.Message.MSG_KEY_RESULT_ERROR_MODULE)
        osError = errorMsg.FindU32(mcl.object.Message.MSG_KEY_RESULT_ERROR_OS)
        output.RecordModuleError(moduleError, osError, errorStrings)
        output.EndWithStatus(input.GetStatus())
        return True
    if msg.GetCount() == 0:
        output.EndWithStatus(mcl.target.CALL_SUCCEEDED)
        return True
    from mcl.object.XmlOutput import XmlOutput
    xml = XmlOutput()
    xml.Start('Groups')
    while msg.GetNumRetrieved() < msg.GetCount():
        if mcl.CheckForStop():
            output.RecordXml(xml)
            output.EndWithStatus(mcl.target.CALL_FAILED)
            return False
        results = Result()
        results.Demarshal(msg)
        _handleGroup(_GROUP_FLAGS, xml, results)

    output.RecordXml(xml)
    output.End()
    return True


def _handleGroup(_GROUP_FLAGS, xml, results):
    sub = xml.AddSubElement('Group')
    sub.AddAttribute('groupId', '%i' % results.id)
    sub.AddAttribute('group', results.name)
    sub.AddAttribute('comment', results.comment)
    sub2 = sub.AddSubElement('Attributes')
    sub2.AddAttribute('mask', '0x%08x' % results.attributes)
    for flag in _GROUP_FLAGS.keys():
        if results.attributes & flag:
            sub2.AddSubElement(_GROUP_FLAGS[flag])


if __name__ == '__main__':
    import sys
    try:
        namespace, InputFilename, OutputFilename = sys.argv[1:]
    except:
        print '%s <namespace> <input filename> <output filename>' % sys.argv[0]
        sys.exit(1)

    if DataHandlerMain(namespace, InputFilename, OutputFilename) != True:
        sys.exit(-1)