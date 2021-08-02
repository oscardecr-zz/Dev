import os
import pathlib
inputfile = None

path = pathlib.Path(__file__).parent.absolute()
current_path = str(path)


#load json files path
builradat_domain = "{}/data_domain_www.buildarat.com_0.json".format(current_path)
builradat_domain_2 = "{}/data_domain_www.buildarat.com_1.json".format(current_path)

disorderstatus_domain = "{}/data_domain_www.disorderstatus.ru_0.json".format(current_path)
disorderstatus_domain_2 = "{}/data_domain_www.disorderstatus.ru_1.json".format(current_path)

garatinterbk_domain = "{}/data_domain_www.garatinterbk.online_0.json".format(current_path)
garatinterbk_domain_2 = "{}/data_domain_www.garatinterbk.online_1.json".format(current_path)

hngleg_domain = "{}/data_domain_www.hngleg.online_0.json".format(current_path)
hngleg_domain_2 = "{}/data_domain_www.hngleg.online_1.json".format(current_path)

pionsecar_domain = "{}/data_domain_www.pionsecar.com_0.json".format(current_path)
pionsecar_domain_2 = "{}/data_domain_www.pionsecar.com_1.json".format(current_path)

#Check if data.json 0 and 1 exists for each domain, so we make sure that they are deleted each 2 days 
if os.path.exists(builradat_domain):
    os.remove(builradat_domain)
if os.path.exists(builradat_domain_2):
    os.remove(builradat_domain_2)
if os.path.exists(disorderstatus_domain):
    os.remove(disorderstatus_domain)
if os.path.exists(disorderstatus_domain_2):
    os.remove(disorderstatus_domain_2)
if os.path.exists(garatinterbk_domain):
    os.remove(garatinterbk_domain)
if os.path.exists(garatinterbk_domain_2):
    os.remove(garatinterbk_domain_2)
if os.path.exists(hngleg_domain):
    os.remove(hngleg_domain)
if os.path.exists(hngleg_domain_2):
    os.remove(hngleg_domain_2)
if os.path.exists(pionsecar_domain):
    os.remove(pionsecar_domain)
if os.path.exists(pionsecar_domain_2):
    os.remove(pionsecar_domain_2)
