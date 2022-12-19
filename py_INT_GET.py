import requests
import sys
import urllib3
proxies = {'http' : 'http://127.0.0.1:8080', 'https': 'https://127.0.0.8080'}
r = requests.get("http://info.cern.ch", verify=False, proxies=proxies )
#c1=  c1 = {'session':"djsklfjdslkjfklds8543793"}
# r = requests.get("https://mysslortlssite.com", cookies=c1, verify=False )
print(r) # Return code
print(r.text) # Return page data
# Data may get squeezed --> Options > Config Idle > Shell/Ed > Large minimum of autosqueeze so not squeezed. 
