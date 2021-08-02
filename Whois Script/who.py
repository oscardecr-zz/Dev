#!/usr/bin/python
# For Python v.3 and later
from urllib.request import urlopen, pathname2url
import yaml
import json
from datetime import date
import os
import pathlib

#get current path
path = pathlib.Path(__file__).parent.absolute()
current_path = str(path)

#load YAML
a_yaml_file = open("{}/domains.yml".format(current_path))
parsed_yaml_file = yaml.load(a_yaml_file, Loader=yaml.FullLoader)

list = parsed_yaml_file.get("domains")


#variables 
apiKey = 'at_ur0GuxUMHnh7RZIMkbs4CXDXnUlmh'
y = 0
counter = 0

#request whois service
for x in list:
    if os.path.exists('{}/data_domain_{}_{}.json'.format(current_path,list[y],counter)):
        url = 'https://www.whoisxmlapi.com/whoisserver/WhoisService?'\
        + 'domainName=' + x + '&apiKey=' + apiKey + "&outputFormat=JSON"
        with open('data_domain_{}_{}.json'.format(list[y],counter+1), 'w') as outfile:
            result = urlopen(url).read().decode('utf8')
            outfile.write(result)
        y += 1
    else:
        url = 'https://www.whoisxmlapi.com/whoisserver/WhoisService?'\
        + 'domainName=' + x + '&apiKey=' + apiKey + "&outputFormat=JSON"
        with open('data_domain_{}_{}.json'.format(list[y],counter), 'w') as outfile:
            result = urlopen(url).read().decode('utf8')
            outfile.write(result)
        y += 1

 
