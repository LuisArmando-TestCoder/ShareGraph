import json

def setStore(filePath, store):
    # opens file for write access
    file = open(filePath, "w")
    storeString = json.dumps(store)

    file.write(storeString)
    file.close()