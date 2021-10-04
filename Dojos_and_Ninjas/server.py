from flask_app import app #from __init___
from flask_app.controllers import dojos, ninjas

if __name__ == "__main__":
    app.run(debug=True)