from .arguments import DeployArguments

def deploy(inference, api_name, template_name="default", template_path=None):
    import os
    from flask import Flask, Blueprint, request, jsonify, render_template, send_file
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

    bp = Blueprint(
        api_name,
        __name__,
        template_folder=template_folder,
        static_folder=os.path.join(template_folder, "static/js"),
        static_url_path="/static/js",
    )
    
    @bp.route("/")
    def index():
        return render_template("index.html")

    @bp.route("/manifest.json")
    def manifest():
        file_path = os.path.join(template_folder, "manifest.json")
        return send_file(file_path)

    @bp.route("/favicon.ico")
    def favicon():
        file_path = os.path.join(template_folder, "favicon.ico")
        return send_file(file_path)

    @bp.route("/api", methods=["POST"])
    def api():
        input = request.form
        data = inference(**input)
        response = jsonify(data)
        return response

    @bp.route("/datalist", methods=["GET"])
    def datalist():
        argnames = inference.__code__.co_varnames[:inference.__code__.co_argcount]
        datalist = [{"name": arg, "type": "text"} for arg in argnames]
        response = jsonify(datalist)
        return response

    app = Flask(__name__)
    app.register_blueprint(bp)
    CORS(app)

    return app
