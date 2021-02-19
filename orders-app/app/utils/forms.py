from werkzeug.datastructures import MultiDict
from wtforms import Form

from flask import request


class JsonForm(Form):
    '''
    Form that automatically picks json data in request object
    '''

    def __init__(self, *args, **kwargs):
        multi_dict_json = MultiDict(request.get_json())
        super().__init__(multi_dict_json, *args, **kwargs)
