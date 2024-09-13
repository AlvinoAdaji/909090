import requests




FREE_FIRE_API_KEY = 'ضع Api'
FREE_FIRE_API_URL = 'https://www.public.freefireinfo.site/api/info'

token_me = '6685864266:AAEN6vHqbYdfKtLzaoxLMyouPGJSPaCbslI'
id_me = '1933020265'



def fetch_player_info(region, uid):
    url = f"https://www.public.freefireinfo.site/api/info/sg/{player_id}?key=3skr"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return None





def send_multiple_requests(region, uid, view_count):
    success_count = 0
    for _ in range(view_count):
        result = fetch_player_info(region, uid)
        if result:
            success_count += 1
            print(f"send visit for id good {success_count}")
            good=f'send visit for id good {success_count}'
            requests.get("https://api.telegram.org/bot"+str(token_me)+"/sendMessage?chat_id="+str(id_me)+"&text="+str(good))
        else:
            print("error..fox")





region = 'me'
player_id = '1084568572'
send_multiple_requests(region, player_id, 99999)