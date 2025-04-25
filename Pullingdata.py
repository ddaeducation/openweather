# reference: https://openweathermap.org/api/geocoding-api
# import required modules
import requests, json
 
# Enter your API key here
api_key = "2bfefc746a8da258bca71e7114c696a6"

# location details and url
city_name = 'Kicukiro'
location_url = f"http://api.openweathermap.org/geo/1.0/direct?q={city_name}&appid={api_key}"

# get method of requests module
# return response object
response = requests.get(location_url)

# json method of response object 
# convert json format data into
# python format data
print(response.json())

# another way would be to go your browser and type the below, you'll also need a json formatter extension (pretty print)
# http://api.openweathermap.org/geo/1.0/direct?q=Kicukiro&appid=3b207b9e440b84d4f295fd1a361c19f7

# [{"name":"Kicukiro","lat":-1.9854367,"lon":30.1036335,"country":"RW","state":"Kigali City"}]

