#! /usr/bin/env python
#! -*- coding: utf-8 -*-

import requests
from gist.endpoints import endpoints
import sys

def main():
    try:
        if not sys.stdin.isatty():
            content = []
            while 1:
                 content.append(sys.stdin.xreadlines().next())
    except StopIteration:
        pass

