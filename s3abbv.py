import stateData



def main(data):
    try:
        stateQuery = input("What State do you need abbreviated?: ")
        stateResult = data[stateQuery]
        print(f"{stateResult.abbreviation} is the shorthand for {stateResult.name} in {stateResult.region}")
    except:
        print("No results. " + stateQuery + " was not found.")



while True:
    data = stateData.getDataFromFile()
    main(data)
    if input("Press enter to continue, type X to close the app.") == "X":
        break
