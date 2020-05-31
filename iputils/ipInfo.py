import requests
from common.log import logUtils as log

def getIpAera(ip, aera="CN"):
    addresses = ["http://ip-api.com/json/{}", "https://ip.zxq.co/{}"]
    for address in addresses:
        try:
            log.info("try to get ip {} aera".format(ip))
            address = address.format(ip)
            response = requests.get(address.format(ip))
            if response.status_code != 200:
                continue
            if response.text in (None, "", "null\n"):
                continue
            ipData = response.json()
            if "countryCode" in ipData:
                aera = ipData.get("countryCode", aera)
                break
            elif "country" in ipData:
                aera = ipData.get("country", aera)
                break
        except Exception as err:
            log.error("ERROR WHEN: getIpAera, {}".format(str(err)))
    
    return aera
        
