#!/usr/bin/python
# -*- coding: UTF-8 -*-
# enable debugging

import cgi, cgitb
cgitb.enable()
import urllib2
import json

print "Content-type:text/html\r\n\r\n"

form = cgi.FieldStorage()

address = form.getvalue('address')
number = form.getvalue('number')

Address = urllib2.quote(address)
geocode_url = "http://maps.googleapis.com/maps/api/geocode/json?address=%s" % Address
req = urllib2.urlopen(geocode_url)
jsonResponse = json.loads(req.read())
data = jsonResponse["results"]
dict = data[0]
geo = dict["geometry"]
loc = geo["location"]
lat = loc["lat"]
lng = loc["lng"]

trucklist = []
foodtruck_url = "https://data.sfgov.org/api/views/rqzj-sfat/rows.json?accessType=DOWNLOAD"
req = urllib2.urlopen(foodtruck_url)
jsonResponse = json.loads(req.read())
trucks = jsonResponse["data"]

for truck in trucks:
	if truck[22] == None or truck[23] == None:
		continue;
	
	trucklist.append({'desc':truck[19], 'lat':truck[22], 'lng':truck[23]})	

print """\
<!DOCTYPE html>
<html>
<head>
<title>Search food trucks nearby</title>
<meta name="viewport" content="initial-scale=1.0, user-scalable=no">
<meta charset="utf-8">
<style>
html, body, #map-canvas {
	height: 100%;
	margin: 0px;
	padding: 0px
}
</style>
<script src="https://maps.googleapis.com/maps/api/js?v=3.exp&libraries=places">
</script>
<script src="http://maps.google.com/maps/api/js?sensor=false&libraries=geometry" type="text/javascript">
</script>   
<script>
var map;
var infowindow;
var myLatlng;

function initialize() {
"""

print "myLatlng = new google.maps.LatLng(%s, %s);" % (lat, lng)

print """\
var mapOptions = {
zoom: 15,
center: myLatlng
}
map = new google.maps.Map(document.getElementById('map-canvas'), mapOptions);
var locs = new Array();
var descs = new Array();
"""
	
i = 0		
for truck in trucklist:
	print "locs[%d] = new google.maps.LatLng(%s, %s);" % (i, truck['lat'], truck['lng'])	
	print "descs[%d] = \"%s\";" % (i, truck['desc'])
	i+=1

print """\
for (var i = 0; i < locs.length; i++) {
createMarker(locs[i], descs[i]);
}
}
function createMarker(loc, desc) {
var distance = google.maps.geometry.spherical.computeDistanceBetween(
myLatlng,
loc
);
distance = distance * 0.000621371192;
"""
print "if (distance <= %s) {" % (number)
print """\
var marker = new google.maps.Marker({
map: map,
position: loc,
title: desc
});
infowindow = new google.maps.InfoWindow();
google.maps.event.addListener(marker, 'click', function() {
infowindow.setContent(marker.title);
infowindow.open(map, this);
});
}
}
google.maps.event.addDomListener(window, 'load', initialize);
</script>
</head>
<body>
<div id="map-canvas"></div>
</body>
</html>
"""

	
	

