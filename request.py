import requests
url = 'http://localhost:5000/api'
r = requests.post(url,json={'exp':[[6.7, 3.1, 5.6, 2.4]],})
print(r.json())