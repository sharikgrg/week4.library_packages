import requests
# import json
request_bbc = requests.get('https://www.bbc.co.uk/')

print(request_bbc.content)

# explore this request package that is installed
# explore http://postcodes.io/

#use requests to make a GET request to http://postcodes.io/ api
# search for a post code (can be your own or any)

# save response in variable

# Use JSON library to unpack it