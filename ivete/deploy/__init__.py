from .arguments import DeployArguments

def deploy(inference, api_name, template_name, template_path=None):
    import os
    from flask import Flask, Blueprint, request, jsonify, render_template
    from flask_cors import CORS
    from werkzeug.middleware.dispatcher import DispatcherMiddleware

    template_folder = os.path.join(template_path, template_name)
    bp = Blueprint(
        api_name,
        __name__,
        template_folder=template_folder,
    )
    
    @bp.route("/")
    def index():
        return render_template("index.html")

    @bp.route("/api", methods=["POST"])
    def api():
        input = request.json
        data = inference(**input)
        response = jsonify(data)
        return response

    app = Flask(__name__)
    app.register_blueprint(bp, url_prefix=f"/{api_name}")
    CORS(app)

    return app
