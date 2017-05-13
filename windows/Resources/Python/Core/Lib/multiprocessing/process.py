# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.6.0b2 (default, Oct 11 2016, 05:27:10) 
# [GCC 6.2.0 20161005]
# Embedded file name: process.py
__all__ = [
 'Process', 'current_process', 'active_children']
import os
import sys
import signal
import itertools
try:
    ORIGINAL_DIR = os.path.abspath(os.getcwd())
except OSError:
    ORIGINAL_DIR = None

def current_process():
    """
    Return process object representing the current process
    """
    global _current_process
    return _current_process


def active_children():
    """
    Return list of process objects corresponding to live child processes
    """
    _cleanup()
    return list(_current_process._children)


def _cleanup():
    for p in list(_current_process._children):
        if p._popen.poll() is not None:
            _current_process._children.discard(p)

    return


class Process(object):
    """
    Process objects represent activity that is run in a separate process
    
    The class is analagous to `threading.Thread`
    """
    _Popen = None

    def __init__(self, group=None, target=None, name=None, args=(), kwargs={}):
        count = _current_process._counter.next()
        self._identity = _current_process._identity + (count,)
        self._authkey = _current_process._authkey
        self._daemonic = _current_process._daemonic
        self._tempdir = _current_process._tempdir
        self._parent_pid = os.getpid()
        self._popen = None
        self._target = target
        self._args = tuple(args)
        self._kwargs = dict(kwargs)
        self._name = name or type(self).__name__ + '-' + ':'.join((str(i) for i in self._identity))
        return

    def run(self):
        """
        Method to be run in sub-process; can be overridden in sub-class
        """
        if self._target:
            self._target(*self._args, **self._kwargs)

    def start(self):
        """
        Start child process
        """
        _cleanup()
        if self._Popen is not None:
            Popen = self._Popen
        else:
            from .forking import Popen
        self._popen = Popen(self)
        _current_process._children.add(self)
        return

    def terminate(self):
        """
        Terminate process; sends SIGTERM signal or uses TerminateProcess()
        """
        self._popen.terminate()

    def join(self, timeout=None):
        """
        Wait until child process terminates
        """
        res = self._popen.wait(timeout)
        if res is not None:
            _current_process._children.discard(self)
        return

    def is_alive(self):
        """
        Return whether process is alive
        """
        if self is _current_process:
            return True
        else:
            if self._popen is None:
                return False
            self._popen.poll()
            return self._popen.returncode is None

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @property
    def daemon(self):
        """
        Return whether process is a daemon
        """
        return self._daemonic

    @daemon.setter
    def daemon(self, daemonic):
        """
        Set whether process is a daemon
        """
        self._daemonic = daemonic

    @property
    def authkey(self):
        return self._authkey

    @authkey.setter
    def authkey(self, authkey):
        """
        Set authorization key of process
        """
        self._authkey = AuthenticationString(authkey)

    @property
    def exitcode(self):
        """
        Return exit code of process or `None` if it has yet to stop
        """
        if self._popen is None:
            return self._popen
        else:
            return self._popen.poll()

    @property
    def ident(self):
        """
        Return identifier (PID) of process or `None` if it has yet to start
        """
        if self is _current_process:
            return os.getpid()
        else:
            return self._popen and self._popen.pid

    pid = ident

    def __repr__(self):
        if self is _current_process:
            status = 'started'
        elif self._parent_pid != os.getpid():
            status = 'unknown'
        elif self._popen is None:
            status = 'initial'
        elif self._popen.poll() is not None:
            status = self.exitcode
        else:
            status = 'started'
        if type(status) is int:
            if status == 0:
                status = 'stopped'
            else:
                status = 'stopped[%s]' % _exitcode_to_name.get(status, status)
        return '<%s(%s, %s%s)>' % (type(self).__name__, self._name,
         status, self._daemonic and ' daemon' or '')

    def _bootstrap(self):
        global _current_process
        from . import util
        try:
            self._children = set()
            self._counter = itertools.count(1)
            try:
                sys.stdin.close()
                sys.stdin = open(os.devnull)
            except (OSError, ValueError):
                pass

            _current_process = self
            util._finalizer_registry.clear()
            util._run_after_forkers()
            util.info('child process calling self.run()')
            try:
                self.run()
                exitcode = 0
            finally:
                util._exit_function()

        except SystemExit as e:
            if not e.args:
                exitcode = 1
            elif type(e.args[0]) is int:
                exitcode = e.args[0]
            else:
                sys.stderr.write(e.args[0] + '\n')
                sys.stderr.flush()
                exitcode = 1
        except:
            exitcode = 1
            import traceback
            sys.stderr.write('Process %s:\n' % self.name)
            sys.stderr.flush()
            traceback.print_exc()

        util.info('process exiting with exitcode %d' % exitcode)
        return exitcode


class AuthenticationString(bytes):

    def __reduce__(self):
        from .forking import Popen
        if not Popen.thread_is_spawning():
            raise TypeError('Pickling an AuthenticationString object is disallowed for security reasons')
        return (
         AuthenticationString, (bytes(self),))


class _MainProcess(Process):

    def __init__(self):
        self._identity = ()
        self._daemonic = False
        self._name = 'MainProcess'
        self._parent_pid = None
        self._popen = None
        self._counter = itertools.count(1)
        self._children = set()
        self._authkey = AuthenticationString(os.urandom(32))
        self._tempdir = None
        return


_current_process = _MainProcess()
del _MainProcess
_exitcode_to_name = {}
for name, signum in signal.__dict__.items():
    if name[:3] == 'SIG' and '_' not in name:
        _exitcode_to_name[-signum] = name