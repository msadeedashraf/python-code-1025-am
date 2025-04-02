# In this code we will send the monkey data into  the mongodb
import requests
import json
import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mymonkeydb = myclient["monkeys-db"]
mymonkeycol = mymonkeydb["monkeys"]

url = "https://raw.githubusercontent.com/jamesmontemagno/app-monkeys/master/MonkeysApp/monkeydata.json"


try:
    response = requests.get(url)

    if response.status_code == 200:
        myData = response.json()
        # print(json.dumps(myData, indent=4))
        try:
            mymonkeycol.insert_many(myData)

            # f2 = open("../files/monkey.json", "a")
            # f2.write(json.dumps(myData, indent=4))

        except (
            FileNotFoundError,
            PermissionError,
            IsADirectoryError,
            OSError,
            EOFError,
        ) as err:
            print(f"Error : {err}")

    else:
        print(f"Error while fetching: Error Code: {response.status_code}")
except requests.exceptions.RequestException as err:
    print(f"Request failed: {err}")
