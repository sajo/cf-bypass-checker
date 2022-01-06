#coding: utf-8
import json,requests,logging
urlZones = 'https://api.cloudflare.com/client/v4/zones/?per_page=100'

headers = {'content-type': 'application/json','Authorization': 'Bearer *****************'}

r = requests.get(urlZones, headers=headers)
zones = r.json()


for zone in zones["result"]:
    DNSREC = requests.get("https://api.cloudflare.com/client/v4/zones/"+zone["id"]+"/dns_records?per_page=200" , headers=headers)
    dnsList = DNSREC.json()
    for dns in dnsList["result"]:
        if(dns["type"] == "A"):
            try:
                site = requests.get("http://"+dns["content"], headers={'Host': dns["name"]})
                if(site.status_code != 403):
                    logging.warning(dns["name"]+":Cloud Armor Disabled")
                    print(dns["name"]+":Cloud Armor Disabled")
            except:
                logging.warning(dns["name"]+":Error")
                print(dns["name"]+":Error")
            
        
            
       



