import requests

print 'Get Response :'
response = requests.get("http://localhost:5000")
print response.json()

print '\nPOST Response :'
response = requests.post("http://localhost:5000/post", json={"name":"top","charge":"+2/3"})
print response.json()