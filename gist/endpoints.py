#! -*- coding: utf-8 *-

GIST_BASE_URL = "https://api.github.com"

endpoints = {
    'post_gist':
        {
            'url': '/'.join([GIST_BASE_URL, 'gists']),
            'method': 'POST',
        }
}
