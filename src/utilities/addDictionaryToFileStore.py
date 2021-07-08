import json

def addDictionaryToFileStore(filePath, dictionary):
    # opens file with read access to extract its contents
    file = open(filePath, "r")
    store = json.load(file)

    store.append(dictionary)
    file.close()

    # opens file for write access
    file = open(filePath, "w")
    storeString = json.dumps(store)

    file.write(storeString)
    file.close()