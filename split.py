#!/usr/bin/env python3

import argparse
parser = argparse.ArgumentParser()
parser.add_argument('command', nargs='*')
parser.add_argument('-i', '--input',  required=True)
parser.add_argument('-o', '--output', required=True)
parser.add_argument('-t', '--time', metavar='SECOND', default=1.0, type=float)
parser.add_argument('-1', '--one', action='store_true', help='split line by line')
parser.add_argument('--ignore', metavar='N', default=0, type=int, help='ignore initial N lines of input')
parser.add_argument('--header', help='put a header string to the output')
parser.add_argument('--footer', help='put a footer string to the output')
args = parser.parse_args()
if args.one and args.command:
    parser.error('the following arguments conflicts: command, -1/--one')
if not args.command:
    args.command += ['./a.out']

if args.one:
    i = 0
    with open(args.input, 'rb') as inf:
        for line in inf:
            if args.ignore:
                args.ignore -= 1
                continue
            i += 1
            fname = args.output.format(i)
            print(fname)
            with open(fname, 'wb') as outf:
                if args.header:
                    outf.write(args.header.encode())
                outf.write(line)
                if args.footer:
                    outf.write(args.footer.encode())

else:

    # workaround
    import fcntl
    import os
    def non_block_read(fh):
        fd = fh.fileno()
        fl = fcntl.fcntl(fd, fcntl.F_GETFL)
        fcntl.fcntl(fd, fcntl.F_SETFL, fl | os.O_NONBLOCK)
        try:
            return fh.read()
        except:
            return ''

    import subprocess
    import time
    with open(args.input, 'rb') as inf:
        with subprocess.Popen(args.command, stdin=subprocess.PIPE, stdout=subprocess.PIPE) as proc:
            i = 0
            acc = b''
            for line in inf:
                if args.ignore:
                    args.ignore -= 1
                    continue
                acc += line
                proc.stdin.write(line)
                proc.stdin.flush()
                time.sleep(args.time)
                if non_block_read(proc.stdout):
                    i += 1
                    fname = args.output.format(i)
                    print(fname)
                    with open(fname, 'wb') as outf:
                        if args.header:
                            outf.write(args.header.encode())
                        outf.write(acc)
                        if args.footer:
                            outf.write(args.footer.encode())
                    acc = b''
                    while non_block_read(proc.stdout):
                        pass
