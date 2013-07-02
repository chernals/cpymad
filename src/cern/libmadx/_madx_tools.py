##
# This file contains tool functions for madx.pyx
#

from cern.pymad.io import tfs,tfsDict


def _checkCommand(cmd):
    ''' give the lowercase version of the command
    this function does some sanity checks...'''
    if "stop;" in cmd or "exit;" in cmd:
        print("WARNING: found quit in command: "+cmd+"\n")
        print("Please use madx.finish() or just exit python (CTRL+D)")
        print("Command ignored")
        return False
    if cmd.split(',')>0 and "plot" in cmd.split(',')[0]:
        print("WARNING: Plot functionality does not work through pymadx")
        print("Command ignored")
        return False
    # All checks passed..
    return True

def _fixcmd(cmd):
    '''
    Makes sure command is sane.
    '''
    if not isinstance(cmd, basestring):
        raise TypeError("ERROR: input must be a string, not "+str(type(cmd)))
    if len(cmd.strip())==0:
        return 0
    if cmd.strip()[-1]!=';':
        cmd+=';'
    # for very long commands (probably parsed in from a file)
    # we split and only run one line at the time.
    if len(cmd)>10000:
        cmd=cmd.split('\n')
    return cmd

def _get_dict(tmpfile,retdict):
    '''
     Returns a dictionary from the temporary file.
    '''
    if retdict:
        return tfsDict(tmpfile)
    return tfs(tmpfile)

def _add_range(madrange):
    if madrange:
        if isinstance(madrange, basestring):
            return 'range='+madrange+','
        elif type(madrange)==list:
            return 'range='+madrange[0]+'/'+madrange[1]+','
        elif type(madrange)==dict:
            return 'range='+madrange['first']+'/'+madrange['last']+','
        else:
            raise TypeError("Wrong range type/format")
    return ''

def _add_offsets(offsets):
    if offsets:
        return 'offsetelem="'+offsets+'",'
    return ''
