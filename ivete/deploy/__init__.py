from .arguments import DeployArguments

def deploy(inference, template_name):
    from flask import Flask, request, jsonify, render_template
    from flask_cors import CORS

    app = Flask(__name__, template_folder=f"templates/{template_name}")
    CORS(app)

    @app.route("/")
    def index():
        return render_template("index.html")

    @app.route("/api", methods=["POST"])
    def api():
        query = request.json['query']
        data = inference(query)
        response = jsonify(data)
        return response

    return app
