import json
from re import compile

def extractAddresses(filePath):
    regexSearchPattern = compile(r'\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b')
    extractedAddresses = []

    def find_ips_in_data(data):
        if isinstance(data, dict):
            for value in data.values():
                find_ips_in_data(value)
        elif isinstance(data, list):
            for item in data:
                find_ips_in_data(item)
        elif isinstance(data, str):
            matchedIpAddresses = regexSearchPattern.findall(data)
            extractedAddresses.extend(matchedIpAddresses)

    if filePath.endswith('.json'):
        with open(filePath, "r") as file:
            data = json.load(file)
            find_ips_in_data(data)
    else:
        with open(filePath, "r") as file:
            for line in file:
                matchedIpAddresses = regexSearchPattern.findall(line)
                extractedAddresses.extend(matchedIpAddresses)

    print("Extracted IPs: ", extractedAddresses)

extractAddresses("ip.txt")





    



