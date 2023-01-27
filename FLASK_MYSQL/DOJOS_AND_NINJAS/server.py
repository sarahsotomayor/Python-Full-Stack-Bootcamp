from flask_app import app
from flask_app.controllers import dojo_routes, ninja_routes



if __name__=="__main__":
    app.run(debug=True)