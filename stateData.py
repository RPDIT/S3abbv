import json 

dicts = {"USdict.json":"US","AUdict.json":"AU","CAdict.json":"CA"}


class StateProv:
    def __init__(self, name, abbreviation, region):
        self.name = name, 
        self.abbreviation = abbreviation,
        self.region = region

def getDataFromFile():
    data = {}
    for key in dicts: 
        fs = open(f"data/{key}", "r")
        fsData = fs.read()
        jsonData = json.loads(fsData)
        fs.close()  
        for s in jsonData:
            data[s] = StateProv(s, jsonData[s], dicts[key])
    return data