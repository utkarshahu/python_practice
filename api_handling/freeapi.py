import requests

def fetch_random_user_data():
    url = "https://api.freeapi.app/api/v1/public/randomusers/user/random"
    response = requests.get(url)
    data = response.json()

    if data["success"] and "data" in data :
        user_data = data["data"]["user"]
        username = user_data["login"]["username"]
        country = user_data["location"]["country"]
        return username, country
    else:
        print("API responded but with error or unexpected structure:", data)
        raise Exception("Failed to raise userdata ")


def main():
    try:
        # Call the function and print result
        username,country = fetch_random_user_data()
        print(f"Username: {username} Country:{country} ")
    except Exception as e:
        print(str(e))
        
    

    
    
if __name__ =="__main__":
    main()

