"""Cloud Foundry test"""
from flask import Flask, render_template
import os

app = Flask(__name__)

port = int(os.getenv("VCAP_APP_PORT"))

@app.route('/')
def TemperatureMonitor():
     return render_template('TemperatureMonitor.html')
#    return 'Hello World2 ! I am running on port ' + str(port)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=port)
