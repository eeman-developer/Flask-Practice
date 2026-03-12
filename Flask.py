from flask import Flask

# wcu py Flask.py or use the python extension in vs code thus which shows the run button

app = Flask(__name__)

# @app.route("/") http://127.0.0.1:5000 
@app.route("/api") # http://127.0.0.1:5000/api
def hello_world():
    return "<p>Hello, World!</p>"

# after running this file, wcu any of below. as localhost is name for http://127.0.0.1. localhost is a hostname, 127.0.0.1 is the loopback IP
# http://127.0.0.1:5000/api
# http://localhost:5000/api
if __name__ == "__main__":
    app.run(debug=True)

# after running this server, what ever changes you do and save the file, the data will be auto updated in the webpage (ie http://localhost:5000/api). 5000 is the default port for flask


