string = input("Enter a paragraph of text: ")
selection = int(input("Select a number in order to perform an operation\n"
                      "1. Word Count\n"
                      "2. Character Count\n"
                      "3. Capitalize the first letter of each sentence\n"
                      "4. Capitalize all the letters\n"
                      "5. Word Search\n"
                      "6. Replace a word with another word\n"
                      "7. Sort it alphabetically\n"
                      "Select: "))

while selection <= 0 or selection >= 8:
    print("Invalid number, select only one of the choices.")
    selection = int(input("Select a number in order to perform an operation\n"
                          "1. Word Count\n"
                          "2. Character Count\n"
                          "3. Capitalize the first letter of each sentence\n"
                          "4. Capitalize all the letters\n"
                          "5. Word Search\n"
                          "6. Replace a word with another word\n"
                          "7. Sort it alphabetically\n"
                          "Select: "))

if selection == 1:
    words = string.split()
    stringCount = len(words)
    print(f"The number of words you have entered is: {stringCount}")
    exit = input("Enter any character to exit: ")
elif selection == 2:
    stringNoSpaces = len(string.replace(" ", ""))
    print(f"The number of characters excluding spaces is {stringNoSpaces}")
    exit = input("Enter any character to exit: ")
elif selection == 3:
    stringCaps = string.title()
    print(stringCaps)
    exit = input("Enter any character to exit: ")
elif selection == 4:
    stringAllCaps = string.upper()
    print(stringAllCaps)
    exit = input("Enter any character to exit: ")
elif selection == 5:
    stringSearch = input("Enter the word you want to look for: ").strip()
    stringCount2 = string.lower().split().count(stringSearch.lower())
    print(f"The word [{stringSearch}] occurs {stringCount2} time/times in this paragraph.")
    exit = input("Enter any character to exit: ")
elif selection == 6:
    oldString = input("Enter the word you want to replace: ").strip()
    newString = input("Enter the new word you want to replace it with. ").strip()
    updatedString = string.replace(oldString, newString)
    print(f"The new string is: \n{updatedString}")
    exit = input("Enter any character to exit: ")
elif selection == 7:
    string = string.split()
    sortedString = sorted(string, key=str.lower)
    print(f"The sorted list of words is: {sortedString}")
    exit = input("Enter any character to exit: ")