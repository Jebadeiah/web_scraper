import requests
import json

given_url = input()
r = requests.get(given_url)
the_content = json.loads(r.content)
if r:
    try:
        print(the_content['content'])
    except KeyError:
        print("Invalid quote resource!")
else:
    print("Invalid quote resource!")
