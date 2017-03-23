#!/usr/bin/env python
# -*- coding: utf-8 -*-

'a test module'

__author__ = 'Chaochao Ye'
__sex = 'male'
import sys
def test():
    args = sys.argv
    if len(args) == 1:
        print 'hello world!'
    elif len(args) == 2:
        print 'hello %s!' % args[1]
    else:
        print 'too many args!'

if __name__ == '__main__':   #只有当单独运行词模块时，__name__ == '__main__'
    test()

def _private1():
    print 'private method can be called!'
