from flask import Flask, Blueprint, jsonify
import random
import argparse
import os
import logging

app = Flask(__name__)


@app.route('/api/health')
def health_check():
    return jsonify({'status': 'OK'}), 200

@app.route('/api/random')
def random_number():
    return jsonify({'message': f'Hello world {random.randint(1, 100000)}!'}), 200

if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='Start the Flask app.')
    parser.add_argument('--port', type=int, default=8081, help='Port to listen on.')
    args = parser.parse_args()

    # app_path = os.environ.get('SERVER_SERVLET_CONTEXT_PATH', '')
    # logging.warning("app_path: %s", app_path)

    # app.config['APPLICATION_ROOT'] = app_path
    app.run(debug=True, host='0.0.0.0', port=args.port)
