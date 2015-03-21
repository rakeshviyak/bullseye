from flask import Flask
from flask import render_template,request
import urllib2
import json

import center
import convert


app = Flask(__name__)

@app.route("/",methods=['GET','POST'])
def hello():
	if request.method=='GET':
	   	return render_template('index.html')
	elif request.method=='POST':
		app.logger.debug("asdasd")
		lvalues={}
		location=[]
		onemapApi='http://api.dex.sg/get/onemap/address-search?token=RHhwI69CUqOWViP1fCiTAB3s8pEb6fDMT0P48o61I8JrVXRBeIHEFZcn8qsD0MFzsTnb3HDPIsoubTnLhZ1DFY0%2BG86CcidFbVKbv%2FpcglUYMtLEE8jxlQ%3D%3D%7Cmv73ZvjFcSo%3D&returnGeom=1&rset=1&api_key=sr9y2y33t37czabgmxeeces3&searchVal='
		app.logger.debug(onemapApi)
		add1=request.form['address1']
		add2=request.form['address2']
		add3=request.form['address3']		
		add4=request.form['address4'] 
		if add1:
			# loc1=urllib2.urlopen(onemapApi+add1).read()
			loc=json.loads(urllib2.urlopen(onemapApi+add1).read())
			app.logger.debug(loc)
			app.logger.debug(type(loc["SearchResults"][1]["X"]))
			lvalues['x']=loc["SearchResults"][1]["X"]
			lvalues['y']=loc["SearchResults"][1]["Y"]
			location.append({'x':str(loc["SearchResults"][1]["X"]),'y':str(loc["SearchResults"][1]["Y"])})
			# loc.append(lvalues)
		if add2:
			loc=json.loads(urllib2.urlopen(onemapApi+add2).read())
			app.logger.debug(loc)
			app.logger.debug(loc["SearchResults"][1]["X"])
			lvalues['x']=loc["SearchResults"][1]["X"]
			lvalues['y']=loc["SearchResults"][1]["Y"]
			location.append({'x':loc["SearchResults"][1]["X"],'y':loc["SearchResults"][1]["Y"]})
		if add3:
			loc=json.loads(urllib2.urlopen(onemapApi+add3).read())
			app.logger.debug(loc)
			app.logger.debug(loc["SearchResults"][1]["X"])
			lvalues['x']=loc["SearchResults"][1]["X"]
			lvalues['y']=loc["SearchResults"][1]["Y"]
			location.append({'x':loc["SearchResults"][1]["X"],'y':loc["SearchResults"][1]["Y"]})
			# loc.append(lvalues)
		if add4:
			loc=json.loads(urllib2.urlopen(onemapApi+add4).read())
			app.logger.debug(loc)
			app.logger.debug(loc["SearchResults"][1]["X"])
			lvalues['x']=loc["SearchResults"][1]["X"]
			lvalues['y']=loc["SearchResults"][1]["Y"]
			location.append({'x':loc["SearchResults"][1]["X"],'y':loc["SearchResults"][1]["Y"]})
		app.logger.debug(json.dumps(location))

		cv=convert.SVY21()
		glocation=[]
		for i in location:
			(N,E)=(i['x'],i['y'])
			app.logger.debug(N+E)
			(lat,lon)=cv.computeLatLon(float(E),float(N))
			glocation.append((lat,lon))
			app.logger.debug("lat:%flong:%f",lat,lon)
			app.logger.debug(glocation)
		
		(flat,flon)=center.center_geolocation(glocation);
		app.logger.debug("lat:%flong:%f",flat,flon)
		foursquare_url="https://api.foursquare.com/v2/venues/explore?query=food&oauth_token=EGG1YN4UVKNC1IB1EAD55GCR00YZJDS2SWKTBCS2MBH5DAOY&v=20150321&radius=2000&ll="+str(flat)+","+str(flon);
		app.logger.debug(foursquare_url)

		fs_data=json.loads(urllib2.urlopen(foursquare_url).read())
		
	   	return render_template('index.html',listaddress=fs_data['response']['groups'][0]['items'],glocation=glocation,flat=flat,flon=flon,category=fs_data['response']['query'])


if __name__ == "__main__":
    app.run(debug=True)