from glob import glob
from utilities.getCleanedStrings import getCleanedStrings
from utilities.getSelectedOption import getSelectedOption
from utilities.getModuleLikePath import getModuleLikePath

# Select a section
entitiesBaseFolder = "./entities/"
entitiesNames = glob(f"{entitiesBaseFolder}*")
baseTrash = ["entities", ".", "/", "\\"]
cleanEntitiesNames = getCleanedStrings(entitiesNames, baseTrash)
selectedSection = getSelectedOption(cleanEntitiesNames)

# Select an action
actionsBaseFolder = f"{entitiesBaseFolder}{selectedSection}/actions/"
actionsNames = glob(f"{actionsBaseFolder}*.py")
cleanActionsNames = getCleanedStrings(
    actionsNames,
    baseTrash + [selectedSection, "actions", "py"]
)
selectedAction = getSelectedOption(cleanActionsNames)

# Execute the action
moduleLikePath = getModuleLikePath(
    next(
    )
)

# Get action from file
action = __import__(
    moduleLikePath,
    globals(),
    locals(),
    ['main'],
    0
)

# Reproduce file action
action.main()
