import os

from glob import glob

from utilities.getCleanedStrings import getCleanedStrings
from utilities.getSelectedOption import getSelectedOption
from utilities.getModuleLikePath import getModuleLikePath

entitiesBaseFolder = "./entities/"

# Gets all the folder paths under entitiesBaseFolder
entitiesNames = glob(f"{entitiesBaseFolder}*")

# Sets all the non existing stores json files
for entity in entitiesNames:
    path = f"{entity}/store.json"

    if not os.path.isfile(path):
        store = open(path, "w")

        store.write("[]")

        store.close()

# List of all the characters to delete from the path to get the bare folder names
baseTrash = ["entities", ".", "/", "\\"]
cleanEntitiesNames = getCleanedStrings(entitiesNames, baseTrash)

# Makes the user input an option from cleanEntitiesNames
selectedSection = getSelectedOption(cleanEntitiesNames)

actionsBaseFolder = f"{entitiesBaseFolder}{selectedSection}/actions/"

actionsNames = glob(f"{actionsBaseFolder}*.py")

cleanActionsNames = getCleanedStrings(
    actionsNames,
    baseTrash + [selectedSection, "actions", "py"]
)

# Select an action which is one of the files under the selected action folder
selectedAction = getSelectedOption(cleanActionsNames)

# Execute the action
moduleLikePath = getModuleLikePath(
    next(
        filter(lambda path: selectedAction in path, actionsNames)
    )
)

# Get action main function from its file
action = __import__(
    moduleLikePath,
    globals(),
    locals(),
    ["main"],
    0
)

# Reproduce the file main function
action.main()
