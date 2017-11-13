# Jawadul Kadir
# SoftDev1 pd7
# HW14 -- Getting More REST
# 2017-11-09

from flask import Flask, render_template
import urllib2
import json

app = Flask(__name__)

@app.route("/")
def root():
	return render_template('index.html')

@app.route("/nasa")
def nasa():
	uResp = urllib2.urlopen('https://api.nasa.gov/planetary/apod?api_key=h6FBTp8CveadkLqinR1DfpPfQP151qpDUVfVZOtI');
	data = uResp.read()
	d = json.loads(data)
	print d
	explanation = d["explanation"]
	title = d["title"]
	date = d["date"]
	image = d["hdurl"]
	guy = d["copyright"]
	return render_template('nasa.html', title = title, date = date, image = image, explanation = explanation, guy = guy)

@app.route("/urlshortener")
def urlshortener():
	shortUrl = "http://goo.gl/fbsS"
	uResp = urllib2.urlopen('https://www.googleapis.com/urlshortener/v1/url?key=AIzaSyD8_ykTtG6VnHVmtWfH7scM9snncqgxW8E&projection=FULL&shortUrl=' + shortUrl);
	data = uResp.read()
	print data
	d = json.loads(data)
	print d
	longUrl = d['longUrl']
	created = d['created']
	shortUrlClicks = d["analytics"]['allTime']['shortUrlClicks']
	longUrlClicks = d["analytics"]['allTime']['longUrlClicks']
	countries = d["analytics"]['allTime']['countries']
	browsers = d["analytics"]['allTime']['browsers']
	platforms = d["analytics"]['allTime']['platforms']

	return render_template('url_shortener.html', shortUrl = shortUrl, longUrl =longUrl, created = created, shortUrlClicks = shortUrlClicks, longUrlClicks = longUrlClicks, countries = countries, browsers = browsers, platforms = platforms)

if __name__ == "__main__":
	app.debug = True
	app.run()
