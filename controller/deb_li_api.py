__author__ = 'Harsh Daftary'
import requests
import json
from flask import Response, abort
from controller.conf import deb_li_base_url, deb_li_api_url


def json_api(url):
    data = {'method': "add_url", 'params': [url], 'id': "jsonrpc"}
    headers = {'Content-type': 'application/json'}
    r = requests.post(deb_li_api_url, headers=headers, data=json.dumps(data))
    resp = r.json()
    if resp.get('result', False):
        return Response(response=json.dumps({'Success': True, 'Url': str(deb_li_base_url + resp.get('result'))}),
                        status=200,
                        content_type='application/json',
                        mimetype="application/json")
    else:
        return abort(500)