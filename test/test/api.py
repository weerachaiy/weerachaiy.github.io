import requests
import json
import tabulate

#requests.packages.urllib3.disable_warnings()

api_base_url = "https://devnetsbx-netacad-apicem-1.cisco.com/api/v1"
api_username = "devnetuser"
api_password = "NTgmY5UY"
api_base_url = "https://devnetsbx-netacad-apicem-2.cisco.com/api/v1"
api_username = "devnetuser"
api_password = "w0ISNW79"
#api_base_url = "https://devnetsbx-netacad-apicem-3.cisco.com/api/v1"
#api_username = "devnetuser"
#api_password = "Xj3BDqbU"
#api_base_url = "https://SandBoxAPICEM.cisco.com/api/v1"
#api_username = "devnetuser"
#api_password = "Cisco123!"

def get_ticket():
    headers = {"content-type": "application/json"}
    api_url = api_base_url + "/ticket"
    payload = {"username": api_username,
               "password": api_password}
    response = requests.post(api_url, json=payload, headers=headers, verify=False).json()
    return response["response"]["serviceTicket"]

def get_hosts(ticket):
    headers = {"content-type": "application/json",
               "X-AUTH-TOKEN": ticket}
    api_url = api_base_url + "/host"
    response = requests.get(api_url, headers=headers, verify=False).json()
    return response["response"]

def get_devices(ticket):
    headers = {"content-type": "application/json",
               "X-AUTH-TOKEN": ticket}
    api_url = api_base_url + "/network-device"
    response = requests.get(api_url, headers=headers, verify=False).json()
    return response["response"]

def print_host():
    ticket = get_ticket()
    print("Service ticket is",ticket)
    hosts = get_hosts(ticket)
    host_list =[]
    i = 0
    for host in hosts:
        i = i + 1
        host_list.append([i,
                          host["hostIp"],
                          host["hostMac"],
                          host["hostType"]])
    table_header = ["No.",
                    "IP Address",
                    "MAC Address",
                    "Type"]
    print(tabulate.tabulate(host_list, table_header))

def print_device():
    ticket = get_ticket()
    print("Service ticket is",ticket)
    devices = get_devices(ticket)
    device_list =[]
    i = 0
    for device in devices:
        i = i + 1
        device_list.append([i,
                            device["managementIpAddress"],
                            device["macAddress"],
                            device["type"]])
    table_header = ["No.",
                    "IP Address",
                    "MAC Address",
                    "Type"]
    print(tabulate.tabulate(device_list, table_header))

def get_flowid(ticket, sourceIP, destIP):
    headers = {"content-type": "application/json",
               "X-AUTH-TOKEN": ticket}
    payload = {"destIP": destIP,
               "sourceIP": sourceIP}
    api_url = api_base_url + "/flow-analysis"
    response = requests.post(api_url, json=payload, headers=headers, verify=False).json()
    return response["response"]

def print_flowid(sourceIP, destIP):
    ticket = get_ticket()
    print("Service ticket is",ticket)
    flow = get_flowid(ticket, sourceIP, destIP)
    #headers = {"content-type": "application/json",
    #           "X-AUTH-TOKEN": ticket}
    api_base_url = "https://devnetsbx-netacad-apicem-2.cisco.com"
    return api_base_url + flow["url"]
