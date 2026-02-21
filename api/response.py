# -*- coding: utf-8 -*-
from django.http import HttpResponse
import json
import datetime


class JSONResponse(HttpResponse):
    def __init__(self, content=b'', **kwargs):
        content = json.dumps(content, default=self.support_datetime_default, sort_keys=True)

        kwargs['content_type'] = 'application/json'
        super().__init__(content, **kwargs)
        self['Access-Control-Allow-Origin'] = '*'
        self['Access-Control-Allow-Methods'] = 'POST, GET, OPTIONS'
        self['Access-Control-Max-Age'] = '1000'
        self['Access-Control-Allow-Headers'] = '*'

    @staticmethod
    def support_datetime_default(obj):
        if isinstance(obj, datetime.date):
            return "{0:%Y-%m-%d}".format(obj)
        elif isinstance(obj, datetime.datetime):
            return "{0:%Y-%m-%d %H:%M:%S}".format(obj)
        elif isinstance(obj, datetime.time):
            return "{0:%H:%M:%S}".format(obj)
        raise TypeError(repr(obj) + " is not JSON serializable")


class JSONResponseNotFound(JSONResponse):
    status_code = 404
