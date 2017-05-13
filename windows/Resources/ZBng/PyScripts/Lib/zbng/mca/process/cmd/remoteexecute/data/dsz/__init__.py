# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.6.0b2 (default, Oct 11 2016, 05:27:10) 
# [GCC 6.2.0 20161005]
# Embedded file name: __init__.py
import dsz
import dsz.cmd
import dsz.data
import dsz.lp

class RemoteExecute(dsz.data.Task):

    def __init__(self, cmd=None):
        dsz.data.Task.__init__(self, cmd)

    def _LoadData(self):
        try:
            self.Target = RemoteExecute.Target(dsz.cmd.data.Get('Target', dsz.TYPE_OBJECT)[0])
        except:
            self.Target = None

        try:
            self.remoteexecution = RemoteExecute.remoteexecution(dsz.cmd.data.Get('remoteexecution', dsz.TYPE_OBJECT)[0])
        except:
            self.remoteexecution = None

        return

    class Target(dsz.data.DataBean):

        def __init__(self, obj):
            try:
                self.local = dsz.cmd.data.ObjectGet(obj, 'local', dsz.TYPE_BOOL)[0]
            except:
                self.local = None

            try:
                self.location = dsz.cmd.data.ObjectGet(obj, 'location', dsz.TYPE_STRING)[0]
            except:
                self.location = None

            return

    class remoteexecution(dsz.data.DataBean):

        def __init__(self, obj):
            try:
                self.processid = dsz.cmd.data.ObjectGet(obj, 'processid', dsz.TYPE_INT)[0]
            except:
                self.processid = None

            try:
                self.returnvalue = dsz.cmd.data.ObjectGet(obj, 'returnvalue', dsz.TYPE_INT)[0]
            except:
                self.returnvalue = None

            return


dsz.data.RegisterCommand('RemoteExecute', RemoteExecute)
REMOTEEXECUTE = RemoteExecute
remoteexecute = RemoteExecute