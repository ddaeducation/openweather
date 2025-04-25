# import required modules
import requests, json
 
# Enter your API key here
api_key = "2bfefc746a8da258bca71e7114c696a6"
city_name = 'Kigali'

# base_url variable to store forecast
base_url = f"https://api.openweathermap.org/data/2.5/forecast?q={city_name}&appid={api_key}"

# get method of requests module
# return response object
response = requests.get(base_url)

# json method of response object 
# convert json format data into
# python format data
print(response.json())