import requests
import json

url = "https://raw.githubusercontent.com/jamesmontemagno/app-monkeys/master/MonkeysApp/monkeydata.json"


try:
    response = requests.get(url)

    if response.status_code == 200:
        myData = response.json()
        # print(json.dumps(myData, indent=4))

        f2 = open("../files/monkey.json", "a")
        f2.write(json.dumps(myData, indent=4))
    else:
        print(f"Error while fetching: Error Code: {response.status_code}")
except requests.exceptions.RequestException as err:
    print(f"Request failed: {err}")
