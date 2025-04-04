import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")


print(myclient.list_database_names())

# Check if Database Exists
mydblist = myclient.list_database_names()

if "monkeys-db" in mydblist:
    print("The db exists")

mydb = myclient["mydatabase"]
mymonkeydb = myclient["monkeys-db"]
mycol = mydb["customers_1"]

# mydict = {"name": "John", "address": "Highway 37"}

# mycol.insert_one(mydict)

print(myclient.list_database_names())

print(mydb.list_collection_names())
print(mymonkeydb.list_collection_names())

mylist = [
    {"_id": 1, "name": "John", "address": "Highway 37"},
    {"_id": 2, "name": "Peter", "address": "Lowstreet 27"},
    {"_id": 3, "name": "Amy", "address": "Apple st 652"},
    {"_id": 4, "name": "Hannah", "address": "Mountain 21"},
    {"_id": 5, "name": "Michael", "address": "Valley 345"},
    {"_id": 6, "name": "Sandy", "address": "Ocean blvd 2"},
    {"_id": 7, "name": "Betty", "address": "Green Grass 1"},
    {"_id": 8, "name": "Richard", "address": "Sky st 331"},
    {"_id": 9, "name": "Susan", "address": "One way 98"},
    {"_id": 10, "name": "Vicky", "address": "Yellow Garden 2"},
    {"_id": 11, "name": "Ben", "address": "Park Lane 38"},
    {"_id": 12, "name": "William", "address": "Central st 954"},
    {"_id": 13, "name": "Chuck", "address": "Main Road 989"},
    {"_id": 14, "name": "Viola", "address": "Sideway 1633"},
]
# x = mycol.insert_many(mylist)

# print(x.inserted_ids)

y = mycol.find_one()
print(y)

for x in mycol.find():
    print(x)


for z in mycol.find({}, {"_id": 0, "name": 1}):
    print(z)
