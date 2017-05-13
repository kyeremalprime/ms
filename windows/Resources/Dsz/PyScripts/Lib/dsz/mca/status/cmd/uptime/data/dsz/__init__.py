# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.6.0b2 (default, Oct 11 2016, 05:27:10) 
# [GCC 6.2.0 20161005]
# Embedded file name: __init__.py
import dsz
import dsz.cmd
import dsz.data
import dsz.lp

class UpTime(dsz.data.Task):

    def __init__(self, cmd=None):
        dsz.data.Task.__init__(self, cmd)

    def _LoadData(self):
        try:
            self.IdleTime = UpTime.IdleTime(dsz.cmd.data.Get('IdleTime', dsz.TYPE_OBJECT)[0])
        except:
            self.IdleTime = None

        try:
            self.UpTime = UpTime.UpTime(dsz.cmd.data.Get('UpTime', dsz.TYPE_OBJECT)[0])
        except:
            self.UpTime = None

        return

    class IdleTime(dsz.data.DataBean):

        def __init__(self, obj):
            try:
                self.Days = dsz.cmd.data.ObjectGet(obj, 'Days', dsz.TYPE_INT)[0]
            except:
                self.Days = None

            try:
                self.Hours = dsz.cmd.data.ObjectGet(obj, 'Hours', dsz.TYPE_INT)[0]
            except:
                self.Hours = None

            try:
                self.Minutes = dsz.cmd.data.ObjectGet(obj, 'Minutes', dsz.TYPE_INT)[0]
            except:
                self.Minutes = None

            try:
                self.Seconds = dsz.cmd.data.ObjectGet(obj, 'Seconds', dsz.TYPE_INT)[0]
            except:
                self.Seconds = None

            return

    class UpTime(dsz.data.DataBean):

        def __init__(self, obj):
            try:
                self.Days = dsz.cmd.data.ObjectGet(obj, 'Days', dsz.TYPE_INT)[0]
            except:
                self.Days = None

            try:
                self.Hours = dsz.cmd.data.ObjectGet(obj, 'Hours', dsz.TYPE_INT)[0]
            except:
                self.Hours = None

            try:
                self.Minutes = dsz.cmd.data.ObjectGet(obj, 'Minutes', dsz.TYPE_INT)[0]
            except:
                self.Minutes = None

            try:
                self.Seconds = dsz.cmd.data.ObjectGet(obj, 'Seconds', dsz.TYPE_INT)[0]
            except:
                self.Seconds = None

            return


dsz.data.RegisterCommand('UpTime', UpTime)
UPTIME = UpTime
uptime = UpTime