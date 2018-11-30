# import requests library
import requests

# api-endpoint
# Auckland transport
URL = "https://api.at.govt.nz/v2/gtfs/agency"  # AT url
# AT headers
HEADERS = {'Ocp-Apim-Subscription-Key': "a0e149fb205d41b5bbfda64798c9d55b"}
PARAMS = {'callback': 'JSON'}  # AT params

# Currently Google Maps
# URL = "http://maps.googleapis.com/maps/api/geocode/json"  # G Maps

# Maps loaction specified here
# location = "AUT University, Auckland"  # G Maps

# Define a dictionary with the needed params for G Maps
# PARAMS = {'address': location}  # G Maps

# Send get request and save the response
# r = requests.get(url=URL, headers=HEADERS, params=PARAMS)  # G Maps
r = requests.get(url=URL, headers=HEADERS)  # AT

# Extract data from json
data = r.json()
sendurl = r.url
print(sendurl)
print(r.status_code)
print(type(data))
print(data)
print(data[status])
# Now extract latitude, longitude and formatted address
#   of the first matching location
# latitude = data['results'][0]['geometry']['location']['lat']
# longitude = data['results'][0]['geometry']['location']['lng']
# formatted_address = data['results'][0]['formatted_address']

# Print output
# print("Latitude: %s\nLongitude: %s\nFormatted Address: %s" %
#       (latitude, longitude, formatted_address))
