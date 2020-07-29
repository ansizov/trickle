from flask import Flask, request, Response, abort, jsonify, render_template
from werkzeug.exceptions import HTTPException
from jinja2 import exceptions
import copy

DEFAULT_DATA = {
    'PROJECT_PATH': '.'
}

try:
    from .settings import *
except ImportError:
    pass

app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True


@app.errorhandler(Exception)
def handle_error(e):
    return jsonify(error=str(e)), e.code if isinstance(e, HTTPException) else 500


@app.route('/', methods=['GET'])
def prepare():
    template = request.args.get('template')
    if template is None:
        abort(400, 'template does not set')

    env_vars = copy.deepcopy(DEFAULT_DATA)
    env_vars.update({key: val for key, val in request.args.items() if key != 'template'})

    try:
        data = render_template(template, data=env_vars)
    except exceptions.TemplateNotFound:
        abort(404, 'template {} does not exists'.format(template))

    return Response(data, mimetype='application/x-yaml')
