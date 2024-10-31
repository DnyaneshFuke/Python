import requests

def get_data_from_api():
    url = "https://api.freeapi.app/api/v1/public/randomusers/user/random"
    response = requests.get(url)
    data= response.json()

    if data['success'] and 'data' in data:
        user = data['data']
        user_name=user['login']['username']
        cointry=user['location']['country']
        return user_name,cointry
    else:
        raise Exception("fail to loade data")
def main():
    try:
        for i in range(5):    
            user_name,cointry=get_data_from_api()
            print()
            print(f"User Name: {user_name}")
            print(f"Country: {cointry}")
    except Exception as e:
        print(e)
    

if __name__ == "__main__":
    main()