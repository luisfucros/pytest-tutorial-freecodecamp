import requests

database = {
    1: "alice",
    2: "bob",
    3: "charlie"
}

def get_user_from_db(user_id):
    return database.get(user_id)

def get_users():
    respose = requests.get("https://jsonplaceholder.typicode.com/users")
    if respose.status_code==200:
        return respose.json()
    raise requests.HTTPError
