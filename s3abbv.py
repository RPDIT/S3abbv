import stateData



def main(data):
    try:
        stateQuery = input("\nWhat State do you need abbreviated?: ")
        stateResult = data[stateQuery]
        print(f"""{data.clean_item(stateResult.abbreviation)}
                    \nIs the shorthand for: {data.clean_item(stateResult.name)}
                    \nIn the region: {data.clean_item(stateResult.region)}
                """)
    except:
        print("No results. " + stateQuery + " was not found.")



while True:
    data = stateData.getDataFromFile()
    main(data)
    if input("Press enter to continue, type X to close the app.\n") == "X":
        break
