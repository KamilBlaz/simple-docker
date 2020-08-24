
from flask import Flask
from datetime import datetime

 

app = Flask(__name__)

  
@app.route("/date")
def index():
     return (str(datetime.now()))

       
if __name__ == '__main__':
     app.run(debug=True, port=3000, host='0.0.0.0')
