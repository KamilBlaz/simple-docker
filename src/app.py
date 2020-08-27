
from flask import Flask, request
from datetime import datetime
import socket
 

app = Flask(__name__)

  
@app.route("/date")
def index():
     return (str(datetime.now()))

@app.route("/hostname")
def return_hostname():
     return " {} to {} \n ".format(socket.gethostname(), request.remote_addr)

@app.route("/boo")
def text():
    with open('/boo.txt', 'r') as f:
        out = f.read()
        return out

if __name__ == '__main__':
    app.run(debug=True, port=3000, host='0.0.0.0')
