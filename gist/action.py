#! /usr/bin/env python
# -*- coding: utf-8 -*-


import requests
from gist.endpoints import endpoints


def gist_post(files, public=True, description=None):
    if public:
        try:
            url = endpoints['gist_post']['url']
            r = requests.post
        except KeyError:
            raise KeyError("URL to POST is missing")
