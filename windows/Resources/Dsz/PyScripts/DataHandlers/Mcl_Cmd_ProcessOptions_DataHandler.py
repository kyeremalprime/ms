# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.6.0b2 (default, Oct 11 2016, 05:27:10) 
# [GCC 6.2.0 20161005]
# Embedded file name: Mcl_Cmd_ProcessOptions_DataHandler.py
EXECUTE_OPTION_EXECUTION_DISABLED = 1
EXECUTE_OPTION_EXECUTION_ENABLED = 2
EXECUTE_OPTION_DISABLE_THUNK_EMULATION = 4
EXECUTE_OPTION_PERMANENT = 8
EXECUTE_OPTION_EXECUTE_DISPATH_ENABLE = 16
EXECUTE_OPTION_IMAGE_DISPATCH_ENABLE = 32
EXECUTE_OPTION_DISABLE_EXCEPTION_CHAIN_VALIDATION = 64
EXECUTE_OPTION_MASK = 127

def DataHandlerMain(namespace, InputFilename, OutputFilename):
    import mcl.imports
    import mcl.data.Input
    import mcl.data.Output
    import mcl.status
    import mcl.target
    import mcl.object.Message
    mcl.imports.ImportNamesWithNamespace(namespace, 'mca.process.cmd.processoptions', globals())
    input = mcl.data.Input.GetInput(InputFilename)
    output = mcl.data.Output.StartOutput(OutputFilename, input)
    output.Start('ProcessOptions', 'processoptions', [])
    msg = mcl.object.Message.DemarshalMessage(input.GetData())
    if input.GetStatus() != mcl.status.MCL_SUCCESS:
        errorMsg = msg.FindMessage(mcl.object.Message.MSG_KEY_RESULT_ERROR)
        moduleError = errorMsg.FindU32(mcl.object.Message.MSG_KEY_RESULT_ERROR_MODULE)
        osError = errorMsg.FindU32(mcl.object.Message.MSG_KEY_RESULT_ERROR_OS)
        if moduleError == ERR_ELEVATION_FAILED:
            import mcl.elevation.errors
            output.RecordModuleError(moduleError, 0, errorStrings)
            output.RecordModuleError(osError, 0, mcl.elevation.errors.errorStrings)
        else:
            output.RecordModuleError(moduleError, osError, errorStrings)
        output.EndWithStatus(input.GetStatus())
        return True
    if msg.GetCount() > 0:
        result = Result()
        result.Demarshal(msg)
        from mcl.object.XmlOutput import XmlOutput
        xml = XmlOutput()
        xml.Start('ExecuteOptions')
        xml.AddAttribute('processId', '%u' % result.processId)
        xml.AddAttribute('value', '0x%08x' % result.value)
        if result.value & EXECUTE_OPTION_EXECUTION_DISABLED:
            xml.AddSubElement('ExecutionDisabled')
        if result.value & EXECUTE_OPTION_EXECUTION_ENABLED:
            xml.AddSubElement('ExecutionEnabled')
        if result.value & EXECUTE_OPTION_DISABLE_THUNK_EMULATION:
            xml.AddSubElement('DisableThunkEmulation')
        if result.value & EXECUTE_OPTION_PERMANENT:
            xml.AddSubElement('Permanent')
        if result.value & EXECUTE_OPTION_EXECUTE_DISPATH_ENABLE:
            xml.AddSubElement('ExecuteDispatchEnabled')
        if result.value & EXECUTE_OPTION_IMAGE_DISPATCH_ENABLE:
            xml.AddSubElement('ImageDispatchEnabled')
        if result.value & EXECUTE_OPTION_DISABLE_EXCEPTION_CHAIN_VALIDATION:
            xml.AddSubElement('DisableExceptionChainValidation')
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