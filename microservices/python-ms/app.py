import logging
import os
from flask import Flask, Blueprint, jsonify
import random
import argparse

bp = Blueprint('api', __name__)

@bp.route('/api/health')
def health_check():
    return jsonify({'status': 'OK'}), 200

@bp.route('/api/random')
def random_number():
    return jsonify({'message': f'Hello world {random.randint(1, 100000)}!'}), 200

app_path = os.environ.get('SERVER_SERVLET_CONTEXT_PATH', '')
logging.info('app_path: %s', app_path)

app = Flask(__name__)
app.register_blueprint(bp, url_prefix=app_path)
logging.warning("URL Map %s",app.url_map)

if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='Start the Flask app.')
    parser.add_argument('--port', type=int, default=8081, help='Port to listen on.')
    args = parser.parse_args()

    app.run(debug=True, host='0.0.0.0', port=args.port)
