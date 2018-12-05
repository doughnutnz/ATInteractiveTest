# # import requests library
import requests

KEY_FILE = ".api-key" # Define file name for subscription key
fin = open(KEY_FILE, "r")  # Open key file, assumed it is there

keydat = fin.read()  # Read the key from the key file, assuming correct format and only data
# print("read data is : ", keydat)

# api-endpoint
# Auckland transport Agencies
URL_AGY = "https://api.at.govt.nz/v2/gtfs/agency"    # AT Agencies url
URL_CAL = "https://api.at.govt.nz/v2/gtfs/calendar"  # AT Calendar url
# AT headers
HEADERS = {'Ocp-Apim-Subscription-Key': keydat}
PARAMS = {'callback': 'JSON'}  # AT params

# Currently Google Maps
# URL = "http://maps.googleapis.com/maps/api/geocode/json"  # G Maps

# Maps location specified here
# location = "AUT University, Auckland"  # G Maps

# Define a dictionary with the needed params for G Maps
# PARAMS = {'address': location}  # G Maps

# Send get request and save the response
# r = requests.get(url=URL, headers=HEADERS, params=PARAMS)  # G Maps
r = requests.get(url=URL_AGY, headers=HEADERS)  # AT Agencies

# Extract data from json
data = r.json()
sendurl = r.url
print("URL used was : ", sendurl)
print("Get HTTPS status code is : ", r.status_code)
print("Type (class) of Get payload is : ", type(data))
print("--------")
data_str = str(data)
len_data_str = len(data_str)
print("Length of data is : ", len_data_str)
if len_data_str > 1000:
  print("Only showing first 1000 characters of Get payload ---->")
  print(data_str[0:1000])
else:
  print("Showing entire Get payload ---->")
  print(data_str)
print("<--------")
print("Internal API status is : ", data["status"])
print("--------")
print("Type (class) of API response is : ", type(data["response"]))
print("--------")
sav_agy0 = data["response"][0]
print("First item of API response is : ", sav_agy0)
print("First Agency Name within API response is : ", data["response"][0]["agency_name"])
print("--------")
print("Internal API error status is : ", data["error"])
print("-------- end --------")


# Now extract latitude, longitude and formatted address
#   of the first matching location
# latitude = data['results'][0]['geometry']['location']['lat']
# longitude = data['results'][0]['geometry']['location']['lng']
# formatted_address = data['results'][0]['formatted_address']

# Print output
# print("Latitude: %s\nLongitude: %s\nFormatted Address: %s" %
#       (latitude, longitude, formatted_address))
