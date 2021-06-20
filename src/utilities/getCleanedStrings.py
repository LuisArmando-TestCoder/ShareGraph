def getCleanedStrings(strings, partsToClean):
    cleanedStrings = []

    for string in  strings:
        cleanedString = string

        for partToClean in partsToClean:
            cleanedString = cleanedString.replace(partToClean, "")

        cleanedStrings.append(cleanedString)

    return cleanedStrings