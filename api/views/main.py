from api.core.application import application

@application.route("/ping")
def index():
    return "pong"
