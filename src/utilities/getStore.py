import json

def getStore(filePath):
    # opens file with read access to extract its contents
    file = open(filePath, "r")

    store = json.load(file)

    file.close()

    return store