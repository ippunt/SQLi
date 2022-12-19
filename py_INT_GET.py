import requests
import sys
import urllib3
proxies = {'http' : 'http://127.0.0.1:8080', 'https': 'https://127.0.0.8080'}
r = requests.get("http://info.cern.ch", verify=False, proxies=proxies )
# r = requests.get("http://info.cern.ch", cookies="ciijue", verify=False, proxies=proxies )
print(r) # Return code
print(r.text) # Return page data
