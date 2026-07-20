import datetime
import json

from django.http import HttpResponse


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
            return f"{obj:%Y-%m-%d}"
        elif isinstance(obj, datetime.datetime):
            return f"{obj:%Y-%m-%d %H:%M:%S}"
        elif isinstance(obj, datetime.time):
            return f"{obj:%H:%M:%S}"
        raise TypeError(repr(obj) + " is not JSON serializable")


class JSONResponseNotFound(JSONResponse):
    status_code = 404
