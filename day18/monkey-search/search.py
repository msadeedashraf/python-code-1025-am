import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["monkeys-db"]
mycol = mydb["monkeys"]

myquery = {"Name": "Henry"}

mydoc = mycol.find(myquery)

for x in mydoc:
    print(x)
