# Application Program Interface (API) - we can program this application access and manipulation.
# Silent Installer = run with parameters.
# REST = REpresentational State Transfer.
from flask import Flask
app = Flask(__name__)
@app.route('/')
def hello_world():
   a, b = 5, 10
   return f'{a} + {b} = {a + b}'

app.run(host='127.0.0.1')