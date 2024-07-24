def extractAddresses(filePath):
        from re import compile
        regexSearchPattern = compile(r'\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b')
        extractedAddresses = []
        with open(filePath, "r") as file:
            for line in file:
                matchedIpAddresses = regexSearchPattern.findall(line)
                for ip in matchedIpAddresses:
                    parts = ip.split('.')
                    if all(0 <= int(part) <= 255 for part in parts):
                        extractedAddresses.append(ip)
            print("Extracted IP's: ", extractedAddresses)


extractAddresses(".txt file here")









    



