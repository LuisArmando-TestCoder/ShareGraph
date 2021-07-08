def getBasicValidInput(inputMessage):
    value = ""

    while not value: value = input(f"{inputMessage}: ")

    return value