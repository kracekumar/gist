#! -*- coding: utf-8 *-

GIST_BASE_URL = "https://api.github.com"

endpoints = {
    'gist_post':
        {
            'url': '/'.join([GIST_BASE_URL, 'gists']),
            'method': 'POST',
        }
}
