#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    : entry.py
@Time    : 2023/09/06 22:52:46
@Author  : yangp
@Contact : yangp@wanyantech.com
@Version : 0.1
@License : Apache License Version 2.0, 2023 yangp
@Desc    : None
'''

import sys
import traceback
from typing import Callable
from setttings import CODEBASE


def getfunc(mod:str, func:str)->Callable:
    try:
        sys.path.append(CODEBASE)
        module = __import__(mod)
        func = getattr(module, func)
        return func
    except:
        raise traceback.format_exc()
    finally:
        sys.path.pop(-1)



def run(module:str,func:str, *args, **kwargs):
    function = getfunc(module, func)
    return function(*args, **kwargs)


if __name__ == '__main__':
    run('datastack', 'deploy')