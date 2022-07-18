from .arguments import DeployArguments

def deploy(inference):
    from flask import Flask, request, jsonify, render_template
    from flask_cors import CORS

    app = Flask(__name__, template_folder='templates')
    CORS(app)

    @app.route('/')
    def index():
        return render_template('index.html')

    @app.route('/api', methods=['POST'])
    def api():
        query = request.json
        #data = inference(...)
        #response = jsonify(data)
        return response

    return app
