# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.6.0b2 (default, Oct 11 2016, 05:27:10) 
# [GCC 6.2.0 20161005]
# Embedded file name: Mcl_Cmd_PcStatus_DataHandler.py


def DataHandlerMain(namespace, InputFilename, OutputFilename):
    import mcl.imports
    import mcl.data.Input
    import mcl.data.Output
    import mcl.status
    import mcl.target
    import mcl.object.Message
    mcl.imports.ImportNamesWithNamespace(namespace, 'pc.cmd.pcstatus', globals())
    input = mcl.data.Input.GetInput(InputFilename)
    output = mcl.data.Output.StartOutput(OutputFilename, input)
    output.Start('PcStatus', 'pcstatus', [])
    msg = mcl.object.Message.DemarshalMessage(input.GetData())
    if input.GetStatus() != mcl.status.MCL_SUCCESS:
        errorMsg = msg.FindMessage(mcl.object.Message.MSG_KEY_RESULT_ERROR)
        moduleError = errorMsg.FindU32(mcl.object.Message.MSG_KEY_RESULT_ERROR_MODULE)
        osError = errorMsg.FindU32(mcl.object.Message.MSG_KEY_RESULT_ERROR_OS)
        output.RecordModuleError(moduleError, osError, errorStrings)
        output.EndWithStatus(input.GetStatus())
        return True
    result = Result()
    result.Demarshal(msg)
    from mcl.object.XmlOutput import XmlOutput
    xml = XmlOutput()
    xml.Start('PcStatus')
    xml.AddAttribute('versionMajor', '%u' % result.major)
    xml.AddAttribute('versionMinor', '%u' % result.minor)
    xml.AddAttribute('versionBuild', '%u' % result.build)
    xml.AddAttribute('pcId', '0x%x' % result.pcId)
    xml.AddAttribute('name', result.name)
    sub = xml.AddSubElement('Trigger')
    typeValue = ''
    if result.triggerType & RESULT_TRIGGER_TYPE_DMGZ:
        typeValue += 'DMGZ, '
    if result.triggerType & RESULT_TRIGGER_TYPE_FLAV:
        typeValue += 'FLAV, '
    if result.triggerType & RESULT_TRIGGER_TYPE_RAW:
        typeValue += 'RAW, '
    if result.triggerType & RESULT_TRIGGER_TYPE_KNOCK:
        typeValue += 'KNOCK, '
    if result.triggerType == RESULT_TRIGGER_TYPE_UNKNOWN:
        typeValue += 'UNKNOWN, '
    sub.AddAttribute('type', typeValue[:-2])
    sub.AddAttribute('numReceived', '%u' % result.numTriggersReceived)
    sub.AddTimeElement('LastReceived', result.lastTriggerTime)
    statusStr = 'UNKNOWN'
    if result.lastTriggerStatus == RESULT_TRIGGER_STATUS_NONE:
        statusStr = 'NONE'
    elif result.lastTriggerStatus == RESULT_TRIGGER_STATUS_ACCEPTED:
        statusStr = 'ACCEPTED'
    elif result.lastTriggerStatus == RESULT_TRIGGER_STATUS_DECRYPT_FAILED:
        statusStr = 'DECRYPT_FAILED'
    elif result.lastTriggerStatus == RESULT_TRIGGER_STATUS_BAD_SIZE:
        statusStr = 'BAD_SIZE'
    elif result.lastTriggerStatus == RESULT_TRIGGER_STATUS_BAD_ID:
        statusStr = 'BAD_ID'
    elif result.lastTriggerStatus == RESULT_TRIGGER_STATUS_BAD_TIMESTAMP:
        statusStr = 'BAD_TIMESTAMP'
    elif result.lastTriggerStatus == RESULT_TRIGGER_STATUS_BAD_DST_ADDRESS:
        statusStr = 'BAD_DST_ADDRESS'
    elif result.lastTriggerStatus == RESULT_TRIGGER_STATUS_DELIVERY_FAILED:
        statusStr = 'DELIVERY_FAILED'
    elif result.lastTriggerStatus == RESULT_TRIGGER_STATUS_UNSUPPORTED_TYPE:
        statusStr = 'UNSUPPORTED_TYPE'
    elif result.lastTriggerStatus == RESULT_TRIGGER_STATUS_INVALID_AUTH:
        statusStr = 'INVALID_AUTH'
    elif result.lastTriggerStatus == RESULT_TRIGGER_STATUS_OTHER_FAILURE:
        statusStr = 'OTHER_FAILURE'
    else:
        statusStr = 'OTHER_FAILURE'
    sub.AddAttribute('status', statusStr)
    output.RecordXml(xml)
    output.EndWithStatus(mcl.target.CALL_SUCCEEDED)
    return True


if __name__ == '__main__':
    import sys
    try:
        namespace, InputFilename, OutputFilename = sys.argv[1:]
    except:
        print '%s <namespace> <input filename> <output filename>' % sys.argv[0]
        sys.exit(1)

    if DataHandlerMain(namespace, InputFilename, OutputFilename) != True:
        sys.exit(-1)