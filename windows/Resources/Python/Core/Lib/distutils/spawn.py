# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.6.0b2 (default, Oct 11 2016, 05:27:10) 
# [GCC 6.2.0 20161005]
# Embedded file name: spawn.py
"""distutils.spawn

Provides the 'spawn()' function, a front-end to various platform-
specific functions for launching another program in a sub-process.
Also provides the 'find_executable()' to search the path for a given
executable name.
"""
__revision__ = '$Id$'
import sys
import os
from distutils.errors import DistutilsPlatformError, DistutilsExecError
from distutils import log

def spawn(cmd, search_path=1, verbose=0, dry_run=0):
    """Run another program, specified as a command list 'cmd', in a new process.
    
    'cmd' is just the argument list for the new process, ie.
    cmd[0] is the program to run and cmd[1:] are the rest of its arguments.
    There is no way to run a program with a name different from that of its
    executable.
    
    If 'search_path' is true (the default), the system's executable
    search path will be used to find the program; otherwise, cmd[0]
    must be the exact path to the executable.  If 'dry_run' is true,
    the command will not actually be run.
    
    Raise DistutilsExecError if running the program fails in any way; just
    return on success.
    """
    if os.name == 'posix':
        _spawn_posix(cmd, search_path, dry_run=dry_run)
    elif os.name == 'nt':
        _spawn_nt(cmd, search_path, dry_run=dry_run)
    elif os.name == 'os2':
        _spawn_os2(cmd, search_path, dry_run=dry_run)
    else:
        raise DistutilsPlatformError, "don't know how to spawn programs on platform '%s'" % os.name


def _nt_quote_args(args):
    """Quote command-line arguments for DOS/Windows conventions.
    
    Just wraps every argument which contains blanks in double quotes, and
    returns a new argument list.
    """
    for i, arg in enumerate(args):
        if ' ' in arg:
            args[i] = '"%s"' % arg

    return args


def _spawn_nt(cmd, search_path=1, verbose=0, dry_run=0):
    executable = cmd[0]
    cmd = _nt_quote_args(cmd)
    if search_path:
        executable = find_executable(executable) or executable
    log.info(' '.join([executable] + cmd[1:]))
    if not dry_run:
        try:
            rc = os.spawnv(os.P_WAIT, executable, cmd)
        except OSError as exc:
            raise DistutilsExecError, "command '%s' failed: %s" % (cmd[0], exc[-1])

        if rc != 0:
            raise DistutilsExecError, "command '%s' failed with exit status %d" % (cmd[0], rc)


def _spawn_os2(cmd, search_path=1, verbose=0, dry_run=0):
    executable = cmd[0]
    if search_path:
        executable = find_executable(executable) or executable
    log.info(' '.join([executable] + cmd[1:]))
    if not dry_run:
        try:
            rc = os.spawnv(os.P_WAIT, executable, cmd)
        except OSError as exc:
            raise DistutilsExecError, "command '%s' failed: %s" % (cmd[0], exc[-1])

        if rc != 0:
            log.debug("command '%s' failed with exit status %d" % (cmd[0], rc))
            raise DistutilsExecError, "command '%s' failed with exit status %d" % (cmd[0], rc)


def _spawn_posix(cmd, search_path=1, verbose=0, dry_run=0):
    log.info(' '.join(cmd))
    if dry_run:
        return
    exec_fn = search_path and os.execvp or os.execv
    pid = os.fork()
    if pid == 0:
        try:
            exec_fn(cmd[0], cmd)
        except OSError as e:
            sys.stderr.write('unable to execute %s: %s\n' % (
             cmd[0], e.strerror))
            os._exit(1)

        sys.stderr.write('unable to execute %s for unknown reasons' % cmd[0])
        os._exit(1)
    else:
        while 1:
            try:
                pid, status = os.waitpid(pid, 0)
            except OSError as exc:
                import errno
                if exc.errno == errno.EINTR:
                    continue
                raise DistutilsExecError, "command '%s' failed: %s" % (cmd[0], exc[-1])

            if os.WIFSIGNALED(status):
                raise DistutilsExecError, "command '%s' terminated by signal %d" % (
                 cmd[0], os.WTERMSIG(status))
            elif os.WIFEXITED(status):
                exit_status = os.WEXITSTATUS(status)
                if exit_status == 0:
                    return
                raise DistutilsExecError, "command '%s' failed with exit status %d" % (
                 cmd[0], exit_status)
            elif os.WIFSTOPPED(status):
                continue
            else:
                raise DistutilsExecError, "unknown error executing '%s': termination status %d" % (
                 cmd[0], status)


def find_executable(executable, path=None):
    """Tries to find 'executable' in the directories listed in 'path'.
    
    A string listing directories separated by 'os.pathsep'; defaults to
    os.environ['PATH'].  Returns the complete filename or None if not found.
    """
    if path is None:
        path = os.environ['PATH']
    paths = path.split(os.pathsep)
    base, ext = os.path.splitext(executable)
    if (sys.platform == 'win32' or os.name == 'os2') and ext != '.exe':
        executable = executable + '.exe'
    if not os.path.isfile(executable):
        for p in paths:
            f = os.path.join(p, executable)
            if os.path.isfile(f):
                return f

        return
    else:
        return executable
        return