from flask import Flask, Blueprint, jsonify
import random
import argparse

bp = Blueprint('api', __name__)

@bp.route('/api/health')
def health_check():
    return jsonify({'status': 'OK'}), 200

@bp.route('/random')
def random_number():
    return jsonify({'message': f'Hello world {random.randint(1, 100000)}!'}), 200

app = Flask(__name__)
app.register_blueprint(bp, url_prefix='/my/path')

if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='Start the Flask app.')
    parser.add_argument('--port', type=int, default=8081, help='Port to listen on.')
    args = parser.parse_args()

    app.run(debug=True, host='0.0.0.0', port=args.port)
