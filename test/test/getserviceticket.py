import api
import requests
import json
import tabulate

api.print_host()

api.print_device()

s_IP = input("Source IP: ")
#s_IP = "10.1.15.117"
d_IP = input("Destination IP: ")
#d_IP = "10.2.1.22"
flow_url = api.print_flowid(s_IP,d_IP)
print(flow_url)
ticket = api.get_ticket()
headers = {"content-type": "application/json",
               "X-AUTH-TOKEN": ticket}
while True:
    response = requests.get(flow_url, headers=headers, verify=False).json()
    if response["response"]["request"]["status"] == "COMPLETED":
        break
    if response["response"]["request"]["status"] == "FAILED":
        break
    print(response["response"]["request"]["status"])
if response["response"]["request"]["status"] != "FAILED":
    paths = response["response"]["networkElementsInfo"]
    path_list =[]
    i = 0
    for path in paths:
        i = i + 1
        if "ip" in path:
            path_ip = path["ip"]
        else:
            path_ip = "------"
        if "name" in path:
            path_name = path["name"]
        else:
            path_name = "------"
        if "type" in path:
            path_type = path["type"]
        else:
            path_type = "------"
        if "linkInformationSource" in path:
            link_type = path["linkInformationSource"]
        else:
            link_type = "Destination"
        path_list.append([i,
                          path_ip,
                          path_name,
                          path_type,
                          link_type])
        table_header = ["No.",
                        "IP Addess",
                        "Name",
                        "Type",
                        "Link"]
    print(tabulate.tabulate(path_list, table_header))
