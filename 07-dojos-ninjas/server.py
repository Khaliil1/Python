from flask_app import app

from flask_app.controllers import dojo_controller
from flask_app.controllers import ninja_controller

if __name__ == "__main__":
    app.run(debug=True)