from requests import get
from datetime import datetime

class SuperSaver:

    def __init__(self) -> None:
        pass
    
    def _getCityId(self, city_name:str) -> list:
        headers = {
            "Sec-Ch-Ua": 'Not_A Brand;v=8, Chromium;v=120',
            "Accept": "application/json, text/plain, */*",
            "Accept-Language": "en",
            "Sec-Fetch-Site": "same-origin",
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Dest": "empty",
            "Accept-Encoding": "gzip, deflate, br"
        }
        params = {
            "name": city_name
        }
        request_city_codes = get(f'https://supersaver.sbb.ch/api/v1/locations', params=params, headers=headers, verify=False)
        if request_city_codes.status_code == 200:
            return request_city_codes.json()
        else:
            return ValueError(f"{request_city_codes.json()['error']}")
        
    def getTravels(self, city_code, date:datetime=datetime.today(), time:datetime=datetime.now(), reduction:str="HALF_FARE", segment="ADULT"):
        try:
            requsest_city_id = self._getCityId("nyon")
            city_code = requsest_city_id[0]["id"]
        except ValueError as e:
            print(e)
            return
        
        headers = {
            "Sec-Ch-Ua": 'Not_A Brand;v=8, Chromium;v=120',
            "Accept": "application/json, text/plain, */*",
            "Accept-Language": "en",
            "Sec-Fetch-Site": "same-origin",
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Dest": "empty",
            "Accept-Encoding": "gzip, deflate, br"
        }
        payload = {
            "originId": city_code,
            "date": date.strftime("%Y-%m-%d"),
            "time": time.strftime("%H:%M"),
            "segment": segment,
            "reduction": reduction
        }
        print(payload)
        request = get(f'https://supersaver.sbb.ch/api/v1/destinations', headers=headers, params=payload, verify=False)
        if request.status_code == 200:
            return request.json()
        
 
