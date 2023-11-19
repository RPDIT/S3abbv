import stateData

def main():
    data = stateData.getDataFromFile()
    try :
        stateQuery = input("What State do you need abbreviated?: ")
        stateResult = data[stateQuery]
        print(f"{stateResult.abbreviation} is the shorthand for {stateResult.name} in {stateResult.region}")
    except:
        print("No results. " + stateQuery + " was not found.")


main()
