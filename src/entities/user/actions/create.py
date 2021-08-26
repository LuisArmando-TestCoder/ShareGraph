from utilities.addDictionaryToFileStore import addDictionaryToFileStore
from utilities.getBasicValidInput import getBasicValidInput
from utilities.getStore import getStore

filePath = "./entities/user/store.json"

def main():
    userDictionary = {
        "name": getBasicValidInput("Enter your name"),
        "address": getBasicValidInput("Enter the address"),
        "id": getBasicValidInput("Enter your id"),
        "phone": getBasicValidInput("Enter your phone")
    }

    for user in getStore(filePath):
        if user["id"] == userDictionary["id"]:
            print("That user already exists")

            return

    addDictionaryToFileStore(filePath, userDictionary)

    return userDictionary["id"]
