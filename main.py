__author__ = 'harsh'
import json
from flask import Flask, request, Response, abort, url_for
from controller.conf import bind_address, bind_port
from controller.request_parser import AddEntry, GetEntry,GetDownload
from controller.helper import FlaskError
import gc
app = Flask(__name__, static_url_path='')


@app.errorhandler(403)
@app.errorhandler(500)
@app.errorhandler(404)
def error(something):
    return Response(response=json.dumps(FlaskError().get_error()), status=500, content_type='application/json',
                    mimetype="application/json")


@app.route('/add', methods=['GET', 'POST'])
def add():
    gc.collect()
    data = request.get_json(force=True)
    print(data)
    if data:
        r = AddEntry(data)
        resp = r.get_resp()
        del r
        return resp
    else:
        return Response(response=json.dumps(FlaskError("Provide valid json data in POST request").get_error()),
                        status=400, content_type='application/json',
                        mimetype="application/json")


@app.route('/get/<session_id>', methods=['GET'])
def get(session_id):
    gc.collect()
    if session_id:
        return GetEntry(session_id=session_id).get_resp()
    else:
        return Response(response=json.dumps(FlaskError("Provide valid session id in GET parameters").get_error()),
                        status=400, content_type='application/json',
                        mimetype="application/json")


@app.route('/download/<session_id>', methods=['GET'])
def download(session_id):
    gc.collect()
    if session_id:
        r = GetDownload(session_id=session_id)
        resp = r.get_resp()
        del r
        return resp
    else:
        return Response(response=json.dumps(FlaskError("Provide valid session id in GET parameters").get_error()),
                        status=400, content_type='application/json',
                        mimetype="application/json")


if __name__ == '__main__':
    gc.enable()
    app.run(host=bind_address, port=int(bind_port))