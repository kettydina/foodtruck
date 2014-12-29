Version 1.0 12/28/2014

Problem Description
--------------------
Create a service that tells the user what types of food trucks might be found near a specific location on a map.
To get the service, the user has to access to the web server via a browser.

The problem includes three questions.
1. How to design the web page to let the user input information?
   The information should at least includes two parts: the specific address and the search scope.

2. How to get the data about food trucks nearby?
   Download the data from website in Json format.

3. How to show the food trucks on a map?
   Parse the Json information and use google map APIs to mark truck places.

==============================================================================================================================



Solution Description
-----------------------
The solution focuses on both front-end and back-end.

The solution only includes two files named index.html and search.py.

Since I have to parse Json and show the web page dynamically, I Chose Python in back-end.
The httpd web server supports CGI (common gateway interface) and I could communicate between the httpd and Python script.

The first page index.html includes two inputs and a submit button.
It is almost in HTML.
And there is a Javascript function to check if the inputs are valid.
If you click submit button, the check function will be called and if the inputs are OK,
the inputs will be handled by a python file and corresponding trucks will be shown on the next page.

The python file search.py first gets the latitude and longitude of the input address via Google Map API.
Then, it will use library functions to get the information of the trucks in Json.
Finally, it will check the distance between each truck and the center via latitude and longitude in Javascript.
If the distance is not greater than the radius the user input, the truck will be marked on the map.

===============================================================================================================================


 
Trade-offs
-------------
If I have additional time on the project, I will do several things to make my project better.

1. Use cache to avoid frequent query from website https://data.sfgov.org/api/views/rqzj-sfat/rows.json?accessType=DOWNLOAD.
   Add a configurable expiration time to control the cache.
   
2. Beautify the index.html and implement creative and additional features a user might find useful.
   For example, let user input the number of trucks he/she would like to show on the map;
                let user input expiration time of the cache.

3. Add more conditions to check the user inputs.
  
4. Use google maps API for Python instead of google maps API for Javascript to compute the distance between two locations and sort
   all distances and put necessary information into a list of dictionaries locally to accelerate the process.

5. For the trucks with the same latitude and longitude, the title of the marker on the map should include all food items of all trucks.

6. Display the routes from the center to the truck when the user click the truck marker.

=========================================================================================================================================



Installing the service application under Linux
--------------------------------------------------
First, make sure httpd is running on your web server.
Second, put index.html under html folder and search.py under cgi-bin folder.
The index.html is the default web page when you input the web server's address in the browser.
Third, make sure python has been installed on your Linux web server.
If the service doesn't work, maybe the python path in the python file is incorrect.
Use 'whereis python' command to find your python path and modify the corresponding content in search.py (the first line).
 
===========================================================================================================================



Link to my public profile
-----------------------------
http://www.linkedin.com/pub/yaqin-li/42/512/bb9/

======================================================================



Link to the hosted application
------------------------------------
http://ec2-54-67-96-156.us-west-1.compute.amazonaws.com/



