# make a list to hold onto out items
shoppingList = []

# print out the list
def showItems():
    print("Here's your list:")
    for item in shoppingList:
        print(item)

def showHelp():
    print("""
Enter 'DONE' to stop adding items.
Enter 'SHOW' to see your current list.
Enter 'HELP' for this help.
""")

def addToList(newItem):
    # add new items to our list
        shoppingList.append(newItem)
        print("Added {}.  List now has {} items.".format(newItem, len(shoppingList)))

# print out instructions on how to use the app
showHelp()
print("What should we pick up at the store?")

while True:
    # ask for new items
    newItem = input("> ")

    # be able to quit the app
    if newItem == 'DONE':
        showItems()
        break
    elif newItem == "SHOW":
        showItems()
        continue
    elif newItem == "HELP":
        showHelp()
        continue
    addToList(newItem)
