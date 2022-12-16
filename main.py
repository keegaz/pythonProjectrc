import os

import requests

import json

api_key = "7yXwa4Q4.LpzaTiwT0mUTEonUBt2faYjXpcLdTOX9"

asnum = input("Enter ASN Number: ")
response = requests.get("https://www.peeringdb.com/api/net?asn={}".format(asnum))


asn = response.json()['data'][0]['asn']

print ("AS Number: ", asn ,"\n")

id = response.json()['data'][0]['id']

# print ("This is the ID", id, "\n")


api_key = os.environ.get(api_key)

URL = "https://www.peeringdb.com/api/net/{}".format(id)

response = requests.get(URL)

data = response.json()["data"][0]

print(data)

##Calling curl and capuring the output

##response = subprocess.run(['curl','-H', "Authorization: Api-Key $api_key", '-H', "Content-Type: application/json",'-X','GET','https://www.peeringdb.com/api/ix/18'],stdout=subprocess.PIPE)


##Details:
name = response.json()['data'][0]['name']
print(name)
as_num = response.json()['data'][0]['name']
print(as_num)




####LinxLon2
print("\n", "LINX LON 2")
linxlon2 =response.json()['data'][0]['netixlan_set'][0]['name']
print(linxlon2)
linxlon2_ip =response.json()['data'][0]['netixlan_set'][0]['ipaddr4']
print(linxlon2_ip)
linxlon6_ip =response.json()['data'][0]['netixlan_set'][0]['ipaddr6']
print(linxlon6_ip)


print("\nCisco Config")

print("conf t \nrouter bgp 65432")
print(f"bgp neighbour {linxlon2_ip}")

print("\nCisco Config", "IPV6")

print("conf t \nrouter bgp 65432")
print(f"bgp neighbour {linxlon6_ip}")

#####Linxlon1
print(" \n", "Linx Lon 1")
linxlon1_name =response.json()['data'][0]['netixlan_set'][1]['name']
print(linxlon1_name)
linxlon1_ip =response.json()['data'][0]['netixlan_set'][1]['ipaddr4']
print(linxlon1_ip)
linxlon16_ip =response.json()['data'][0]['netixlan_set'][1]['ipaddr6']
print(linxlon16_ip)


#####LONAP
print(" \n", "LONAP")
loanp_name =response.json()['data'][0]['netixlan_set'][2]['name']
print(loanp_name)
lonap_ip =response.json()['data'][0]['netixlan_set'][2]['ipaddr4']
print(lonap_ip)
lonap6_ip =response.json()['data'][0]['netixlan_set'][2]['ipaddr6']
print(lonap6_ip)