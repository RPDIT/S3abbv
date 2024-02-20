import json

dicts = {
    "USdict.json": "US",
    "AUdict.json": "AU",
    "CAdict.json": "CA"
    }


class StateTable:
    def __init__(self):
        self.MAX = 250
        self.arr = [None for i in range(self.MAX)]

    def get_hash(self, key):
        h = 0
        for char in key:
            h += ord(char)
        return h % 100

    def __setitem__(self, key, val):
        h = self.get_hash(self.capit(key))
        item = self.arr[h]
        if item is None:
            self.arr[h] = val
        elif type(item) is list:
            bucket = [val]
            bucket.extend(item)
            self.arr[h] = bucket
        else:
            bucket = [item]
            bucket.append(val)
            self.arr[h] = bucket
        return


    def __getitem__(self, key):
        h = self.get_hash(self.capit(key))
        item = self.arr[h]
        if type(item) is list:
            for i in item:
                if self.capit(key) == self.clean_item(i.name):
                    return i
        elif item:
            return item
        else:
            return print("There is no item with that key")

    def capit(self, key):
        words = key.split(" ")
        output = words.pop(0).capitalize()
        if len(words) >= 1:
            for word in words:
                capped = word.capitalize()
                output = output + f" {capped}"
        return output

    def clean_item(self, string):
        typed_string = str(string)
        unwrapped = typed_string.strip("()")
        released = unwrapped.replace("'", "")
        lineated = released.replace(",", "")
        return lineated


class StateProv:
    def __init__(self, name, abbreviation, region):
        self.name = name,
        self.abbreviation = abbreviation,
        self.region = region


def getDataFromFile():
    data = StateTable()
    for key in dicts:
        fs = open(f"data\{key}", "r")
        fsData = fs.read()
        jsonData = json.loads(fsData)
        fs.close()
        for s in jsonData:
            data[s] = StateProv(s, jsonData[s], dicts[key])
    return data
