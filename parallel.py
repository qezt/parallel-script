#!/usr/bin/env python
# coding: utf8

import sys

from multiprocessing import Pool
import subprocess


def proc(cmd):
    pipe = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True, close_fds=True)
    return pipe.communicate()


def main():
    cmds = sys.stdin.read().strip().splitlines()
    pool = Pool()
    try:
        for idx, (stdout, stderr) in enumerate(pool.imap(proc, cmds)):
            print '>', idx, cmds[idx]
            if stderr:
                print >> sys.stderr, stderr
            print stdout.strip()
    except KeyboardInterrupt:
        pool.close()
        print 'Exiting ...'


if __name__ == '__main__':
    main()
