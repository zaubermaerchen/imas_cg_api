# -*- coding: utf-8 -*-
from django.http import HttpResponse
import simplejson


class JSONResponse(HttpResponse):
    def __init__(self, content=b'', **kwargs):
        json = simplejson.dumps(content, sort_keys=True)
        
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(json, **kwargs)
        self['Access-Control-Allow-Origin'] = '*'
        self['Access-Control-Allow-Methods'] = 'POST, GET, OPTIONS'
        self['Access-Control-Max-Age'] = '1000'
        self['Access-Control-Allow-Headers'] = '*'


class JSONResponseNotFound(JSONResponse):
    status_code = 404