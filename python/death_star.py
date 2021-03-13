import requests, json

url_random = 'https://api.whatdoestrumpthink.com/api/v1/quotes/random'
response_2 = requests.get(url_random)
data_2 = json.loads(response_2.text)

result = data_2['message']

print(result)