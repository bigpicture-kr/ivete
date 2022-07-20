from .arguments import DeployArguments

def deploy(inference, api_name, template_name="default", template_path=None):
    import os
    from flask import Flask, Blueprint, request, jsonify, render_template
    from flask_cors import CORS
    from werkzeug.middleware.dispatcher import DispatcherMiddleware

    if template_path is not None:
        template_folder = os.path.join(template_path, template_name)
    else:
        template_folder = os.path.join(
            os.path.dirname(os.path.abspath(__file__)),
            "templates",
            template_name,
        )
    print(template_folder)

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
