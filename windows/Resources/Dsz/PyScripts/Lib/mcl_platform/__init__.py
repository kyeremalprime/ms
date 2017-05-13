# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.6.0b2 (default, Oct 11 2016, 05:27:10) 
# [GCC 6.2.0 20161005]
# Embedded file name: __init__.py


def CheckForStop():
    import _dsz
    if _dsz.dszObj.check_for_stop():
        return True
    else:
        return False


def TransferXmlToCore(xml, parent=None):
    import _dsz
    import mcl.object.XmlOutput
    if not isinstance(xml, mcl.object.XmlOutput.XmlOutput):
        raise RuntimeError('xml must be of type mcl.object.XmlOutput.XmlOutput')
    namespace = xml.GetNamespace()
    if namespace != None and namespace != '':
        name = '%s:%s' % (namespace, xml.GetName())
    else:
        name = xml.GetName()
    attributes = xml.GetAttributes()
    text = xml.GetText()
    elements = xml.GetSubElements()
    if parent == None:
        x = _dsz.dszObj.xml_start(name, True)
    else:
        x = _dsz.dszObj.xml_add_subelement(parent, name)
    for key in attributes.keys():
        _dsz.dszObj.xml_add_attribute(x, key, attributes[key])

    if len(text) > 0:
        _dsz.dszObj.xml_set_text(x, text)
    for sub in elements:
        TransferXmlToCore(sub, x)

    return