# Jawadul Kadir
# SoftDev1 pd7
# HW13 -- A RESTful Journey Skyward
# 2017-11-09

from flask import Flask, render_template
import urllib2
import json

app = Flask(__name__)

@app.route("/")
def root():
	uResp = urllib2.urlopen('https://api.nasa.gov/planetary/apod?api_key=h6FBTp8CveadkLqinR1DfpPfQP151qpDUVfVZOtI');
	data = uResp.read()
	d = json.loads(data)
	print d
	explanation = d["explanation"]
	title = d["title"]
	date = d["date"]
	image = d["hdurl"]
	guy = d["copyright"]
	return render_template('index.html', title = title, date = date, image = image, explanation = explanation, guy = guy)

if __name__ == "__main__":
	app.debug = True
	app.run()
