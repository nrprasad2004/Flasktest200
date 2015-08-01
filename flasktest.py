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

	if os.path.isfile("datafile_cf2"):
		file = open("datafile_cf2", "r")
		all_lines = file.readlines()
		file.close()
		mlen = len(all_lines)
		mtemp2 = all_lines[mlen-1]
	else:
		mtemp2=0

	if os.path.isfile("datafile_cf3"):
		file = open("datafile_cf3", "r")
		all_lines = file.readlines()
		file.close()
		mlen = len(all_lines)
		mtemp3 = all_lines[mlen-1]
	else:
		mtemp3=0

	if os.path.isfile("datafile_cf4"):
		file = open("datafile_cf4", "r")
		all_lines = file.readlines()
		file.close()
		mlen = len(all_lines)
		mtemp4 = all_lines[mlen-1]
	else:
		mtemp4=0
		
	if os.path.isfile("datafile_cf5"):
		file = open("datafile_cf5", "r")
		all_lines = file.readlines()
		file.close()
		mlen = len(all_lines)
		mtemp5 = all_lines[mlen-1]
	else:
		mtemp5=0
		
	if os.path.isfile("datafile_cf6"):
		file = open("datafile_cf6", "r")
		all_lines = file.readlines()
		file.close()
		mlen = len(all_lines)
		mtemp6 = all_lines[mlen-1]
	else:
		mtemp6=0

        return render_template('TemperatureMonitor2.html', cf1t1=mtemp1, cf2t1=mtemp2, cf3t1=mtemp3, cf4t1=mtemp4, cf5t1=mtemp5, cf6t1=mtemp6)
        


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
