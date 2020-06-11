# ***HTTP INTRODUCTION***
# write python code that talks to websites (API requests etc)
# OBJECTIVES:
# - describe what happens when you type a URL in the URL bar
# - describe the request/response cycle
# - explain what a request or response header is, and give examples
# - explain the different categories of response codes
# - compare GET and POST requests

# WHAT HAPPENS WHEN I TYPE GOOGLE.COM IN THE BROWSER?
# 1. DNS Lookup
# 2. Computer makes REQUEST to a server
# 3. Server processes the REQUEST
# 4. Server issues a RESPONSE
# 2,3,4 is the Request/Response cycle

# DNS LOOKUP- like phonebook of the internet
# google.com ---> DNS SERVER ---> 172.217.9.142

# REQUEST AND RESPONSE
# Client --> 172.217.9.142 GET --> Server --> 200 OK --> Client
# 404 response, something went wrong
# 200 is OK
# <!doctype html>
# <hrmo lang="en">
# <!--
#   HTML for google.com
#   will be here!
#   -->
# </html>

# **HTTP HEADERS**
# sent with both requests and responses
# provide additional information about the request or response
# EXAMPLES
# REQUEST HEADERS:
# - ACCEPT - Acceptable content-types for responses (e.g. html, json, xml)
# - CACHE CONTROL - Specify cachine behavior
# - USER AGENT - Information about the software used to make the request
# RESPONSE HEADERS:
# ACCESS-CONTROL-ALLOW-ORIGIN - specify domains that can make requests
# ALLOWED - HTTP verbs that are allowed in requests
# **RESPONSE STATUS CODES**
# - 2xx - SUCCESS
# - 3XX - REDIRECT
# - 4XX - CLIENT ERROR (your fault!)

# ***HTTP VERBS***
# GET & POST
# GET:
# Retuest method is the same as get
# Useful for retrieving data
# Data passed in query strings
# Should have no "side-effects"
# Can be cached
# Can be bookmarked

# POST:
# Useful for writing data
# Data passed in request body
# Can have "side-effects"
# Not cached
# Can't be bookmarked

# API - Application Programming Interface
# reddit.com/.json gives the api version of reddit
# - Allows you to get data from another application without needing to
# understand how the application works
# - Can often send data back in different formats
# - Examples of companies with APIs: GitHub, Spotify, Google
# I could request:
# "api.weather.com"
# And get this back
# "temp" : "78"
# JSON : javascript object notation. standard format now days
# XML used to be standard format.

# ***WRITING YOUR FIRST PYTHON REQUEST***
# **USING THE REQUESTS MODULE**

# import requests
# url = "http://www.google.com"
# response = requests.get(url)
# print(f"Your request to {url} came back with status code {response.status_code}")

# **REQUESTS MODULE**
# lets make HTTP requests from our Python code!
# Installed using pip
# Useful for web scraping/crawling, grabbing data from other APIs, etc

# REQUEST HEADERS

# import requests
# url = "https://icanhazdadjoke.com/"
#
# response = requests.get(url, headers={"Accept" : "application/json"})

# print(response.text)
# print(response.json())
#
# response = requests.get(
#     "https://icanhazdadjoke.com",
#     headers={
#         "header1" : "value1",
#         "header2" : "value2"
#     }
# )
# RESPONSE:
# {"id":"KJmrOKeNexc","joke":"This morning I was wondering where the sun was, but then it dawned on me.","status":200}
#
# >>> print(response.json())
# {'id': 'KJmrOKeNexc', 'joke': 'This morning I was wondering where the sun was, but then it dawned on me.', 'status': 200}

# data = response.json()
# # print(type(data)) # dictionary
# print(data["joke"])

# **SENDING REQUESTS WITH PARAMS**
# WHAT'S A QUERY STRING?
# - A way to pass data to a server as part of a GET request
# - http://www.example.com/?key1=value1&key2=value2

# HOW TO FORMAT A QUERY STRING:
# import requests

# response.get(
#     "http://www.example.com",
#     params={
#         "key1" : "value1",
#         "key2" : "value2"
#     }
# )

# import requests
# url = "https://icanhazdadjoke.com/search"
#
# response = requests.get(
#     url,
#     headers={"Accept" : "application/json"},
#     params={"term" : cat, "limit" : 1}
# )
#
# data = response.json()
# # print(type(data)) # dictionary
# print(data["results"])

# import requests
#
# r = requests.get("https://google.com/")
# print(r.status_code)