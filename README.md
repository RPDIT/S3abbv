# S3abbv

A python tool, created out of my own frustration at work, to return the postal abbreviation of the given state/province. Using data that was originally downloaded as a CSV, convert a list of each relevent country's State Name/Abbreviation pairs into a python Dictionary of the same key/value pairs.

The application iterates through a dictionary of Region Codes and filepaths as key value pairs, opening each file under a specific region code to iterate through each each dictionary to create State Objects that intake each State's Name, Abbreviation, and Region. Each State object is then stored in a dictionary with its full name as the key.

With the data loaded into an active dictionary, the application prompts the user for an input of the full state name.


# Updates 

02/20/2024 - I have been experimenting with hash maps in other languages and decided to try implementing one here. It uses a hashing function that finds the MOD of each character to determine its key, then places the state object at that position on the hash map. 

```
$ python s3abbv.py
What State do you need abbreviated?: Queensland
('QLD',) is the shorthand for ('Queensland',) in AU
Press enter to continue, type X to close the app.
What State do you need abbreviated?: Florida
('FL',) is the shorthand for ('Florida',) in US
Press enter to continue, type X to close the app.
What State do you need abbreviated?: Hawaii
('HI',) is the shorthand for ('Hawaii',) in US
Press enter to continue, type X to close the app.
What State do you need abbreviated?: Europe
No results. Europe was not found.
Press enter to continue, type X to close the app.
```
