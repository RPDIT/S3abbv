import json 

dicts = {"USdict.json":"US","AUdict.json":"AU","CAdict.json":"CA"}

class StateProv:
    def __init__(self, name, abbreviation, region):
        self.name = name, 
        self.abbreviation = abbreviation,
        self.region = region

def getDataFromFile(dictFile):
    fs = open(f"data/{dictFile}", "r")
    fsData = fs.read()
    jsonData = json.loads(fsData)
    fs.close()  
    return jsonData

def main():
    data = {}
    for key in dicts: 
        newData = getDataFromFile(key)
        for s in newData:
            data[s] = StateProv(s, newData[s], dicts[key])
    try :
        stateQuery = input("What State do you need abbreviated?: ")
        stateResult = data[stateQuery]
        print(f"{stateResult.abbreviation} is the shorthand for {stateResult.name} in {stateResult.region}")
    except:
        print("No results. " + stateQuery + " was not found.")


main()
