# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.6.0b2 (default, Oct 11 2016, 05:27:10) 
# [GCC 6.2.0 20161005]
# Embedded file name: __init__.py
import dsz
import dsz.cmd
import dsz.data
import dsz.lp

class Aliases(dsz.data.Task):

    def __init__(self, cmd=None):
        dsz.data.Task.__init__(self, cmd)

    def _LoadData(self):
        self.AliasItem = list()
        try:
            for x in dsz.cmd.data.Get('AliasItem', dsz.TYPE_OBJECT):
                self.AliasItem.append(Aliases.AliasItem(x))

        except:
            pass

    class AliasItem(dsz.data.DataBean):

        def __init__(self, obj):
            try:
                self.location = dsz.cmd.data.ObjectGet(obj, 'location', dsz.TYPE_STRING)[0]
            except:
                self.location = None

            try:
                self.replace = dsz.cmd.data.ObjectGet(obj, 'replace', dsz.TYPE_STRING)[0]
            except:
                self.replace = None

            try:
                self.alias = dsz.cmd.data.ObjectGet(obj, 'alias', dsz.TYPE_STRING)[0]
            except:
                self.alias = None

            self.Options = list()
            try:
                for x in dsz.cmd.data.ObjectGet(obj, 'Options', dsz.TYPE_OBJECT):
                    self.Options.append(Aliases.AliasItem.Options(x))

            except:
                pass

            return

        class Options(dsz.data.DataBean):

            def __init__(self, obj):
                try:
                    self.option = dsz.cmd.data.ObjectGet(obj, 'option', dsz.TYPE_STRING)
                except:
                    self.option = None

                return


dsz.data.RegisterCommand('Aliases', Aliases)
ALIASES = Aliases
aliases = Aliases