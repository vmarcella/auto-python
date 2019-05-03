import requests

url = "http://www.columbia.edu/~fdc/sample.html"
response = requests.get(url)

print(response)

print("\n--STATUS CODE--")
print(response.status_code)  # Print the status code of the response
print("\n--HEADERS--")
print(response.headers)  # Print the headers of the response
print("\n--TEXT RESPONSE--")
print(response.text)  # Print the text version of the response
print("\n--URL--")
print(response.url)  # Print the url the request was made to
