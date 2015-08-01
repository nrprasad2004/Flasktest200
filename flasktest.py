# Hackathon 2015
# ALLSTARS Team
# Author : Rama prasad Nakka 
# Date   : 8/1/2015
from flask import Flask, render_template
import os

app = Flask(__name__)

port = int(os.getenv("VCAP_APP_PORT"))

@app.route('/')
def TemperatureMonitor():
     return render_template('TemperatureMonitor.html')
#    return 'Hello World2 ! I am running on port ' + str(port)

@app.route('/displayAll')
def displaytemperatures():
	if os.path.isfile("datafile_cf1"):
        	file = open("datafile_cf1", "r")
                all_lines = file.readlines()
                file.close()
                mlen = len(all_lines)
                mtemp1 = all_lines[mlen-1]
        else:
                mtemp1=0

        return render_template('TemperatureMonitor2.html', cf1t1=mtemp1)


@app.route('/cf1/<temperature>')
def writecf1(temperature):
	file = open("datafile_cf1", "a")
	file.write(  temperature)
	file.write("\n")
	file.close()
	return("Updated CF1 %s  " %  temperature)


@app.route('/cf2/<temperature>')
def writecf2(temperature):
	file = open("datafile_cf2", "a")
	file.write(  temperature)
	file.write("\n")
	file.close()
	return("Updated CF2 %s  " %  temperature)


@app.route('/cf3/<temperature>')
def writecf3(temperature):
	file = open("datafile_cf3", "a")
	file.write(  temperature)
	file.write("\n")
	file.close()
	return("Updated CF3 %s  " %  temperature)


@app.route('/cf4/<temperature>')
def writecf4(temperature):
	file = open("datafile_cf4", "a")
	file.write(  temperature)
	file.write("\n")
	file.close()
	return("Updated CF4 %s  " %  temperature)


@app.route('/cf5/<temperature>')
def writecf5(temperature):
	file = open("datafile_cf5", "a")
	file.write(  temperature)
	file.write("\n")
	file.close()
	return("Updated CF5 %s  " %  temperature)


@app.route('/cf6/<temperature>')
def writecf6(temperature):
	file = open("datafile_cf6", "a")
	file.write(  temperature)
	file.write("\n")
	file.close()
	return("Updated CF6 %s  " %  temperature)



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=port)
