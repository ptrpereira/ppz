#!/usr/bin python

import sys


def hide(msg):
    s = ''
    for i in msg:
        s += chr(ord(i) + 7)
    return s


def show(msg):
    s = ''
    for i in msg:
        s += chr(ord(i) - 7)
    return s


args = sys.argv[1:]
r = ''
if args[0] == 'hide':
    r = hide(args[1])
    myFile = open('/home/pereira/password.txt', 'w')
    myFile.write(r)
elif args[0] == 'show':
    r = show(args[1])
print(r)
