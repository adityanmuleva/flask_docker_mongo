from mongo_config import my_collection

my_data = {
    "fname": "Harish",
    "lname": "Muleva",
    "username": "Harish_muleva@gmail.com",
    "password": "Muleva@1234567"
}

def get_user_data(name):
    data = my_collection.find({"fname": "{}".format(name)})
    print(data)
    for i in data:
        return i

# user_data = get_user_data("Harish")
# print(user_data)
# data = my_collection.insert_one(my_data)
# print(data.inserted_id)