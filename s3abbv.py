import stateData



def main():
    try :
        stateQuery = input("What State do you need abbreviated?: ")
        stateResult = data[stateQuery]
        print(f"{stateResult.abbreviation} is the shorthand for {stateResult.name} in {stateResult.region}")
    except:
        print("No results. " + stateQuery + " was not found.")


data = stateData.getDataFromFile()

while True:
    main()
    if input("Do you with to continue? Enter X to close.") == "X":
        break
